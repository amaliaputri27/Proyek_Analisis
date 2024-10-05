import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Judul Aplikasi
st.title("Bike Sharing Dataset ✨")
st.write("Nama: Amalia Putri")
st.write("Email: m384b4kx0446@bangkit.academy")
st.write("ID Dicoding: aleailearn")

# Load the dataset
df_day = pd.read_csv('Data/day.csv')

# Exploratory Data Analysis (EDA)
st.title("Exploratory Data Analysis (EDA)")

# Random sampling of all rows
df_day_sample = df_day.sample(frac=1)

# Descriptive statistics for DAY
st.subheader('Descriptive Statistics for Day Data')
st.write("Statistika deskriptif dilakukan untuk memahami karakteristik data, termasuk ukuran pusat, penyebaran, dan pola.")
day_stats = df_day_sample.describe(include='all')
st.write(day_stats)

# Plot histograms for selected features
st.subheader('Histograms of Selected Features')
st.write("Analisis histogram dan KDE (Kernel Density Estimation) untuk kolom 'cnt' (jumlah penyewaan) ini membantu dalam pengambilan keputusan strategis berdasarkan pola distribusi jumlah penyewaan.")
fig, ax = plt.subplots(figsize=(10, 8))
df_day_sample[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].hist(bins=30, ax=ax)
plt.suptitle('Histogram of DAY Data')
st.pyplot(fig)

# Plot histogram with seaborn for 'cnt' column
st.subheader('Distribusi Kolom cnt')
st.write("Analisis distribusi kolom 'cnt' memberikan wawasan yang berguna untuk pengambilan keputusan strategis dalam konteks penyewaan.")
fig2, ax2 = plt.subplots(figsize=(8, 6))
sns.histplot(df_day_sample['cnt'], kde=True, ax=ax2)
ax2.set_title('Distribusi Kolom cnt')
ax2.set_xlabel('Jumlah Penyewaan (cnt)')
ax2.set_ylabel('Frekuensi')
st.pyplot(fig2)

# Korelasi untuk DAY
st.subheader('Analisis Korelasi')
st.write("Analisis korelasi ini memberikan pemahaman mendalam tentang faktor-faktor yang mempengaruhi jumlah penyewaan sepeda.")
df_day_numeric = df_day.select_dtypes(include=[np.number])
day_corr = df_day_numeric.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(day_corr, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Heatmap for DAY Data')
st.pyplot(plt)

# Menghitung korelasi Pearson antara temp dan cnt
correlation = df_day['temp'].corr(df_day['cnt'])
st.write(f"Korelasi antara suhu (temp) dan jumlah penyewaan (cnt) pada dataset DAY: {correlation}")

# Scatter plot untuk visualisasi
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df_day['temp'], y=df_day['cnt'])
plt.title('Hubungan antara Suhu (temp) dan Jumlah Penyewaan (cnt) pada Dataset DAY')
plt.xlabel('Suhu (temp)')
plt.ylabel('Jumlah Penyewaan (cnt)')
st.pyplot(plt)

# Membagi data menjadi hari kerja dan hari libur
df_workingday = df_day[df_day['workingday'] == 1]
df_holiday = df_day[df_day['workingday'] == 0]

# Menghitung korelasi Pearson
correlation_workingday = df_workingday['temp'].corr(df_workingday['cnt'])
st.write(f"Korelasi antara suhu (temp) dan jumlah penyewaan (cnt) pada hari kerja: {correlation_workingday}")

correlation_holiday = df_holiday['temp'].corr(df_holiday['cnt'])
st.write(f"Korelasi antara suhu (temp) dan jumlah penyewaan (cnt) pada hari libur: {correlation_holiday}")

# Scatter plots
for data, title in zip([df_workingday, df_holiday], ['Hari Kerja', 'Hari Libur']):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=data['temp'], y=data['cnt'])
    plt.title(f'Hubungan antara Suhu (temp) dan Jumlah Penyewaan (cnt) pada {title}')
    plt.xlabel('Suhu (temp)')
    plt.ylabel('Jumlah Penyewaan (cnt)')
    st.pyplot(plt)

# Rata-rata suhu dan jumlah sewa
summary_df = df_day.groupby('holiday').agg({'temp': 'mean', 'cnt': 'mean'}).reset_index()
summary_df['holiday'] = summary_df['holiday'].map({0: 'Hari Kerja', 1: 'Hari Libur'})

# Menampilkan DataFrame summary
st.write(summary_df)

# Bar plot
fig, ax1 = plt.subplots(figsize=(10, 6))
bar_width = 0.35
index = np.arange(2)

# Plot untuk 'cnt' (Jumlah Penyewaan)
bars1 = ax1.bar(index - bar_width / 2, summary_df['cnt'], bar_width, color='blue', label='Jumlah Penyewaan', alpha=0.6)
# Membuat sumbu y kedua untuk 'temp' (Suhu)
ax2 = ax1.twinx()
bars2 = ax2.bar(index + bar_width / 2, summary_df['temp'], bar_width, color='orange', label='Suhu', alpha=0.9)

# Menambahkan label, judul, dan legend
plt.title('Rata-rata Suhu dan Jumlah Penyewaan pada Hari Kerja dan Hari Libur', fontsize=16)
ax1.set_xlabel('Tipe Hari', fontsize=14)
ax1.set_ylabel('Jumlah Penyewaan', fontsize=14)
ax2.set_ylabel('Suhu (temp)', fontsize=14)

ax1.set_xticks(index)
ax1.set_xticklabels(['Hari Kerja', 'Hari Libur'])
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Tampilkan plot di Streamlit
st.pyplot(fig)

# Jawaban untuk pertanyaan
st.subheader('Visualization & Explanatory Analysis')
st.write("Dari visualisasi di atas, kita dapat menarik beberapa kesimpulan:")
st.write("- Rata-rata suhu pada hari kerja dan hari libur dapat berbeda secara signifikan.")
st.write("- Rata-rata jumlah sewa pada hari kerja mungkin lebih tinggi dibandingkan dengan hari libur atau sebaliknya, menunjukkan pengaruh suhu terhadap perilaku penyewa.")

