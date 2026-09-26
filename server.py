import http.server
import socketserver
import json
import csv
import os
import webbrowser
import sys

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(DIRECTORY, "kayit.csv")

# Ensure kayit.csv exists with headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Ad Soyad", "Oda No", "Avatar", "Avatar Basligi", "Puan", "Tamamlanan Gorevler", "Kayit Tarihi"])
        writer.writerow(["CBÜ-2026-101", "Efe Yılmaz", "204", "🦁", "Cesur Aslan", "25", "task-water;task-food", "26.09.2026"])
        writer.writerow(["CBÜ-2026-102", "Zeynep Kaya", "108", "🦢", "Zarif Kuğu", "55", "task-water;task-food;task-hygiene;task-medicine", "26.09.2026"])
        writer.writerow(["CBÜ-2026-103", "Ali Demir", "312", "🐯", "Güçlü Kaplan", "10", "task-hygiene", "26.09.2026"])

def read_patients_csv():
    patients = []
    if not os.path.exists(CSV_FILE):
        return patients

    try:
        with open(CSV_FILE, mode="r", newline="", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            header = next(reader, None)
            for row in reader:
                if not row or len(row) < 3:
                    continue
                patient_id = row[0].strip() if len(row) > 0 else ""
                name = row[1].strip() if len(row) > 1 else ""
                room = row[2].strip() if len(row) > 2 else ""
                avatar = row[3].strip() if len(row) > 3 else "🦁"
                avatar_title = row[4].strip() if len(row) > 4 else "Cesur Aslan"
                points = 0
                if len(row) > 5:
                    try:
                        points = int(row[5].strip())
                    except ValueError:
                        points = 0
                
                completed_tasks = []
                if len(row) > 6 and row[6].strip():
                    completed_tasks = [t.strip() for t in row[6].strip().split(";") if t.strip()]
                
                created_at = row[7].strip() if len(row) > 7 else ""

                patients.append({
                    "id": patient_id,
                    "name": name,
                    "room": room,
                    "avatar": avatar,
                    "avatarTitle": avatar_title,
                    "points": points,
                    "completedTasks": completed_tasks,
                    "createdAt": created_at
                })
    except Exception as e:
        print(f"CSV Okuma Hatasi: {e}")
    return patients

def write_patients_csv(patients):
    try:
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Ad Soyad", "Oda No", "Avatar", "Avatar Basligi", "Puan", "Tamamlanan Gorevler", "Kayit Tarihi"])
            for p in patients:
                tasks_str = ";".join(p.get("completedTasks", []))
                writer.writerow([
                    p.get("id", ""),
                    p.get("name", ""),
                    p.get("room", ""),
                    p.get("avatar", "🦁"),
                    p.get("avatarTitle", "Cesur Aslan"),
                    p.get("points", 0),
                    tasks_str,
                    p.get("createdAt", "")
                ])
        return True
    except Exception as e:
        print(f"CSV Yazma Hatasi: {e}")
        return False

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        if self.path == '/api/patients':
            patients = read_patients_csv()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps(patients, ensure_ascii=False).encode('utf-8'))
        elif self.path == '/api/status':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok", "file": "kayit.csv", "count": len(read_patients_csv())}).encode('utf-8'))
        elif self.path == '/' or self.path == '':
            self.path = '/Kid_inferance.html'
            super().do_GET()
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/api/patients':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            try:
                data = json.loads(body.decode('utf-8'))
                if isinstance(data, list):
                    success = write_patients_csv(data)
                    self.send_response(200 if success else 500)
                    self.send_header('Content-Type', 'application/json; charset=utf-8')
                    self.end_headers()
                    self.wfile.write(json.dumps({"success": success, "count": len(data)}).encode('utf-8'))
                    return
            except Exception as e:
                print(f"POST Islem Hatasi: {e}")

            self.send_response(400)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Gecersiz veri"}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def run():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"==================================================")
        print(f"🏥 CBÜ Çocuk Servisi Portalı Başlatıldı!")
        print(f"📁 Bilgiler 'kayit.csv' dosyasında anlık tutulmaktadır.")
        print(f"🌐 Adres: http://localhost:{PORT}")
        print(f"==================================================")
        
        url = f"http://localhost:{PORT}/Kid_inferance.html"
        try:
            webbrowser.open(url)
        except Exception:
            pass

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nSunucu kapatıldı.")

if __name__ == '__main__':
    run()
