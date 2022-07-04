##########################################
              # 2. ÖDEV #
##########################################


# Görev 1:Kendi isminizde bir virtual environment oluşturunuz, oluşturma esnasında python 3 kurulumu yapınız.
# Görev 2:Oluşturduğunuz environment'ı aktif ediniz.
# Görev 3:Yüklü paketleri listeleyiniz.
# Görev 4:Environment içerisine Numpy'ın güncel versiyonunu ve Pandas'ın 1.2.1 versiyonunu aynı anda indiriniz.
# Görev 5:İndirilen Numpy'ın versiyonu nedir?
# Görev 6:Pandas'ı upgrade ediniz. Yeni versiyonu nedir?
# Görev 7:Numpy'ı environment'tan siliniz.
# Görev 8:Seaborn ve matplotlib kütüphanesinin güncel versiyonlarını aynı anda indiriniz.
# Görev 9:Virtual environment içindeki kütüphaneleri versiyon bilgisi ile beraber export ediniz ve yaml dosyasını inceleyiniz.
# Görev 10:Oluşturduğunuz environment'i siliniz. Önce environment'i deactivate ediniz.


# Çözüm 1: conda create -n İsim
# Çözüm 2: conda activate İsim
# Çözüm 3: conda list
# Çözüm 4: conda install numpy pandas=1.21
# Çözüm 5: conda list
# Çözüm 6: conda upgrade pandas
# Çözüm 7: conda remove numpy
# Çözüm 8: conda install seaborn matplotlib
# Çözüm 9: conda env export > environment.yaml
# Çözüm 10: conda env remove -n İsim

##########################################
              # 3. ÖDEV #
##########################################

#TODO:
# GÖREV-1: Veri tiplerini sorgulayınız.

# X= 8
# Y= 3.2
# Z= 8J+18
# S= "HELLO WORLD"
# B= True
# C= 23<22
# L= [1,2,3,4]
# D= {Name: "Jack", Age: 22}
# T= ("Machine learning" "Data science")
# S= {"Python","Veri"}

# Görev-1 CEVAPLAR:
# X= İNTEGER
# Y= FLOAT
# Z= COMPLEX
# S= STRİNG
# B= BOOLEN
# C= FALSE
# L= LİST
# D= DİCTİONARY
# T= TUPLE
# S= SET

#TODO:
# GÖREV-2 Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. virgül ve nokta yerine boşluk koyunuz.
text= "The goal is to turn data information, and information into insight."

# GÖREV-2 CÖZÜM:
# 1- text = text.upper()
# 2- text = text.replace("," , " ")
# 3- text = text.replace("." , " ")
# 4- text = text.split()

#TODO:
# GÖREV-3 Verilen listeye aşağıdaki adımları uygulayınız.
list= ["D","A","T","A","S","C","İ","E","N","C","E",]
# Adım1: Verilen listenin eleman sayısına bakınız.
# Adım2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
# Adım3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
# Adım4: Sekizinci indeksteki elemanı siliniz.
# Adım5: Yeni bir eleman ekleyiniz.
# Adım6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

# GÖREV-3 ÇÖZÜM:
# Adım1 : len(list)
# Adım2 : list[0] , list[10]
# Adım3 : list2=list[:4]
# Adım4 : list.pop(8)
# Adım5 : list.append(25)
# Adım6 : list.insert(8,"N")

#TODO:
# GÖREV-4 Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
# dict={ "Christian" : ["America",18],
#       "Daisy": ["England",12],
#       "Antonio": ["Spain",22],
#       "Dante": ["İtaly",25]}
# Adım1: Key değerlerine erişiniz.
# Adım2: Value'lara erişiniz.
# Adım3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
# Adım4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
# Adım5: Antonio'yu dictionary'den siliniz.

# GÖREV-4 ÇÖZÜM:
# 1- dict.keys()
# 2- dict.values()
# 3- dict["Daisy"] = ["England" , 13]
# 4- dict["Ahmet"] = ["Turkey" , 24]
# 5- dict.pop("Antonio")

#TODO:
# GÖREV-5 Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan
# ve bu listeleri return eden fonksiyon yazınız.

# GÖREV-5 ÇÖZÜM:
l = [2, 13, 18, 93, 22]
even_list = []
odd_list = []

def func( a=[]):
    for i in l:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return odd_list, even_list
odd_list, even_list = func(l)
print(odd_list, even_list)

#TODO:
# GÖREV-6 List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz
# ve başına NUM ekleyiniz.

#GÖREV-6 ÇÖZÜM:
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns
num_col = num_col = ["NUM" + col.upper() if df[col].dtype != "O"] else col.upper() for col in df.columns]

#TODO:
# GÖREV-7 List Comprehension yapısı kullanarak car_crashes verisinde isminde"no" barındırmayan değişkenlerin isimlerinin
# sonuna "FLAG" yazınız.

#GÖREV-7 ÇÖZÜM:
import seaborn as sns
df=sns.load_dataset("car_crashes")
df.columns
new_col = [col.upper() + "FLAG" if "no" not in col else col.upper() for col in df.columns ]
df.columns = new_col

#TODO:
# GÖREV-8 List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini
# seçiniz ve yeni bir data frame oluşturunuz.

#GÖREV-8 ÇÖZÜM:
import seaborn as sns
df = sns.load_dataset("car_crashes")
og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]

