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

# Exploratory Data Analysis (EDA)
st.title("Exploratory Data Analysis (EDA)")

# Sample data for demonstration
df_day = pd.read_csv('Data/day.csv')

# Random sampling of all rows
df_day_sample = df_day.sample(frac=1)

# Descriptive statistics for DAY
st.subheader('Descriptive Statistics for day Data')
st.write("Statistika deskriptif dilakukan untuk memahami karakteristik data, termasuk ukuran pusat, penyebaran, dan pola.")
day_stats = df_day_sample.describe(include='all')
st.write(day_stats)

# Plot histograms for 'temp', 'atemp', 'hum', 'windspeed', and 'cnt' columns
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

# Memastikan hanya kolom numerik yang dipilih untuk korelasi
df_day_numeric = df_day.select_dtypes(include=[np.number])

# Korelasi untuk DAY
st.subheader('Analisis Korelasi')
st.write("Secara keseluruhan, analisis korelasi ini memberikan pemahaman mendalam tentang faktor-faktor yang mempengaruhi jumlah penyewaan sepeda, serta bagaimana memanfaatkan wawasan ini untuk strategi bisnis yang lebih baik.")
day_corr = df_day_numeric.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(day_corr, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Heatmap for DAY Data')
st.pyplot(plt)

# Menghitung korelasi Pearson antara temp dan cnt untuk df_day
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

# Menghitung korelasi Pearson antara suhu (temp) dan jumlah penyewaan (cnt) pada hari kerja
correlation_workingday = df_workingday['temp'].corr(df_workingday['cnt'])
st.write(f"Korelasi antara suhu (temp) dan jumlah penyewaan (cnt) pada hari kerja: {correlation_workingday}")

# Menghitung korelasi Pearson antara suhu (temp) dan jumlah penyewaan (cnt) pada hari libur
correlation_holiday = df_holiday['temp'].corr(df_holiday['cnt'])
st.write(f"Korelasi antara suhu (temp) dan jumlah penyewaan (cnt) pada hari libur: {correlation_holiday}")

# Membuat scatter plot untuk hari kerja
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df_workingday['temp'], y=df_workingday['cnt'])
plt.title('Hubungan antara Suhu (temp) dan Jumlah Penyewaan (cnt) pada Hari Kerja')
plt.xlabel('Suhu (temp)')
plt.ylabel('Jumlah Penyewaan (cnt)')
st.pyplot(plt)

# Membuat scatter plot untuk hari libur
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df_holiday['temp'], y=df_holiday['cnt'])
plt.title('Hubungan antara Suhu (temp) dan Jumlah Penyewaan (cnt) pada Hari Libur')
plt.xlabel('Suhu (temp)')
plt.ylabel('Jumlah Penyewaan (cnt)')
st.pyplot(plt)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the dataset
df = pd.read_csv("Data/day.csv")  # Make sure to specify the correct path to your CSV file

# Menghitung rata-rata suhu dan jumlah sewa
summary_df = df.groupby('holiday').agg({'temp': 'mean', 'cnt': 'mean'}).reset_index()
summary_df['holiday'] = summary_df['holiday'].map({0: 'Hari Kerja', 1: 'Hari Libur'})

# Menampilkan DataFrame summary
st.write(summary_df)

# Bar plot untuk hari kerja dan hari libur
bar_width = 0.35  # Lebar bar
index = np.arange(2)  # Indeks posisi untuk kategori

fig, ax1 = plt.subplots(figsize=(10, 6))

# Membagi data menjadi hari kerja dan hari libur
df_workingday = df[df['holiday'] == 0]
df_holiday = df[df['holiday'] == 1]

# Menghitung rata-rata suhu dan jumlah penyewaan per kategori
mean_workingday = df_workingday[['temp', 'cnt']].mean()
mean_holiday = df_holiday[['temp', 'cnt']].mean()

# Plot untuk 'cnt' (Jumlah Penyewaan)
bars1 = ax1.bar(index[0] - bar_width / 2, mean_holiday['cnt'], bar_width, color='blue', label='Jumlah Penyewaan (Hari Libur)', alpha=0.6)
bars2 = ax1.bar(index[1] - bar_width / 2, mean_workingday['cnt'], bar_width, color='green', label='Jumlah Penyewaan (Hari Kerja)', alpha=0.6)

