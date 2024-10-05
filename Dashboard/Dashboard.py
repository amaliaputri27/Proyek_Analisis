import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Judul Aplikasi
st.title("Bike sharing dataset")
st.write("Nama: Amalia Putri")
st.write("Email: m384b4kx0446@bangkit.academy")
st.write("ID Dicoding: aleailearn")

# Exploratory Data Analysis (EDA)
st.title("Exploratory Data Analysis (EDA)")

# Shuffle data DAY (mengacak urutan baris)
df_day_shuffled = df_day.sample(frac=1)

# Descriptive statistics untuk dataset DAY
st.subheader("Statistik Deskriptif Dataset DAY")
day_stats = df_day.describe(include='all')
st.write(day_stats)

# Nilai unik untuk kolom 'dteday'
st.subheader("Nilai Unik pada Kolom 'dteday'")
unique_dates = df_day['dteday'].unique()
st.write(unique_dates)

# Nilai unik untuk setiap kolom dalam dataset DAY
st.subheader("Nilai Unik di Semua Kolom Dataset DAY")
unique_values = df_day.apply(pd.Series.unique)
st.write(unique_values)

# Menggabungkan data berdasarkan kolom 'dteday'
df_merged = pd.merge(df_day, df_hour, on='dteday')

# Menampilkan beberapa baris pertama data yang digabungkan
st.subheader("Data Gabungan DAY dan HOUR")
st.write(df_merged.head())

