# 🎓 Dashboard Analisis dan Sistem Prediksi Risiko Dropout Mahasiswa

## 🗂️ Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### 🔍 Permasalahan Bisnis
Perguruan tinggi menghadapi tantangan serius dalam mempertahankan kelulusan mahasiswanya. Beberapa permasalahan bisnis yang ingin diselesaikan dalam proyek ini meliputi:

1. **Deteksi Dini Risiko Dropout**  
   Kurangnya sistem deteksi dini menyebabkan kampus kesulitan mengidentifikasi mahasiswa yang berpotensi putus studi (dropout), hingga terlambat memberikan intervensi.

2. **Kurangnya Visualisasi Data Akademik & Finansial**  
   Pihak institusi belum memiliki dashboard interaktif untuk memantau performa akademik, status pembayaran biaya kuliah, hingga IPK mahasiswa secara menyeluruh.

3. **Minimnya Insight dari Data Historis Mahasiswa**  
   Data mahasiswa yang ada belum dimanfaatkan secara optimal untuk mengidentifikasi pola-pola yang berhubungan dengan risiko akademik dan dropout.

4. **Ketidakjelasan Prioritas Intervensi**  
   Sulit menentukan mahasiswa mana yang perlu diintervensi lebih dulu berdasarkan risiko dropout tertinggi.

### 📌 Cakupan Proyek
Cakupan proyek ini meliputi:
1. Eksplorasi dan Pra-pemrosesan Data.
2. Membangun dashboard interaktif untuk menampilkan temuan secara visual, dengan pendekatan user-friendly untuk pemangku kepentingan kampus.
3. Mengembangkan solusi machine learning untuk mendeteksi risiko dropout mahasiswa berdasarkan variabel akademik dan finansial.
4. Menerjemahkan visualisasi menjadi insight dan rekomendasi kebijakan untuk pihak kampus.


### ⚙️ Persiapan
* Data : Students' Dropout and Academic Success
* Sumber data : [UCI](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)
* Dataset ini dibuat dari lembaga pendidikan tinggi (diperoleh dari beberapa basis data terpisah) yang terkait dengan mahasiswa yang terdaftar dalam berbagai gelar sarjana, seperti agronomi, desain, pendidikan, keperawatan, jurnalisme, manajemen, layanan sosial, dan teknologi. Dataset tersebut mencakup informasi yang diketahui pada saat pendaftaran mahasiswa (jalur akademik, demografi, dan faktor sosial-ekonomi) dan kinerja akademik mahasiswa pada akhir semester pertama dan kedua. Data tersebut digunakan untuk membangun model klasifikasi guna memprediksi putus sekolah dan keberhasilan akademik mahasiswa. Masalah tersebut diformulasikan sebagai tugas klasifikasi tiga kategori, yang di dalamnya terdapat ketidakseimbangan yang kuat terhadap salah satu kelas.

**Setup Environment - Anaconda** :
```
conda create --name myenv python=3.10
conda activate myenv
pip install -r requirements.txt
```
**Setup Environment - Shell/Terminal** :
```
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```
## 📊 Business Dashboard

Dashboard ini berfungsi sebagai alat bantu analisis visual untuk memantau performa mahasiswa dari berbagai sisi:

### Visualisasi yang Ditampilkan:

1. **Total Mahasiswa & Status**  
  Ringkasan jumlah mahasiswa per kategori: Graduate, Enrolled, Dropout.

2. **Proporsi Status Mahasiswa**  
  Visualisasi donut chart menunjukkan proporsi status mahasiswa.

3. **Rata-rata SKS Lulus**  
  Bar chart semester 1 & 2 berdasarkan status mahasiswa.

4. **Rata-rata IPK**  
  Bar chart distribusi IPK semester 1 & 2 berdasarkan status mahasiswa.

5. **Proporsi Usia Mahasiswa**  
  Distribusi mahasiswa berdasarkan kelompok usia.

