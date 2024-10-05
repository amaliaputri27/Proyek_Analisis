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
st.write("Gathering Data")
data = pd.read_csv('Bangkit7/day.csv')

# Memuat data dari kedua CSV
df_day = pd.read_csv('data/day.csv')
df_hour = pd.read_csv('data/hour.csv')

# Menggabungkan data berdasarkan kolom 'dteday'
df_merged = pd.merge(df_day, df_hour, on='dteday')

# Menampilkan beberapa baris pertama data yang digabungkan
print(df_merged.head())

st.write("Assesing Data")
# Menilai data df_day

df_day.info()

# Mengonversi kolom 'dteday' ke format datetime
df_day['dteday'] = pd.to_datetime(df_day['dteday'])

# Memeriksa tipe data setelah konversi
print(df_day.dtypes)

