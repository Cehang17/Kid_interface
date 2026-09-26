@echo off
chcp 65001 > nul
title CBU Cocuk Portali - CSV Veritabani
echo ====================================================
echo  CBÜ Çocuk Servisi Portalı Başlatılıyor...
echo  Kayıtlar 'kayit.csv' dosyasına anlık yazılacaktır.
echo ====================================================
python -X utf8 server.py
pause
