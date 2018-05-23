import os

from nltk.stem.snowball import SnowballStemmer


def get_categories():
    f = open("category.csv","r")
    list_categoires = []
    f_str = f.readlines()
    for word in f_str:
        word = word.replace("\n","")
        list_categoires.append(word)
    f.close()
    return list_categoires

def tokenize(word):
    word = ''.join(word)
    word = word.replace("&lt","")
    word = word.replace(",","")
    word = word.replace("!","")
    word = word.replace("@","")
    word = word.replace("#","")
    word = word.replace("%","")
    word = word.replace("$","")
    word = word.replace("^","")
    word = word.replace("&","")
    word = word.replace("*","")
    word = word.replace("(","")
    word = word.replace(")","")
    word = word.replace("-","")
    word = word.replace("+","")
    word = word.replace("<","")
    word = word.replace(".","")
    word = word.replace(">","")
    word = word.replace("/","")
    word = word.replace("?","")
    word = word.replace("_","")
    word = word.replace("=","")
    word = word.replace("{","")
    word = word.replace("[","")
    word = word.replace("}","")
    word = word.replace("]","")
    word = word.replace("\\","")
    word = word.replace("|","")
    word = word.replace(":","")
    word = word.replace(";","")
    word = word.replace("'","")
    word = word.replace("\"","")
    word = word.replace("1","")
    word = word.replace("2","")
    word = word.replace("3","")
    word = word.replace("4","")
    word = word.replace("5","")
    word = word.replace("6","")
    word = word.replace("7","")
    word = word.replace("8","")
    word = word.replace("9","")
    word = word.replace("0","")
    return  word

def list_stop_words():
    f = open("list-stop2.csv","r")
    list_stop=[]
    for word_stop in f.readlines():
        word_stop = word_stop.replace("\n","")
        list_stop.append(word_stop)
    return list_stop

def stop_words(word,list_stop):
    for stop_word in list_stop:
        if ( word == stop_word):
            return True
        else:
            return False

def get_count_dok():
    path = os.getcwd()+'\Dokumen'
    list_count_dok = []
    for foldername in os.listdir(path):
        path = os.getcwd()+'\Dokumen\\'+foldername
        count = 0
        for file in os.listdir(path):
            count = count + 1
        list_count_dok.append(count)
    return list_count_dok

def stemming_word(word):
    stemmer = SnowballStemmer("english")
    return stemmer.stem(word)

def text_preprocessing(dok):
    list_categories = get_categories()
    list_count_dok_by_categories = get_count_dok()
    list_word_perprocessing = []
    list_stop = list_stop_words()
    path = os.getcwd()+'\Dokumen'


    i = 0 # index of number document in separated categories
    j = 0
    for folder_name in os.listdir(path):
        path = os.getcwd()+'\Dokumen\\'+folder_name
        eof = list_count_dok_by_categories[i] * 70 / 100
        j = 0
        while ( j < eof):
            f = open(path+"Categories_"+list_categories[i]+"Doc"+str(j+1)+".csv","r")
            f_str = f.readlines()
            for word_inline in f_str:
                for word in word_inline.split():
                    word = tokenize(word)
                    word = stop_words(word,list_stop)
                    word = stemming_word(word)
                    list_word_perprocessing.append(word)
            j = j + 1
        i = i + 1

