# Sistem Pemesanan Travel Agent

Sistem pemesanan hotel berbasis microservices modern yang memungkinkan pengguna untuk memesan hotel mewah di seluruh Indonesia dan memproses pembayaran dengan mudah.

## 🌟 Fitur

- Jelajahi hotel-hotel mewah di seluruh Indonesia
- Proses pemesanan yang mudah
- Dukungan berbagai metode pembayaran
- Pelacakan status pemesanan secara real-time
- Pemrosesan pembayaran yang aman

## 🏗️ Arsitektur

Sistem terdiri dari dua microservices:

1. **Layanan Pemesanan** (Port 5001)
   - Mengelola daftar hotel
   - Menangani pembuatan pemesanan
   - Melacak status pemesanan
   - Menyediakan antarmuka manajemen pemesanan

2. **Layanan Pembayaran** (Port 5002)
   - Memproses pembayaran
   - Mendukung berbagai metode pembayaran
   - Mengelola status pembayaran
   - Menyediakan riwayat pembayaran

## 🚀 Memulai

### Prasyarat
- Python 3.8 atau lebih tinggi
- pip (Python package manager)
- Web browser (Chrome, Firefox, atau Safari direkomendasikan)

### Langkah-langkah Instalasi

1. Clone repository atau unduh file proyek:
```bash
git clone <your-repository-url>
cd travel-agent-project
```

2. Buat dan aktifkan virtual environment (direkomendasikan):
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/MacOS
python -m venv venv
source venv/bin/activate
```

3. Install dependensi yang diperlukan:
```bash
pip install flask requests
```

### Menjalankan Aplikasi

1. Mulai Layanan Pembayaran terlebih dahulu:
```bash
cd payment_service
python payment_service.py
```
Layanan akan berjalan di http://localhost:5002

2. Buka terminal baru dan mulai Layanan Pemesanan:
```bash
cd booking_service
python booking_service.py
```
Layanan akan berjalan di http://localhost:5001
