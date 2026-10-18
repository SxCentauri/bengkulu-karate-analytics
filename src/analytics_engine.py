import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

print("=== Bengkulu Karate Competition Analytics Engine ===")
print("Developed by: Akhmat Qavidhufahmi\n")

raw_data = {
    'kategori': ['Kumite -55kg', 'Kumite -55kg', 'Kumite -55kg', 'Kata Perorangan', 'Kata Perorangan'],
    'tahun': [2023, 2024, 2025, 2023, 2024],
    'jumlah_peserta': [40, 45, 120, 20, 22] 
}
df = pd.DataFrame(raw_data)

print("Data awal (dengan anomali):")
print(df)
print("\n")

df.loc[(df['kategori'] == 'Kumite -55kg') & (df['tahun'] == 2025), 'jumlah_peserta'] = 50

print("Data setelah persiapan (campur tangan manusia):")
print(df)
print("\n")

kumite_data = df[df['kategori'] == 'Kumite -55kg']
X = kumite_data[['tahun']]
y = kumite_data['jumlah_peserta']

model = LinearRegression()
model.fit(X, y)

prediksi_2026 = int(model.predict([[2026]])[0])
print(f"Prediksi jumlah peserta Kumite -55kg tahun 2026: {prediksi_2026} orang\n")

kapasitas_matras = 25 

if prediksi_2026 > kapasitas_matras:
    matras_dibutuhkan = int(np.ceil(prediksi_2026 / kapasitas_matras))
    print(f"-> REKOMENDASI SISTEM: Alokasikan {matras_dibutuhkan} matras dan {matras_dibutuhkan} tim wasit untuk kategori Kumite -55kg guna mencegah keterlambatan jadwal.")
else:
    print("-> REKOMENDASI SISTEM: Alokasi 1 matras sudah cukup.")