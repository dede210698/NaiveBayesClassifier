# NaiveBayesClassifier
Proyek-2

---DATA YANG DIPROSES HANYA DATA LATIH SAJA--

Proses Menentukan Kategori yang ada pada dataset reuters beserta peluang
  input : dataset reuters
  output : list kategori dan peluangnya yang disimpan kedalam 1 buah file sementara .csv (Optional : langsung disimpan ke DB apabila penentuan kategori sekali proses langsung "benar")
  Format dalam file : | Nama Kategori | Peluang Kategori |
  Keterangan : proses ini dilakukan sebelum melakukan teks preprosesing , karena teks preprosesing lebih memperhatikan term-termnya saja. hasil dari proses ini akan dimasukkan kedalam DB (Tabel Kategori)

Text Preprocessing :

  1 Tokenize
    input : seluruh dokumen reuters
    output : kata(term) seluruh dokumen beserta kategorinya yang disimpan kedalam 1 buah file sementara .csv (Optional : beberapa file csv)
    Format dalam file : | NamaTerm | Kategori |

  2 Stopword
    input : file .csv hasil tokenize
    output : kata(term) seluruh dokumen yang sudah dihilangkan stopword (kata yang tidak bermakna) beserta kategorinya disimpan kedalam 1 buah file sementara .csv (Optional : beberapa file csv)
    Format dalam file : | NamaTerm | Kategori |

  3 Stemming (Menggunakan Stemmer Snowball (porter 2))
    input : file .csv hasil stopword
    output : kata(term) seluruh dokumen yang sudah distemming (dihilangkan akhiran kata karena bahsa inggris) beserta kategorinya   disimpan kedalam 1 buah  file sementara .csv (Optional : beberapa file csv)
    Format dalam file : | NamaTerm | Kategori | 

  4.a Proses Membuat Term(Kata) Unik satu sama lain.
      input : file.csv hasil stemming
      output : kata(term) seluruh dokumen unik dan disimpan kedalam 1 buah file sementara .csv (Optional : langsung disimpan ke DB apabila sekali proses langsung "benar")
      Format dalam file : | NamaTerm |
      Keterangan : hasil dari proses ini , akan dimasukkan kedalam DB (Tabel Term)

  4.b Proses Membuat Term(Kata) Unik satu sama lain dan menghitung frekuensinya
      input : file.csv hasil stemming
      output : kata(term) seluruh dokumen beserta frekuensinya pada masing-masing kategori dan disimpan kedalam 1 buah file  sementara .csv
      Format dalam file :| Nama Term | Nama Kategori | Frekuensi |
   
  5. Proses perhitungan peluang masing-masing term pada masing-masing kategori
     input : file.csv hasil proses no 4.b
     output : kata(term) seluruh dokumen beserta kategorinya dan peluang term pada masing-masing kategori dan disimpan kedalam 1 buah file sementara .csv (Optional : langsung disimpan ke DB apabila sekali proses langsung "benar")
     Format dalam file :| Nama Term | Nama Kategori | Peluang Term |
     Keterangan : hasil dari proses ini, akan dimasukkan kedalam DB (Tabel Kamus)

