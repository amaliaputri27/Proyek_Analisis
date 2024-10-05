import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Judul Aplikasi
st.title("Bike sharing dataset ✨")
st.write("Nama: Amalia Putri")
st.write("Email: m384b4kx0446@bangkit.academy")
st.write("ID Dicoding: aleailearn")



#BABABABAB

# Menghitung rata-rata suhu dan jumlah penyewaan langsung, tanpa groupby
mean_workingday = df_workingday[['temp', 'cnt']].mean()
mean_holiday = df_holiday[['temp', 'cnt']].mean()

# Set style
sns.set(style="whitegrid")

# Menambahkan offset untuk membuat bar bersanding
bar_width = 0.35  # Lebar bar
index = np.arange(2)  # Indeks posisi untuk kategori (hari kerja dan hari libur)

# Bar plot untuk hari kerja dan hari libur
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot untuk 'cnt' (Jumlah Penyewaan) dengan warna biru
bars1 = ax1.bar(index - bar_width / 2, [mean_holiday['cnt'], mean_workingday['cnt']], 
                bar_width, color='blue', label='Jumlah Penyewaan', alpha=0.6)

# Membuat sumbu y kedua untuk 'temp' (Suhu)
ax2 = ax1.twinx()
bars2 = ax2.bar(index + bar_width / 2, [mean_holiday['temp'], mean_workingday['temp']], 
                bar_width, color='orange', label='Suhu (temp)', alpha=0.9)

# Menambahkan label, judul, dan legend
plt.title('Rata-rata Suhu dan Jumlah Penyewaan pada Hari Kerja dan Hari Libur', fontsize=16)
ax1.set_xlabel('Kategori', fontsize=14)
ax1.set_ylabel('Jumlah Penyewaan', fontsize=14)
ax2.set_ylabel('Suhu (temp)', fontsize=14)

# Modifikasi label pada sumbu x
ax1.set_xticks(index)  # Set tick positions
ax1.set_xticklabels(['Hari Libur', 'Hari Kerja'])  # Set tick labels

# Menambahkan legend
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Menambahkan nilai pada bar
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom')

for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')

# Tampilkan plot
plt.show()
