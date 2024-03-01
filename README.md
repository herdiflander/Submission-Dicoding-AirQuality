# Project Analisis Kualitas Udara: Stasiun Gucheng

## Live Dashboard


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
1. Clone repositori ini ke local machine Anda:
```
git clone https://github.com/herdiansyah_3ia17/Submission-Dicoding-AirQuality.git
```
2. Buka direktori project
```
cd Submission-Dicoding-AirQuality
```
3. Instal paket Python yang diperlukan dengan menjalankan:
```
pip install -r requirements.txt
```

## Penggunaan
1. **Data Wrangling**: Script data wrangling tersedia di file `notebook.ipynb` untuk menyiapkan dan membersihkan data.

2. **Exploratory Data Analysis (EDA)**: Jelajahi dan analisis data menggunakan script Python yang disediakan. Wawasan EDA dapat memandu pemahaman Anda tentang pola musim yg mempengaruhi kualitas udara.

3. **Visualization**: Jalankan Streamlit dashboard untuk eksplorasi data interaktif:

```
cd Submission-Dicoding-AirQuality/dashboard
streamlit run dashboard.py
```
Akses dashboard di browser web Anda pada `http://localhost:8501`.

## Data Sources
Dataset yang digunakan dalam proyek ini mencakup pengukuran kualitas udara dari stasiun Gucheng, dengan fokus pada tingkat PM10 dan data lingkungan terkait lainnya
