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

# Memuat Data
data = pd.read_csv('Data/day.csv')

# Memuat kedua data CSV
df_day = pd.read_csv('Data/day.csv')
df_hour = pd.read_csv('Data/hour.csv')

# Menampilkan info singkat tentang dataset
st.write("Data Day")
st.write(df_day.head())

st.write("Data Hour")
st.write(df_hour.head())



# Mengonversi kolom 'dteday' ke format datetime
df_day['dteday'] = pd.to_datetime(df_day['dteday'])

# Memeriksa tipe data setelah konversi
print(df_day.dtypes)

