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

# Sample data for demonstration
df_day = pd.read_csv('Data/day.csv')

# Random sampling of all rows
df_day_sample = df_day.sample(frac=1)

# Descriptive statistics for DAY
st.subheader('Descriptive Statistics for day data')
day_stats = df_day_sample.describe(include='all')
st.write(day_stats)

# Exploratory Data Analysis (EDA)
st.title("Exploratory Data Analysis (EDA)")

# Plot histograms for 'temp', 'atemp', 'hum', 'windspeed', and 'cnt' columns
st.subheader('Histograms of Selected Features')
fig, ax = plt.subplots(figsize=(10, 8))
df_day_sample[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].hist(bins=30, ax=ax)
plt.suptitle('Histogram of DAY Data')
st.pyplot(fig)

# Plot histogram with seaborn for 'cnt' column
st.subheader('Distribusi Kolom cnt')
fig2, ax2 = plt.subplots(figsize=(8, 6))
sns.histplot(df_day_sample['cnt'], kde=True, ax=ax2)
ax2.set_title('Distribusi Kolom cnt')
ax2.set_xlabel('Jumlah Penyewaan (cnt)')
ax2.set_ylabel('Frekuensi')
st.pyplot(fig2)
