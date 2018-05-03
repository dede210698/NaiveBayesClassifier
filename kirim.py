import os
import math

#===============Membuat List Kategori untuk Entity Kategori=================#
f2=open("category.csv","w+")
path=os.getcwd()+'/Dokumen'
l=[]
i=0
for foldername in os.listdir(path):
    path = os.getcwd()+'\Dokumen\\'+foldername
    j=0
    #++++++++++Proses membuat list kategori untuk Entity Kategori+++++++++#
    f2.write("id_Kategori"+str(i+1)+","+foldername+"\n")
    #++Proses menghitung jumlah data yang akan di jadikan data testing++#
    for file in os.listdir(path):
        j=j+1
    j = j*70/100
    i=i+1
    l.append(math.floor(j))
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

f2.close()
#=======================Isi entiti dokumen lama#
i=0
j=0
f=open("document2.csv","w+")
path=os.getcwd()+'/Dokumen'
for foldername in os.listdir(path):
    try:
        path = os.getcwd()+'\Dokumen\\'+foldername
            
        for filename in os.listdir(path):
            f3=open(path+"\\"+filename,"r")
            fstr=f3.readlines()
            kata=[]
            for x in fstr:
                kata.append(x)
            kata_str = ''.join(kata)
            kata_str = kata_str.replace("\n"," ")
            if(j>=l[0]):
                f.write("id_Docs"+str(j+1)+",id_Kategori"+str(i+1)+","+kata_str+",data_uji\n") 
            else:
                f.write("id_Docs"+str(j+1)+",id_Kategori"+str(i+1)+","+kata_str+",data_latih\n") 
             
             #print(filename)
            j=j+1
        i=i+1
    except Exception as e:
        raise e
f.close()
f3.close()
