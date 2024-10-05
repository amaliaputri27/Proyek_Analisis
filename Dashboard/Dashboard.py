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

