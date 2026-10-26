#write your code here
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance.csv')

print('Menampilkan 5 data pertama')
print(df.head())

print('Menampilkan 5 data terakhir')
print(df.tail())

print('Menampilkan semua informasi')
print(df.info())

print('Menjelaskan data numerik/angka secara detail')
print(df.describe())

df['math score'].plot(kind='hist', bins=7, color='red', edgecolor='beige')

plt.title('Distribusi Jumlah Berdasarkan Math Score')
plt.xlabel('Math Score')
plt.ylabel('Jumlah')
plt.grid(axis='y', linestyle='--', alpha=0.9)

plt.tight_layout()
plt.savefig('math_score_distribusi.png')
plt.show()
plt.close()

# race_counts = df['gender'].value_counts().sort_index()
# fig, ax = plt.subplots(figsize=(8, 5))
# race_counts.plot(kind='pie', color='skyblue', ax=ax)
# ax.set_title('Number of Students by Race/EthnicityGe Group', fontsize=14, fontweight='bold')
# ax.set_xlabel('Race/Ethnicity Group', fontsize=12)
# ax.set_ylabel('Student Count', fontsize=12)
# ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
# ax.grid(axis='y', linestyle='--', alpha=0.7)
# plt.tight_layout()
# plt.savefig('student_counts_by_race.png')
# plt.close()
# plt.figure(figsize=(8, 5))
