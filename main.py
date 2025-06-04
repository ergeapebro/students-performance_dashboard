"""
main.py

Aplikasi Streamlit untuk memprediksi risiko mahasiswa dropout berdasarkan performa akademik
dan kondisi administratif pada dua semester pertama.

Model yang digunakan: Random Forest (dengan 10 fitur terpilih melalui feature selection)

Fitur input:
- proporsi_sks_1: Rasio SKS lulus terhadap SKS diambil pada semester 1
- proporsi_sks_2: Rasio SKS lulus terhadap SKS diambil pada semester 2
- Curricular_units_2nd_sem_approved: SKS lulus semester 2
- Ipk_sem2: IPK semester 2
- Ipk_sem1: IPK semester 1
- Curricular_units_1st_sem_approved: SKS lulus semester 1
- delta_ipk: Perubahan IPK antara semester 2 dan semester 1
- Age_at_enrollment: Usia mahasiswa saat mendaftar
- Tuition_fees_up_to_date: Apakah pembayaran kuliah lunas (1: Ya, 0: Tidak)
- status_pembayaran: Gabungan dari status pelunasan dan penunggakan

Author: Ergeape
"""

import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load('model.joblib')

# Judul aplikasi
st.title("🎓 Prediksi Risiko Dropout Mahasiswa")

st.markdown("Masukkan informasi mahasiswa berdasarkan dua semester pertama:")

# Input data
col1, col2 = st.columns(2)

with col1:
    sem1_enrolled = st.number_input(
        "SKS yang Diambil Semester 1", min_value=0, max_value=25, value=20)
    sem1_approved = st.number_input(
        "SKS yang Lulus Semester 1", min_value=0, max_value=25, value=20)
    ipk_1 = st.slider("IPK Semester 1", min_value=0.0,
                      max_value=4.0, value=3.0)
    sem2_enrolled = st.number_input(
        "SKS yang Diambil Semester 2", min_value=0, max_value=25, value=20)
    sem2_approved = st.number_input(
        "SKS yang Lulus Semester 2", min_value=0, max_value=25, value=20)
    ipk_2 = st.slider("IPK Semester 2", min_value=0.0,
                      max_value=4.0, value=3.0)

with col2:
    usia = st.number_input("Usia saat pendaftaran kuliah",
                           min_value=16, max_value=60, value=19)
    biaya_lunas = st.selectbox(
        "Apakah pembayaran kuliah lunas?", ["Ya", "Tidak"])
    penunggak = st.selectbox("Apakah menunggak biaya kuliah?", ["Ya", "Tidak"])
    # status_pembayaran: 1 = Lunas dan Bukan Penunggak, selain itu = 0
    status_pembayaran = 1 if (
        biaya_lunas == "Ya" and penunggak == "Tidak") else 0

# Prediksi saat tombol diklik
if st.button("Prediksi"):
    # Hitung fitur turunan
    proporsi_sks_1 = sem1_approved / sem1_enrolled if sem1_enrolled != 0 else 0
    proporsi_sks_2 = sem2_approved / sem2_enrolled if sem2_enrolled != 0 else 0
    delta_ipk = ipk_2 - ipk_1
    tuition_fees_up_to_date = 1 if biaya_lunas == "Ya" else 0

    # Susun input sesuai urutan top10_features
    input_data = np.array([[
        proporsi_sks_2,
        proporsi_sks_1,
        sem2_approved,
        ipk_2,
        ipk_1,
        sem1_approved,
        delta_ipk,
        usia,
        tuition_fees_up_to_date,
        status_pembayaran
    ]])

    # Prediksi
    pred = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0]

    # Tampilkan hasil
    status = "🔴 Dropout" if pred == 1 else "🟢 Tidak Dropout"
    st.subheader(f"Hasil Prediksi: {status}")
    st.caption(
        f"Probabilitas Dropout: {proba[1]:.2f} | Tidak Dropout: {proba[0]:.2f}")
