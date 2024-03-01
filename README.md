# Project Analisis Kualitas Udara: Stasiun Gucheng

## Project Overview
Project ini, yang diajukan untuk kursus "Belajar Analisis Data dengan Python" dari Dicoding, berfokus pada analisis data kualitas udara, khususnya tingkat PM10, dari stasiun Gucheng. Tujuannya adalah untuk mengungkap pola, variasi musiman, dan dampak kondisi cuaca yang berbeda terhadap kualitas udara.

## Course Submission
Analisis ini digunakan sebagai submission kursus untuk "Belajar Analisis Data dengan Python" yang ditawarkan oleh Dicoding. Analisis ini menunjukkan penerapan teknik analisis data dan keterampilan visualisasi yang dipelajari dalam kursus

## Table of Contents
- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Installasi](#installasi)
- [Penggunaan](#penggunaan)
- [Data Sources](#data-sources)

## Project Overview
Project ini, yang diajukan untuk kursus "Belajar Analisis Data dengan Python" dari Dicoding, berfokus pada analisis data kualitas udara, khususnya tingkat PM10, dari stasiun Gucheng. Tujuannya adalah untuk mengungkap pola, variasi musiman, dan dampak kondisi cuaca yang berbeda terhadap kualitas udara.

## Project Structure
- `dashboard/`: Direktori ini berisi dashboard.py yang digunakan untuk membuat dashboard hasil analisis data.
- `data/`: Direktori yang berisi file data CSV mentah.
- `notebook.ipynb`: File ini digunakan untuk melakukan analisis data.
- `README.md`: Ini adalah file dokumentasi.

## Installasi
1. Membuat dan Mengaktifkan Python Environment::
```
conda create --name airquality-ds python=3.9
conda activate airquality-ds
```
2. Install Paket yang Diperlukan
```
pip install pandas numpy scipy matplotlib seaborn streamlit statsmodels
```
3. Navigasikan ke Direktori Project di mana dashboard.py berada

4. Menjalankan Streamlit App:
```
streamlit run dashboard.py
```

## Penggunaan
1. **Data Wrangling**: Script data wrangling tersedia di file `notebook.ipynb` untuk menyiapkan dan membersihkan data.

2. **Exploratory Data Analysis (EDA)**: Jelajahi dan analisis data menggunakan script Python yang disediakan. Wawasan EDA dapat memandu pemahaman Anda tentang pola musim yg mempengaruhi kualitas udara.

3. **Visualization**: Jalankan Streamlit dashboard untuk eksplorasi data interaktif:

```
streamlit run dashboard.py
```
Akses dashboard di browser web Anda pada `http://localhost:8501`.

## Data Sources
Dataset yang digunakan dalam proyek ini mencakup pengukuran kualitas udara dari stasiun Gucheng, dengan fokus pada tingkat PM10 dan data lingkungan terkait lainnya

## Live Dashboard
Link : https://herdiansyah.streamlit.app/