# Membuat sumbu y kedua untuk 'temp' (Suhu)
ax2 = ax1.twinx()
ax2.bar(index[0] + bar_width / 2, mean_holiday['temp'], bar_width, color='orange', label='Suhu (Hari Libur)', alpha=0.9)
ax2.bar(index[1] + bar_width / 2, mean_workingday['temp'], bar_width, color='red', label='Suhu (Hari Kerja)', alpha=0.9)

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
for bar in bars1 + bars2:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom')

# Tampilkan plot di Streamlit
st.subheader('Explore mean() method df_day & df_hour')
st.write("Dengan melakukan analisis ini, pengelola layanan penyewaan sepeda dapat merancang strategi yang lebih baik berdasarkan data. Misalnya, jika jumlah penyewaan meningkat pada hari kerja saat suhu naik, mereka mungkin ingin melakukan promosi khusus pada hari-hari tersebut untuk menarik lebih banyak pelanggan.")
st.pyplot(fig)

# Menjawab pertanyaan 1
st.subheader('Visualization & Explanatory Analysis')
st.write("Pertanyaan 1: Bagaimana pengaruh suhu (temp) terhadap jumlah total sewa (cnt) pada hari kerja dibandingkan dengan hari libur?")

# Pastikan kolom 'holiday' ada
if 'holiday' not in df.columns:
    st.error("Kolom 'holiday' tidak ditemukan dalam DataFrame.")
else:
    # Set style
    sns.set(style="whitegrid")


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the dataset
df = pd.read_csv("Data/day.csv")  # Make sure to specify the correct path to your CSV file
df = pd.read_csv("Data/hour.csv") 

# Check if the 'holiday' column exists in the DataFrame
if 'holiday' not in df.columns:
    st.error("Kolom 'holiday' tidak ditemukan dalam DataFrame.")
else:
    # Memisahkan data berdasarkan hari kerja dan hari libur
    workdays_df = df[df['holiday'] == 0]
    holidays_df = df[df['holiday'] == 1]

    # Menghitung rata-rata suhu dan jumlah sewa
    summary_df = df.groupby('holiday').agg({'temp': 'mean', 'cnt': 'mean'}).reset_index()
    summary_df['holiday'] = summary_df['holiday'].map({0: 'Hari Kerja', 1: 'Hari Libur'})

    # Menampilkan DataFrame summary
    st.write(summary_df)

    plt.figure(figsize=(12, 6))

    # Subplot untuk Suhu
    plt.subplot(1, 2, 1)
    sns.barplot(x='holiday', y='temp', data=summary_df, palette='coolwarm')
    plt.title('Rata-Rata Suhu pada Hari Kerja vs Hari Libur')
    plt.ylabel('Rata-Rata Suhu (°C)')
    plt.xlabel('Tipe Hari')

    # Subplot untuk Jumlah Sewa
    plt.subplot(1, 2, 2)
    sns.barplot(x='holiday', y='cnt', data=summary_df, palette='coolwarm')
    plt.title('Rata-Rata Jumlah Sewa pada Hari Kerja vs Hari Libur')
    plt.ylabel('Rata-Rata Jumlah Sewa')
    plt.xlabel('Tipe Hari')

    plt.tight_layout()

    # Display the plots in Streamlit
    st.pyplot(plt)

    # Jawaban
    st.write("Dari visualisasi di atas, kita dapat menarik beberapa kesimpulan:")
    st.write("- Rata-Rata Suhu: Rata-rata suhu pada hari kerja dan hari libur dapat berbeda secara signifikan. Perhatikan apakah hari libur memiliki suhu yang lebih tinggi atau lebih rendah.")
    st.write("- Rata-Rata Jumlah Sewa: Rata-rata jumlah sewa pada hari kerja mungkin lebih tinggi dibandingkan dengan hari libur atau sebaliknya. Ini bisa mengindikasikan pengaruh suhu terhadap perilaku penyewa, di mana suhu yang lebih tinggi mungkin meningkatkan jumlah sewa, baik pada hari kerja maupun hari libur.")


