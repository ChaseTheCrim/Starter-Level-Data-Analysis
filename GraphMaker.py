import pandas as pd
import matplotlib.pyplot as plt

#Formatlanmış CSV dosyasını okuma
csv_file = r'D:\Workspace\PythonProjects\isYeriOdevi\FormattedDataframe\formatted_dataframe.csv'
df = pd.read_csv(csv_file)

print("Grafikler neyi kıyaslasın?")
print("1- Cinsiyetin skorlar üzerindeki etkisi")
print("2- Etnik kökenin skorlar üzerindeki etkisi")
print("3- Test için hazırlık kursunun skorlar üzerindeki etkisi")
print("4- Anne ve Babanın, öğrenci skoruna etkisi")
print("5- Öğrencinin öğle öğününün skora etkisi")

input_sec = int(input("Seçiminizi yapınız: "))

if input_sec == 1:
    print("Cinsiyet/Skor grafiği:")

    #Cinsiyet belirteçleri
    female_data = df[df['gender'] == 'female']
    male_data = df[df['gender'] == 'male']

    #Kız öğrenciler için scatter plot
    plt.scatter(female_data.index, female_data['average score'], color='red', label='Female')

    #Erkek öğrenciler için scatter plot
    plt.scatter(male_data.index, male_data['average score'], color='blue', label='Male')

    #Eksen etiketleri ve başlık
    plt.xlabel('Student Amount = 1000')
    plt.ylabel('Score')
    plt.title('Scores by Gender')

    #Okuma Kolaylığı için lejant oluşturma
    plt.legend()

    #Grafiği göster
    plt.xticks(ticks=[], labels=[])
    plt.tight_layout()
    plt.show()

elif input_sec == 2:
    print("Etnik köken/Skor grafiği:")

    #Her etnik köken grubu için scatter plot
    for ethnicity in df['race/ethnicity'].unique():
        ethnicity_data = df[df['race/ethnicity'] == ethnicity]
        plt.scatter(ethnicity_data.index, ethnicity_data['average score'], label=ethnicity)

    #Eksen etiketleri ve başlık
    plt.xlabel('Student Amount = 1000')
    plt.ylabel('Score')
    plt.title('Scores by Race/Ethnicity')

    #Okuma Kolaylığı için lejant oluşturma
    plt.legend()

    #Grafiği göster
    plt.xticks(ticks=[], labels=[])
    plt.tight_layout()
    plt.show()

elif input_sec == 3:
    print("Test için hazırlık kursunun skorlar üzerindeki etkisi:")

    #Test hazırlık belirteçleri
    completed_data = df[df['test preparation'] == 'completed']
    none_data = df[df['test preparation'] == 'none']

    #Tamamlanmış test hazırlığı için scatter plot
    plt.scatter(completed_data.index, completed_data['average score'], color='green', label='Completed')

    #Hazırlık yapılmamış test için scatter plot
    plt.scatter(none_data.index, none_data['average score'], color='orange', label='None')

    #Eksen etiketleri ve başlık
    plt.xlabel('Student Amount = 1000')
    plt.ylabel('Score')
    plt.title('Scores by Test Preparation')

    #Okuma Kolaylığı için lejant oluşturma
    plt.legend()

    #Grafiği göster
    plt.xticks(ticks=[], labels=[])
    plt.tight_layout()
    plt.show()

elif input_sec == 4:
    print("Anne ve Babanın, öğrenci skoruna etkisi:")

    #Her ebeveyn eğitim düzeyi için scatter plot
    for education in df['parental level of education'].unique():
        education_data = df[df['parental level of education'] == education]
        plt.scatter(education_data.index, education_data['average score'], label=education)

    #Eksen etiketleri ve başlık
    plt.xlabel('Student Amount = 1000')
    plt.ylabel('Score')
    plt.title('Scores by Parental Level of Education')

    #Okuma Kolaylığı için lejant oluşturma
    plt.legend()

    #Grafiği göster
    plt.xticks(ticks=[], labels=[])
    plt.tight_layout()
    plt.show()

elif input_sec == 5:
    print("Öğrencinin öğle öğününün skora etkisi:")

    #Öğle yemeği belirteçleri
    standard_lunch_data = df[df['lunch'] == 'standard']
    free_reduced_lunch_data = df[df['lunch'] == 'free/reduced']

    #Standart öğle yemeği için scatter plot
    plt.scatter(standard_lunch_data.index, standard_lunch_data['average score'], color='purple', label='Standard')

    #Ücretsiz/indirimli öğle yemeği için scatter plot
    plt.scatter(free_reduced_lunch_data.index, free_reduced_lunch_data['average score'], color='brown', label='Free/Reduced')

    #Eksen etiketleri ve başlık
    plt.xlabel('Student Amount = 1000')
    plt.ylabel('Score')
    plt.title('Scores by Lunch Type')

    #Okuma Kolaylığı için lejant oluşturma
    plt.legend()

    #Grafiği göster
    plt.xticks(ticks=[], labels=[])
    plt.tight_layout()
    plt.show()