6. **Proporsi Biaya Kuliah (Paid vs Unpaid)**  
  Menampilkan tingkat kepatuhan terhadap pembayaran.

7. **Jumlah Mahasiswa Berdasarkan Status Debtor & Beasiswa**  
  Visualisasi side-by-side untuk melihat peran faktor finansial terhadap status.

Berikut adalah tautan akses ke dashboard online: 👉 [Lihat Dashboard Tableau](https://public.tableau.com/views/students_performance/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## 🚀 Menjalankan Sistem Machine Learning
Untuk menjalankan prototype sistem prediksi dropout mahasiswa, ikuti langkah berikut:
1. Clone repository atau salin semua file proyek ke dalam satu direktori.
2. Pastikan semua file model (.joblib) tersedia di folder.
3. Jalankan aplikasi Streamlit dengan perintah:
```
streamlit run main.py
or
python -m streamlit run main.py
```
4. Akses aplikasi melalui browser di:
```
http://localhost:8501
```
### 🔗 Akses Online Prototype

Prototype juga dapat diakses secara online melalui Streamlit Cloud:

[Link Streamlit](https://prediction-of-student-dropout.streamlit.app/)

## ✅ Conclusion

Dari hasil eksplorasi data, ditemukan beberapa temuan penting:

1. Mahasiswa dengan IPK rendah dan jumlah SKS yang sedikit, terutama pada semester pertama, memiliki kemungkinan lebih tinggi untuk dropout.
2. Kelompok usia 17–21 tahun mendominasi populasi mahasiswa, namun juga memiliki distribusi dropout yang signifikan.
3. Faktor keuangan, seperti status pembayaran biaya kuliah dan kepemilikan beasiswa, turut berkontribusi terhadap kelulusan mahasiswa.
4. Sebagian besar mahasiswa telah melunasi biaya kuliah, namun segmen kecil yang tidak membayar memiliki tingkat dropout yang lebih tinggi.

Dashboard interaktif yang dikembangkan menampilkan informasi ini secara ringkas dan dapat diakses oleh pemangku kebijakan, memungkinkan monitoring performa mahasiswa secara real-time.

Sementara itu, model machine learning yang dibangun mampu memprediksi status kelulusan mahasiswa berdasarkan kombinasi variabel akademik dan demografis. Model ini membuka peluang untuk sistem peringatan dini (early warning system) yang dapat membantu lembaga melakukan intervensi sebelum mahasiswa benar-benar memutuskan untuk keluar.

Dengan demikian, proyek ini tidak hanya menjawab permasalahan bisnis saat ini, tetapi juga menjadi fondasi penting dalam menciptakan lingkungan pendidikan yang lebih adaptif, inklusif, dan berbasis data.


### 🎯 Rekomendasi Action Items

Berikut adalah beberapa langkah konkret yang direkomendasikan untuk institusi:

1. Terapkan Sistem Early Warning 
  Implementasikan model prediktif ke dalam sistem akademik untuk mendeteksi mahasiswa berisiko tinggi secara otomatis setiap semester.

2. Lakukan Intervensi Dini terhadap Mahasiswa Rentan 
  Prioritaskan pembimbingan, konseling, atau pendampingan akademik terhadap mahasiswa yang terdeteksi berisiko tinggi.

3. Monitoring Rutin melalui Dashboard
  Gunakan dashboard untuk pemantauan berkala performa akademik dan keuangan mahasiswa agar keputusan intervensi dapat dilakukan berbasis data real-time.

4. Tinjau Kebijakan Beasiswa dan Pembayaran
  Evaluasi ulang skema pemberian beasiswa dan rancang program bantuan finansial yang lebih terarah untuk kelompok rentan.

5. Perluas Fitur Prediktif di Masa Depan 
  Kembangkan lebih lanjut model machine learning dengan memasukkan variabel tambahan seperti kehadiran, partisipasi kelas, dan data survey kepuasan mahasiswa.

