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
