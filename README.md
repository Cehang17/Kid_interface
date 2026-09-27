# 🏥 Hastanedeki Gizli Haritam - Çocuk Oryantasyon Portalı

Bu proje, çocuk hastaların hastane ortamına alışmasını, merak ve cesaret duygusuyla korkularını yenmesini sağlayan oyunlaştırılmış bir çocuk oryantasyon ve klinik motivasyon portalıdır.

---

## 👩‍⚕️ Hemşire Yönetim & Canlı Görev Takip Paneli (Dashboard)

Hemşire Abla modu, gereksiz tüm karmaşık dosya/teknik detaylardan arındırılarak **gerçek bir klinik yönetim paneli** haline getirilmiştir:

* **👶 Hızlı Çocuk Seçimi & Geçiş:**
  * Servisteki tüm çocukları canlı arama (isim veya oda numarası) ile filtreleyebilir, tek tıkla **"Seç & Profile Geç"** diyerek o çocuğun aktif görünümüne geçebilirsiniz.
* **🎯 6 Temel Görev Takip Matrisi (Canlı Durum):**
  * Her çocuğun kartında günlük 6 görevinin tamamlanma durumu anlık renkli rozetlerle takip edilir:
    * 💧 **Su**: Su içme görevi (✅ / ⏳)
    * 🥗 **Yemek**: Sağlıklı beslenme görevi (✅ / ⏳)
    * 🧼 **El Yıkama**: Mikrop avcısı el hijyeni (✅ / ⏳)
    * 💊 **İlaç**: Tedavi uyumu & cesaret (✅ / ⏳)
    * 🌙 **Uyku**: Dinlenme & uyku vakti (✅ / ⏳)
    * 🎬 **Video**: Servis tanıtım videosu tamamlama (✅ / ⏳)
* **🎴 QR Kimlik Kartı & Güvenlik Yetkilendirmesi:**
  * **Hemşire Modunda:** Bağlantıyı Kopyala, Yeni Sekmede Aç ve Rozet Formatında Yazdır butonları tam yetkili olarak çalışır.
  * **Çocuk Modunda:** Çocuk kendi kartına girdiğinde bu butonlar gizlenir, sadece sevimli QR kartını ve puanlarını görüntüler.
* **🔒 Güvenli Çocuk Moduna Kilit:**
  * Telefonu çocuğa teslim ederken tek tıkla **"Kitle 🔒"** butonuna basılır ve tüm yetkili paneller kilitlenir.

---

## 🌟 Dinamik QR Kod Sistemi & Yeni Eklenen Her Çocuk İçin Özel Tasarım

Sistemde **her yeni eklenen çocuk için anında özel QR kimlik kartı ve rozeti** otomatik olarak tasarlanır ve üretilir:

1. ➕ **Yeni Hasta Kaydı:**
   - Hemşire adını ve oda numarasını girer, çocuk kendi sevimli maskotunu (🦁, 🦖, 🦢 vb.) seçer.
   - Kayıt tamamlandığı an **Özel QR Kutlama & Kart Ekranı** açılır.
   - **"Kartı / Rozeti Yazdır"** butonuyla hastanın yatağına/dolabına asılacak ya da velisine verilecek resmi Celal Bayar Üniversitesi kahraman yaka kartı çıkartılabilir.

2. 🎴 **Tüm Kahraman QR Kartları Merkezi:**
   - "Kartım ✨" bölümündeki **"Tüm QR Kartları"** sekmesinde tüm çocukların QR kodları canlı listelenir ve toplu yazdırılabilir.

---

## 👩‍⚕️ Şifreli Hemşire Abla Giriş Bilgileri:
- **Kullanıcı Adı:** `hemsire` *(veya `admin`)*
- **Şifre:** `1234` *(veya `cbu2026`)*

---

## 📁 Canlı CSV (`kayit.csv`) Veritabanı

Sistemde yapılan **tüm işlemler anında `kayit.csv` dosyasına kaydedilir**:
* ➕ **Yeni Çocuk Eklendiğinde**: `kayit.csv` dosyasına yeni kayıt anında işlenir.
* 🗑️ **Çocuk Silindiğinde**: `kayit.csv` dosyasından anında kaldırılır.
* ⭐ **Görev veya Puan Kazanıldığında**: Tamamlanan görevler ve puan anlık güncellenir.
* 📁 **Dosya Konumu**: Çalışma dizinindeki `kayit.csv` dosyasıdır. Excel ile de çift tıklayarak doğrudan açabilirsiniz.

---

## 🌐 Netlify ve Canlı Web Yayınlama (Hosting)

Site, Netlify üzerinde doğrudan çalışacak şekilde yapılandırılmıştır (`_redirects`, `netlify.toml` ve `index.html` yönlendirmeleri hazırdır):
1. Projeyi GitHub'a bağlayıp Netlify'da tek tıkla canlıya alabilirsiniz.
2. QR kodlarının canlı site adresinize (örn: `https://cemile-site.netlify.app`) göre üretilmesi için QR modalındaki **"Ayarlar ⚙️"** sekmesinden özel alan adınızı kaydedebilirsiniz.

---

## 📱 Telefondan Test Etme ve QR Kullanımı

1. **Yerel Ağda:** `baslat.bat` dosyasını çalıştırın. Konsolda çıkan yerel ağ adresini (örnek: `http://192.168.1.X:8000`) göreceksiniz.
2. **Canlıda:** Netlify linkinizi veya yerel adresi açın.
3. Telefonunuzun kamerasını ekrandaki QR kodlardan birine tutun ve açılan bağlantıya dokunun.
4. **Telefon doğrudan o çocuğun profiliyle şifresiz açılır**, çocuk sadece kendi hesabında güvenle oyununu oynar ve puanlarını toplar!
