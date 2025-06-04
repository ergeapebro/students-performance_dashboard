# Student's Performance - Dashboard
# 🔰 Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## 🗂️ Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### 🔍 Permasalahan Bisnis
Tuliskan seluruh permasalahan bisnis yang akan diselesaikan.

### 📌 Cakupan Proyek
1. Membuat dashboard untuk membantu Jaya Jaya Institut dalam memahami data dan memonitor performa siswa.
2. Mengembangkan solusi machine learning.
3. Membuat kesimmpulan dan merekomendasikan action items.

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
Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

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

[Link Streamlit]()

## ✅ Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### 🎯 Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
