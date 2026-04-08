from flask import Flask, render_template, request

app = Flask(__name__)

def hitung_diskon(harga_asli, persen_diskon):
    potongan = harga_asli * (persen_diskon / 100)
    harga_akhir = harga_asli - potongan
    return potongan, harga_akhir

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hitung', methods=['POST'])
def hitung():
    nama_barang = request.form['nama_barang']
    harga_asli = float(request.form['harga_asli'])
    persen_diskon = float(request.form['persen_diskon'])
    potongan, harga_akhir = hitung_diskon(harga_asli, persen_diskon)
    return render_template('hasil.html',
                           nama_barang=nama_barang,
                           harga_asli=harga_asli,
                           persen_diskon=persen_diskon,
                           potongan=potongan,
                           harga_akhir=harga_akhir)

if __name__ == '__main__':
    app.run(debug=True)
