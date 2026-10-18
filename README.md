<div align="center">

# 🥋 Bengkulu Karate Analytics

### Platform Analitik Preskriptif untuk Tata Kelola **Bengkulu Karate Competition**

*Dari data pendaftar → prediksi lonjakan → rekomendasi matras & wasit otomatis.*

<br>

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
<br>
![Prisma](https://img.shields.io/badge/Prisma-5.x-2D3748?style=for-the-badge&logo=prisma&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)

<br>

[📖 Studi Kasus](#-studi-kasus) •
[🔺 Piramida Analitik](#-penerapan-piramida-analitik) •
[🏗️ Arsitektur](#️-arsitektur--struktur-folder) •
[🚀 Cara Menjalankan](#-cara-menjalankan) •
[📊 Contoh Output](#-contoh-output) •

</div>

---

## 📖 Studi Kasus

> **Platform Preskriptif untuk Tata Kelola Bengkulu Karate Competition**

### ❗ Konteks Masalah

Setiap tahun, panitia **Bengkulu Karate Competition** kesulitan mengalokasikan **jumlah wasit** dan **durasi waktu pada matras (tatami)** tertentu. Penyebabnya adalah **ketidakpastian jumlah pendaftar** di setiap kelas, misalnya **Kumite -55kg Putra** vs **Kata Perorangan**.

Akibatnya:

| Gejala | Dampak |
|---|---|
| 🔴 Kelas tertentu melebihi kapasitas matras | Antrean menumpuk, jadwal molor |
| 🔴 Jumlah wasit tidak sesuai kebutuhan | Beban kerja timpang, kualitas penilaian turun |
| 🔴 Alokasi dilakukan berdasarkan perkiraan | Keputusan reaktif, bukan berbasis data |

### 💡 Solusi

Sistem yang tidak hanya **menjelaskan apa yang terjadi**, tetapi juga **memprediksi apa yang akan terjadi** dan **merekomendasikan apa yang harus dilakukan**, yaitu menambah matras atau wasit sebelum kelas membeludak.

---

## 🔺 Penerapan Piramida Analitik

Project ini menerapkan empat level **Piramida Analitik** (Sesi 1), dari pertanyaan *"apa yang terjadi?"* hingga *"apa yang harus kita lakukan?"*.

```mermaid
flowchart BT
    A["📊 <b>DESCRIPTIVE</b><br/>Apa yang terjadi?"]
    B["🔍 <b>DIAGNOSTIC</b><br/>Mengapa itu terjadi?"]
    C["🔮 <b>PREDICTIVE</b><br/>Apa yang akan terjadi?"]
    D["🎯 <b>PRESCRIPTIVE</b><br/>Apa yang harus dilakukan?"]

    A --> B --> C --> D

    style A fill:#dbeafe,stroke:#3b82f6,color:#1e3a8a
    style B fill:#e0e7ff,stroke:#6366f1,color:#312e81
    style C fill:#fef3c7,stroke:#f59e0b,color:#78350f
    style D fill:#dcfce7,stroke:#22c55e,color:#14532d
```

| # | Level | Pertanyaan | Penerapan pada Kasus Karate | Implementasi di Project |
|:-:|---|---|---|---|
| 1 | 📊 **Descriptive** | Apa yang terjadi? | Menampilkan jumlah pendaftar tahun lalu per kategori | Tabel `DataFrame` histori pendaftar |
| 2 | 🔍 **Diagnostic** | Mengapa itu terjadi? | Menemukan bahwa antrean menumpuk karena kelas tertentu melebihi kapasitas matras | Deteksi anomali data + kolom `is_anomalous` di skema |
| 3 | 🔮 **Predictive** | Apa yang akan terjadi? | Memprediksi kelas mana yang akan melonjak tahun ini | `LinearRegression` (scikit-learn) |
| 4 | 🎯 **Prescriptive** | Apa yang harus dilakukan? | Merekomendasikan penambahan matras/wasit untuk kelas yang diprediksi membeludak | Aturan kapasitas matras → rekomendasi otomatis |

---

## 🏗️ Arsitektur & Struktur Folder

Karena project ini memadukan ekosistem **full-stack (Prisma + MySQL)** dengan **AI/Data (Python)**, kedua sisi dipisah agar tidak saling bertabrakan:

```text
Bengkulu_Karate_Analytics/
├── 📂 prisma/
│   └── 📄 schema.prisma        # Skema database MySQL (ekosistem Node.js/Prisma)
├── 📂 src/
│   └── 🐍 analytics_engine.py  # Data preparation + prediksi + rekomendasi (Python)
├── 📄 package.json             # Dependensi Node.js (Prisma)
├── 📄 requirements.txt         # Dependensi Python (Pandas, scikit-learn, NumPy)
└── 📄 README.md
```

### Alur Sistem

```mermaid
flowchart LR
    DB[("🗄️ MySQL<br/>via Prisma")] -->|histori pendaftar| DP["🧹 Data Preparation<br/>(Pandas)"]
    DP -->|data bersih| ML["🤖 Linear Regression<br/>(scikit-learn)"]
    ML -->|prediksi pendaftar| RX["🎯 Aturan Kapasitas<br/>Matras"]
    RX --> OUT["✅ Rekomendasi<br/>Matras & Wasit"]

    style DB fill:#e0f2fe,stroke:#0284c7
    style DP fill:#fef9c3,stroke:#ca8a04
    style ML fill:#ffedd5,stroke:#ea580c
    style RX fill:#fce7f3,stroke:#db2777
    style OUT fill:#dcfce7,stroke:#16a34a
```

---

## 🗄️ Skema Database (Prisma)

Dua model dengan relasi *one-to-many*: satu kelas karate memiliki banyak riwayat pendaftaran per tahun.

```mermaid
erDiagram
    KarateClass ||--o{ RegistrationHistory : "memiliki"
    KarateClass {
        Int id PK
        String category_name "cth: Kumite -55kg Junior Putra"
    }
    RegistrationHistory {
        Int id PK
        Int classId FK
        Int year
        Int participant_qty "jumlah pendaftar aktual"
        Boolean is_anomalous "default: false"
    }
```

<details>
<summary><b>📄 Lihat <code>schema.prisma</code> lengkap</b></summary>

```prisma
datasource db {
  provider = "mysql"
  url      = env("DATABASE_URL")
}

generator client {
  provider = "prisma-client-js"
}

model KarateClass {
  id              Int                   @id @default(autoincrement())
  category_name   String                // Contoh: "Kumite -55kg Junior Putra"
  historical_data RegistrationHistory[]
}

model RegistrationHistory {
  id              Int         @id @default(autoincrement())
  classId         Int
  year            Int
  participant_qty Int         // Jumlah pendaftar aktual
  is_anomalous    Boolean     @default(false)
  karateClass     KarateClass @relation(fields: [classId], references: [id])
}
```

</details>

---

## ⚙️ Cara Kerja `analytics_engine.py`

### 1️⃣ Data Preparation: *tahap yang memakan 60–70% waktu*

Data mentah sering mengandung anomali. Pada data contoh, jumlah peserta **Kumite -55kg tahun 2025 tercatat 120**, padahal angka sebenarnya **50**. Tanpa pembersihan, model akan memprediksi lonjakan palsu.

```python
df.loc[(df['kategori'] == 'Kumite -55kg') & (df['tahun'] == 2025), 'jumlah_peserta'] = 50
```

| Kategori | 2023 | 2024 | 2025 (mentah) | 2025 (bersih) |
|---|:-:|:-:|:-:|:-:|
| Kumite -55kg | 40 | 45 | ~~120~~ ⚠️ | **50** ✅ |
| Kata Perorangan | 20 | 22 | n/a | n/a |

> 🧠 **Human-in-the-loop:** koreksi dilakukan oleh manusia yang memahami konteks lapangan. Itulah mengapa tahap ini tidak bisa sepenuhnya diotomatisasi.

### 2️⃣ Predictive Analytics

Model **Linear Regression** dilatih pada tren historis `tahun → jumlah_peserta`, lalu dipakai memprediksi tahun 2026.

```python
model = LinearRegression()
model.fit(X, y)
prediksi_2026 = int(model.predict([[2026]])[0])
```

### 3️⃣ Prescriptive Analytics

Hasil prediksi dibandingkan dengan **kapasitas satu matras (25 peserta)**. Bila melebihi, sistem menghitung jumlah matras dan tim wasit yang dibutuhkan:

$$
\text{matras dibutuhkan} = \left\lceil \frac{\text{prediksi peserta}}{\text{kapasitas matras}} \right\rceil
$$

```python
kapasitas_matras = 25
matras_dibutuhkan = int(np.ceil(prediksi_2026 / kapasitas_matras))
```

---

## 🚀 Cara Menjalankan

### Prasyarat

- 🐍 **Python** 3.9 atau lebih baru
- 🟢 **Node.js** 18 atau lebih baru
- 🐬 **MySQL** (hanya diperlukan untuk menjalankan migrasi database)

### 1. Clone Repository

```bash
git clone https://github.com/<username>/Bengkulu_Karate_Analytics.git
cd Bengkulu_Karate_Analytics
```

### 2. Jalankan Skrip Python (AI & Analytics)

```bash
pip install -r requirements.txt
python src/analytics_engine.py
```

### 3. Siapkan Database Prisma (Backend)

```bash
npm install
npx prisma generate
```

Buat file `.env` di root project, lalu isi dengan koneksi MySQL Anda:

```env
DATABASE_URL="mysql://USER:PASSWORD@localhost:3306/bengkulu_karate"
```

Setelah `.env` siap, jalankan migrasi untuk membuat tabel:

```bash
npx prisma migrate dev --name init
```

> [!NOTE]
> File `.env` berisi kredensial. Pastikan sudah masuk ke `.gitignore` agar tidak ter-upload ke GitHub.

---

## 📊 Contoh Output

```text
=== Bengkulu Karate Competition Analytics Engine ===
Developed by: Akhmat Qavidhufahmi

Data awal (dengan anomali):
          kategori  tahun  jumlah_peserta
0     Kumite -55kg   2023              40
1     Kumite -55kg   2024              45
2     Kumite -55kg   2025             120
3  Kata Perorangan   2023              20
4  Kata Perorangan   2024              22

Data setelah persiapan (campur tangan manusia):
          kategori  tahun  jumlah_peserta
0     Kumite -55kg   2023              40
1     Kumite -55kg   2024              45
2     Kumite -55kg   2025              50
3  Kata Perorangan   2023              20
4  Kata Perorangan   2024              22

Prediksi jumlah peserta Kumite -55kg tahun 2026: 55 orang

-> REKOMENDASI SISTEM: Alokasikan 3 matras dan 3 tim wasit untuk kategori Kumite -55kg
   guna mencegah keterlambatan jadwal.
```

### 🎯 Hasil Akhir

<div align="center">

| Kategori | Prediksi 2026 | Kapasitas / Matras | Rekomendasi |
|:-:|:-:|:-:|:-:|
| **Kumite -55kg** | **55 peserta** | 25 | 🟥 **3 matras + 3 tim wasit** |

</div>

---

## ⚠️ Catatan & Batasan

Project ini adalah **prototipe pembelajaran**. Beberapa hal yang perlu diketahui:

- 📉 **Data sangat sedikit.** Model dilatih dari 3 titik data (2023–2025), sehingga prediksi bersifat indikatif, belum siap untuk keputusan produksi.
- 🥋 **Baru satu kategori yang diprediksi.** Saat ini hanya *Kumite -55kg*; *Kata Perorangan* baru ada di data dan belum diprediksi.
- ✋ **Pembersihan anomali masih manual** (nilai 120 → 50 ditulis langsung di kode). Skema Prisma sudah menyediakan kolom `is_anomalous` untuk otomatisasi ke depan.
- 🔌 **Python belum terhubung ke MySQL.** Data masih berupa dictionary di dalam skrip; skema Prisma disiapkan sebagai fondasi integrasi.

---

## 👨‍💻 Developer

<div align="center">

**Akhmat Qavidhufahmi**

*Dibuat untuk mendukung tata kelola Bengkulu Karate Competition yang lebih efisien dan berbasis data* 🥋

⭐ Jika project ini bermanfaat, jangan lupa beri **star** pada repository ini!

</div>
