import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import urllib
from statsmodels.tsa.seasonal import seasonal_decompose
import numpy as np

# Judul Halaman
st.set_page_config(page_title="Air Quality from Gucheng Analysis by Herdiansyah")


# Load dataset
data = pd.read_csv('https://github.com/herdiflander/Submission-Dicoding-AirQuality/blob/main/data/PRSA_Data_Gucheng_20130301-20170228.csv')

# Judul dashboard
st.title('Air Quality Analysis Dashboard: Stasiun Gucheng')



# Deskripsi
st.write('Dasboard ini menyediakan cara interaktif untuk menjelajahi data kualitas udara, khususnya berfokus pada tingkat PM10 dan hubungannya dengan berbagai kondisi cuaca.')


# About me
st.markdown("""
### About Me
- **Name**: Herdiansyah Suhendar
- **Email Address**: herdiflander@gmail.com
- **Dicoding ID**: [herdiansyah_3ia17](https://www.dicoding.com/users/herdiansyah_3ia17/)

### Project Overview
Dashboard ini menyajikan analisis data kualitas udara, khususnya yang berfokus pada tingkat PM10 dari stasiun Gucheng. Project ini bertujuan untuk mengungkap pola, variasi musiman, dan dampak kondisi cuaca yang berbeda terhadap kualitas udara. Wawasan dari analisis ini dapat bermanfaat untuk studi lingkungan dan pemantauan kesehatan masyarakat.
""")

# Menambahkan sidebar untuk input interaktif
st.sidebar.header('Fitur Input User')

# Memungkinkan users memilih tahun dan bulan untuk melihat data
selected_year = st.sidebar.selectbox('Pilih Tahun', list(data['tahun'].unique()))
selected_month = st.sidebar.selectbox('Pilih Bulan', list(data['bulan'].unique()))

# Filter data berdasarkan tahun dan bulan yang dipilih
data_filtered = data[(data['tahun'] == selected_year) & (data['bulan'] == selected_month)].copy()

# Menampilkan statistik data
st.subheader('Tinjauan Data untuk Periode yang Dipilih')
st.write(data_filtered.describe())

# Line chart untuk tingkat PM10 selama bulan yang dipilih
st.subheader('Tingkat PM10 Harian')
fig, ax = plt.subplots()
ax.plot(data_filtered['hari'], data_filtered['PM10'])
plt.xlabel('Hari dalam Sebulan')
plt.ylabel('Konsentrasi PM10')
st.pyplot(fig)

# Analisis Pola Musiman
st.subheader('Analisis Pola Musiman')
seasonal_trends = data.groupby('bulan')['PM10'].mean()
fig, ax = plt.subplots()
seasonal_trends.plot(kind='bar', color='pink', ax=ax)
plt.title('Rata-rata Tingkat PM10 Bulanan')
plt.xlabel('Bulan')
plt.ylabel('Rata-rata PM10')
st.pyplot(fig)

# Rata-rata Heatmap per jam
st.subheader('Rata-rata PM10 per jam')
try:
    # Memastikan tipe data yang benar dan menangani nilai yang hilang
    data['jam'] = data['jam'].astype(int)
    data['PM10'] = pd.to_numeric(data['PM10'], errors='coerce')
    data['PM10'].ffill(inplace=True)

    # Menghitung rata-rata per jam
    hourly_avg = data.groupby('jam')['PM10'].mean()

    # Plotting
    fig, ax = plt.subplots()
    sns.heatmap([hourly_avg.values], ax=ax, cmap='coolwarm')
    plt.title('Rata-rata PM10 per jam')
    st.pyplot(fig)
except Exception as e:
    st.error(f"Error dalam memplotkan rata-rata per jam: {e}")

# Membandingkan Curah Hujan dengan Kualitas Udara
st.subheader('Membandingkan Curah Hujan dengan tingkat PM10')
fig, ax = plt.subplots()
sns.scatterplot(x='HUJAN', y='PM10', data=data_filtered, ax=ax)
plt.title('Perbandingan Curah Hujan dengan tingkat PM10')
st.pyplot(fig)

# Korelasi Heatmap - Interaktif
st.subheader('Korelasi Heatmap Interaktif')
selected_columns = st.multiselect('Pilih Kolom untuk Korelasi', data.columns, default=['PM10', 'NO2', 'TEMP', 'PRES', 'DEWP'])
corr = data[selected_columns].corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, ax=ax)
st.pyplot(fig)


# Kesimpulan
st.subheader('Kesimpulan')
st.write("""
- Dashboard ini menyediakan analisis data kualitas udara yang mendalam dan interaktif.
- Berbagai visualisasi yang menawarkan wawasan tentang tingkat PM10, distribusinya, dan faktor-faktor yang mempengaruhinya.
- Pola musiman dan dampak kondisi cuaca dan polutan yang berbeda terhadap kualitas udara digambarkan dengan jelas.
- Pengguna dapat menjelajahi data secara dinamis untuk mendapatkan pemahaman yang lebih dalam tentang pola kualitas udara.
""")
