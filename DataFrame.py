#Gerekli kütüphanelerin eklenmesi
import pandas as pd
from tabulate import tabulate


#Data'nın alınması
df = pd.read_csv('D:\Workspace\PythonProjects\isYeriOdevi\StudentsPerformance.csv')

#Verinin doğruluğu ve netliği için grupların doğru etnik kökenlere yerleştirilmesi
ethnicity_mapping = {
    'group A': 'White - British',
    'group B': 'White - Irish',
    'group C': 'White - Any other White background',
    'group D': 'Mixed - White and Black Caribbean',
    'group E': 'Mixed - White and Black African',
    'group F': 'Mixed - White and Asian',
    'group G': 'Mixed - Any other mixed background'
}

#Tablonun bütünlüğü için ayarlar, değiştirilmiş etnik kökenlerin yerine koyulması ve ortalama hesabı
df['race/ethnicity'] = df['race/ethnicity'].map(ethnicity_mapping)

score_columns = ['math score', 'reading score', 'writing score']

df['average score'] = df[score_columns].mean(axis=1)

pd.set_option('display.max_rows', None)

#Kullanım kolaylığı için tablonun sadece skor ortalaması olan hali
df_means_only = df.iloc[:, [0,1,2,3,8]]

#Eğer istenen formatta sadece ders skorlarının ortalaması isteniyor ise, "df" yazısı, "df_means_only" ile değiştirilmeli
formatted_table = tabulate(df, headers='keys', tablefmt='pipe', showindex=True, colalign=("center",))

#Dosyaların kaydedilecekleri adresler
output_file_path_txt = r'D:\Workspace\PythonProjects\isYeriOdevi\FormattedDataframe\formatted_dataframe.txt'
output_file_path_csv = r'D:\Workspace\PythonProjects\isYeriOdevi\FormattedDataframe\formatted_dataframe.csv'

#Dosya kayıt işlemleri
with open(output_file_path_txt, 'w') as f:
    f.write(formatted_table)

df.to_csv(output_file_path_csv, index=False)

#Başarılı Kayıt onayı
print("Formatted DataFrame is saved")