# PintarBelanja - Kalkulator Diskon

## Deskripsi Program
PintarBelanja adalah aplikasi web kalkulator diskon berbasis Python Flask yang membantu pengguna menghitung harga akhir suatu barang setelah mendapatkan potongan diskon.

## Tujuan Pembuatan
- Mempraktikkan penggunaan fungsi (function) dalam framework Python Flask
- Melatih kemampuan pemrograman menggunakan Python
- Memahami komponen dalam framework Flask seperti routing, template HTML, dan static file
- Membuat aplikasi web yang berguna bagi masyarakat umum

## Cara Kerja Program

### Input
- **Nama Barang** — nama produk yang ingin dihitung diskonnya (tipe data: String)
- **Harga Asli (Rp)** — harga original barang sebelum diskon (tipe data: Float)
- **Persentase Diskon (%)** — besar potongan harga dalam persen (tipe data: Float)

### Proses
Data dikirim ke server Flask melalui form POST, lalu diproses oleh fungsi hitung_diskon():

```python
def hitung_diskon(harga_asli, persen_diskon):
    potongan = harga_asli * (persen_diskon / 100)
    harga_akhir = harga_asli - potongan
    return potongan, harga_akhir

```

### Output
- Nama barang yang dihitung
- Harga asli barang  
- Persentase diskon
- Jumlah potongan harga (Rp)
- Harga akhir setelah diskon (Rp)

## Rumus Perhitungan
Potongan Harga = Harga Asli x (Persentase Diskon / 100)
Harga Akhir    = Harga Asli - Potongan Harga

## Teknologi yang Digunakan
- Python
- Flask
- HTML
- CSS
- Jinja2

## Cara Menjalankan Program
1. Install Flask: pip install flask
2. Masuk ke folder: cd kalkulator_diskon
3. Jalankan: python app.py
4. Buka browser: http://127.0.0.1:5000

## Tampilan Website

### Halaman Utama
![Halaman Utama](Cuplikan%20layar%202026-04-12%20214555.png)

### Halaman Input
![Halaman Input](Cuplikan%20layar%202026-04-12%20214631.png)

### Halaman Hasil
![Halaman Hasil](Cuplikan%20layar%202026-04-12%20214654.png)

## Pembuat
Nama: Ratna Wulandari
NIM: 250907501004
