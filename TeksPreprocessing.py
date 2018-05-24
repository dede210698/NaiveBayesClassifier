import os
import math

from nltk.stem.snowball import SnowballStemmer;

#mengambil kategori kedalam list
def get_categories():
    f = open("category.csv", "r")
    list_categoires = []
    f_str = f.readlines()
    for word in f_str:
        word = word.replace("\n", "")
        list_categoires.append(word)
    f.close()
    return list_categoires

#menghilangkan huruf selain alphabet dan hanya menggunakan alpabed lowercase (ASCII 65 - 81) ==> tokenize
def tokenize(word):
    word = ''.join(word)
    word = word.lower()
    word = word.replace("&lt", "")
    word = word.replace(",", "")
    word = word.replace("!", "")
    word = word.replace("@", "")
    word = word.replace("#", "")
    word = word.replace("%", "")
    word = word.replace("$", "")
    word = word.replace("^", "")
    word = word.replace("&", "")
    word = word.replace("*", "")
    word = word.replace("(", "")
    word = word.replace(")", "")
    word = word.replace("-", "")
    word = word.replace("+", "")
    word = word.replace("<", "")
    word = word.replace(".", "")
    word = word.replace(">", "")
    word = word.replace("/", "")
    word = word.replace("?", "")
    word = word.replace("_", "")
    word = word.replace("=", "")
    word = word.replace("{", "")
    word = word.replace("[", "")
    word = word.replace("}", "")
    word = word.replace("]", "")
    word = word.replace("\\", "")
    word = word.replace("|", "")
    word = word.replace(":", "")
    word = word.replace(";", "")
    word = word.replace("'", "")
    word = word.replace("\"", "")
    word = word.replace("1", "")
    word = word.replace("2", "")
    word = word.replace("3", "")
    word = word.replace("4", "")
    word = word.replace("5", "")
    word = word.replace("6", "")
    word = word.replace("7", "")
    word = word.replace("8", "")
    word = word.replace("9", "")
    word = word.replace("0", "")
    return word

#mengambil stop word kedalam list
def list_stop_words():
    f = open("list-stop2.csv", "r")
    list_stop = []
    for word_stop in f.readlines():
        word_stop = word_stop.replace("\n", "")
        list_stop.append(word_stop)
    return list_stop

#membuat list dengan list tersebut  sudah dibuang huruf stop wordnya
def stop_words(word, list_stop):
    for stop_word in list_stop:
        if (word == stop_word):
            return True
        else:
            return False

#menghitung jumlah dokumen pada tiap kategori
def get_count_dok():
    path = os.getcwd() + '\Dokumen'
    list_count_dok = []
    for foldername in os.listdir(path):
        path = os.getcwd() + '\Dokumen\\' + foldername
        list_count_dok.append(len(os.listdir(path)))
    return list_count_dok

#melakukan stemming pada list kata dan mengembalikan list kata yang baru setelah hasil stemming
def stemming_word(word):
    stemmer = SnowballStemmer("english")
    return stemmer.stem(word)


#membuat list term unik pada tiap kelas dengan  menghasilkan list 2dimensi
def unique_in_categories(list_word_preprocessing):
    list_categories = get_categories()
    list_word_unique = []
    i = 0
    while ( i < len(list_categories)):
        list_word_unique.append(set(list_word_preprocessing[i]))
        i = i + 1
    return  list_word_unique

# menghitung jumlah kata unik pada tiap kelas
def count_a_word_in_categories(list_word_preprocessing,list_word_unique):
    list_categories = get_categories()
    list_word_unique_count = []
    i = 0
    while(i < len(list_categories)):
        l_temp = []
        for word in list_word_unique[i]:
            l_temp.append(list_word_preprocessing[i].count(word))
        list_word_unique_count.append(l_temp)
        i = i + 1
    return list_word_unique_count

#menghitung seluruh jumlah kata pada tiap kelas
def count_word_in_categories(list_word_preprocessing):
    list_categories = get_categories()
    list_count_word_categories = []
    i = 0
    while (i < len(list_categories)):
        list_count_word_categories.append(len(list_word_preprocessing[i]))
        i = i + 1
    return list_count_word_categories


#mebuat term unik untuk seluruh kelas
def term_unique(list_word_unique):
    list_categories = get_categories()
    l_temp = []
    l_temp2 = []
    i = 0
    while(i < len(list_categories)):
        for word in list_word_unique[i]:
            l_temp.append(word)
        i = i + 1
    l_temp2 = set(l_temp)
    return  l_temp2
#mengitung jumlah kata untuk kamus
def count_term_unique(list_word_unique_all_categories):
    return len(list_word_unique_all_categories)

def naive_bayes():
    list_categories = get_categories()
    list_count_dok_by_categories = get_count_dok()
    list_word_perprocessing = []
    list_stop = list_stop_words()

    list_word_unique = []
    list_word_unique_count = []
    list_count_word = []
    list_term_uniqe = []


    path = os.getcwd() + '\Dokumen'

    i = 0  # index of number document in separated categories

    for folder_name in os.listdir(path):
        path = os.getcwd() + '\Dokumen\\' + folder_name
        eof = list_count_dok_by_categories[i] * 70 / 100
        j = 0

        while (j < math.floor(eof)):
            f = open(path + "\\Categories_" + list_categories[i] + "Doc_" + str(j + 1) + ".csv", "r")
            f_str = f.readlines()
            list_word= []
            for word_inline in f_str:
                for word in word_inline.split():
                    word = tokenize(word)
                    if (not stop_words(word, list_stop)):
                        word = stemming_word(word)
                        if(len(word)>3):
                            list_word.append(word)
            list_word_perprocessing.append(list_word)#2 dimensi
            f.close()
            j = j + 1
        i = i + 1

    list_word_unique = unique_in_categories(list_word_perprocessing)#2 dimensi
    print("list word selesai\n")
    list_word_unique_count = count_a_word_in_categories(list_word_perprocessing,list_word_unique)#2 dimensi jumlah kata tentu pada tiap kelas
    print("hitung list word selesai\n")
    list_count_word = count_word_in_categories(list_word_perprocessing) #1 dimensi jumlah kata pada tiap kelas
    print("jumlah term seluruh")
    list_term_uniqe = term_unique(list_word_unique) # untuk entity term
    print("entity term")
    sum_term = count_term_unique(list_term_uniqe)
    i = 0
    f = open("naivebayes.csv","w+")
    while(i < len(list_categories)):
        j = 0
        while(j < len(list_word_unique_count[i])):
            peluang = ( list_word_unique_count[i][j] + 1) / (list_count_word[i] + sum_term)
            f.write(list_word_unique[i][j]+","+list_categories[i]+","+str(round(peluang,7)) +"\n")
            j = j + 1
        i = i + 1
    f.close()
