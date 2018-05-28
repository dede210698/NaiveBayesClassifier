import os
import math

from nltk.stem.snowball import SnowballStemmer;
import MySQLdb

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

def getListKategori():
    f = open("category.csv", "r")
    listKategori = []
    f_str = f.readlines()
    for word in f_str:
        word = word.replace("\n", "")
        listKategori.append(word)
    f.close()
    return listKategori

def getListStopWord():
    f = open("list-stop2.csv", "r")
    listStopWord = []
    for word_stop in f.readlines():
        word_stop = word_stop.replace("\n", "")
        listStopWord.append(word_stop)
    return listStopWord

def checkStopWord(word,listStopWord):
    if word in listStopWord:
        return True
    else:
        return False
#membuat list jumlah dokumen pada setiap kategori
def createListJumlahDokumen():
    path = os.getcwd() + '\Dokumen'
    listJumlahDokumen = []
    for foldername in os.listdir(path):
        path = os.getcwd() + '\Dokumen\\' + foldername
        listJumlahDokumen.append(len(os.listdir(path)))
    return listJumlahDokumen

def stemming(word):
    stemmer = SnowballStemmer("english")
    return stemmer.stem(word)

#membuat list term unique tiap kategori
def createListTermUnique(listTermEveryKategori):
    listTermUnique = []
    i=0
    while(i<len(listTermEveryKategori)):
         listTermUnique.append(set(listTermEveryKategori[i]))
         i = i+1
    return listTermUnique


#membuat list jumlah tiap term  pada tiap kategori
def createListJumlahTermUnique(listTermEveryKategori,listTermUnique):
    listJumlahTermUnique=[]
    i=0
    while(i<len(listTermEveryKategori)):
        tempJumlahTermUnique = []
        for word in listTermUnique[i]:
            tempJumlahTermUnique.append(listTermEveryKategori[i].count(word))
        listJumlahTermUnique.append(tempJumlahTermUnique)
        i = i+1
    return listJumlahTermUnique

#membuat list totalterm  tiap kategori
def createListTotalTerm(listJumlahTermUnique):
    listTotalTerm=[]
    i=0
    while(i<len(listJumlahTermUnique)):
        listTotalTerm.append(sum(listJumlahTermUnique[i]))
        i = i+1
    return listTotalTerm

def createListAllTermUnique(listTermUnique):
    tempListAllTermUnique =[]
    i=0
    while(i<len(listTermUnique)):
        tempListAllTermUnique.extend(listTermUnique[i])
        i = i + 1

    listAllTermUnique = set(tempListAllTermUnique)

    return listAllTermUnique

def getTotalVocabulary(listAllTermUnique):
    return len(listAllTermUnique)


def naive_bayes():
    #conn = MySQLdb.connect('localhost','root','','naive bayes')
    #cursor = conn.cursor()
    
    listKategori=getListKategori()
    listStopWord = getListStopWord()
    
    #print(listStopWord)
    dokUsed = 70/100
    listTermEveryKategori = []
    totalDokumen=0
    inc=0
    for folderName in listKategori:
        path = os.getcwd() + '\Dokumen\\' + folderName
        maxDokumen = math.floor(len(os.listdir(path)) * dokUsed)
        i=0
        listTermAfterProcess=[]
        while(i<maxDokumen):
            fp = open(path + "\\Categories_" + folderName + "Doc_" + str(i + 1) + ".csv", "r") #path ke masing-masing dokumen pada kategori tertentu
            buffer = fp.readlines()
            listTerm=[]
            for kalimat in buffer:
                for term in kalimat.split(): #kalimat.split() menghasilkan list kata-kata dari suatu kalimat yang dibaca
                    term = tokenize(term)#tokenize setiap kata
                    if(not checkStopWord(term,listStopWord)):#check stopword
                        term = stemming(term)#stemming
                        if(len(term)>3):#check apakah kata tersebut lebih dari 3 huruf
                            listTerm.append(term)
            listTermAfterProcess.extend(listTerm)
            fp.close()
            i = i + 1
            inc=inc + 1
            print("Total Dokumen :" + str(inc) + '\n')
            print("Kategori : " + folderName + " Current File :" + str(i) + '\n')
        totalDokumen=totalDokumen+maxDokumen
        listTermEveryKategori.append(listTermAfterProcess)

    listTermUnique = createListTermUnique(listTermEveryKategori) #membuat list term pada setiap kategori unique
    listJumlahTermUnique = createListJumlahTermUnique(listTermEveryKategori,listTermUnique) #membuat list jumlah term pada setiap kategori
    listAllTermUnique = createListAllTermUnique(listTermUnique) #membuat list semua term unique
    totalVocabulary = getTotalVocabulary(listAllTermUnique) #menghitung total term yang digunakan
    listTotalTermKategori = createListTotalTerm(listJumlahTermUnique) #membuat list total term pada setiap kategori
    listJumlahDokKategori = createListJumlahDokumen() #membuat list jumlah dokumen pada setiap kategori
    print(len(listTermEveryKategori))
    print(totalDokumen)
    #print(listTermEveryKategori)
    #print(listJumlahTermUnique)
    #print(listAllTermUnique)
    #print(totalVocabulary)

    #membuat kamus untuk entity kategori
    kamusKategoriPeluang = {}
    m=0    
    while(m<len(listTermEveryKategori)):
        peluang = listJumlahDokKategori[m]/totalDokumen
        kamusKategoriPeluang.update ({listKategori[m] : peluang})
        m= m+1

    #membuat kamus untuk menyimpan data Nama Kategori dan Jumlah Term Pada Kategori Tertentu
    #dengan struktur (Nama Kategori : TotalTerm)
    kamusKategoriTerm = {}
    k=0
    while(k<len(listTermEveryKategori)):
        kamusKategoriTerm.update({listKategori[k] : listTotalTermKategori[k]})
        k= k+1
    
    #membuat kamus untuk menyimpan data Term , Nama Kategori dan Peluang Term Tertentu
    #dengan struktur (Term : (Nama Kategori : Peluang))
    kamusNB = {}
    for term in listAllTermUnique:
        l=0
        kamusKategoriFrek= {}
        while(l<len(listTermEveryKategori)):
            jumlahTermInKategori = kamusKategoriTerm[listKategori[l]]
            jumlahTerm = listTermEveryKategori[l].count(term)
            peluang = (jumlahTerm + 1) / (jumlahTermInKategori + totalVocabulary)
            kamusKategoriFrek.update({listKategori[l] : peluang})
            #kamusKategoriFrek[listKategori[l]] = listTermEveryKategori[l].count(term)
            l=l+1
        kamusNB.update({term : kamusKategoriFrek})

    #menyimpan data kamusNB yang telah dibuat kedalam file.csv (sementara)
    #dengan format Nama Term,Nama Kategori,Peluang
    fp = open("Kamus.csv","w+")
    for term,kategoriInfo in kamusNB.items():
        for kategori in kategoriInfo:
            #kategoriInfo[kategori] = (kategoriInfo[kategori] + 1 )/ (kamusKategoriTerm[kategori] + totalVocabulary) 
            fp.write(term +","+kategori+","+str(round(kategoriInfo[kategori],7))+"\n")
            #print(term + " = {" + kategori + " : " + str(kategoriInfo[kategori]) + " }")
    fp.close()
    
    #conn.close()
     
    


    
