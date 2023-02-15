# BelajarPyhton
`Python` adalah bahasa pemrograman tingkat tinggi yang sangat populer dan sering digunakan untuk pengembangan perangkat lunak, analisis data, dan kecerdasan buatan. Python mudah dipelajari, mudah dipahami, dan sangat fleksibel, menjadikannya pilihan ideal bagi programmer pemula dan ahli.

Berikut adalah beberapa dasar-dasar `Python` yang harus dipahami oleh programmer pemula:
1. Variabel
   Variabel digunakan untuk menyimpan data di Python. Sebuah variabel harus didefinisikan terlebih dahulu sebelum digunakan. `Contoh: nama = 'John'`.

2. Tipe data
   `Python` mendukung beberapa jenis data, termasuk integer, float, string, boolean, list, tuple, dan dictionary. Jenis data dapat ditentukan secara otomatis oleh          `Python` berdasarkan nilai yang diberikan. Contoh: `umur = 25` atau `nama = 'John'`.

3. Operasi matematika
   `Python` mendukung berbagai operasi matematika seperti penjumlahan, pengurangan, perkalian, dan pembagian. `Contoh: a = 5; b = 3; c = a + b`

4. Percabangan
   Percabangan digunakan untuk memilih antara dua atau lebih jalur program berdasarkan kondisi yang diberikan. `Python` menggunakan pernyataan if untuk percabangan.  
   ```python
   contoh:
   umur = 25
   if umur > 18:
      print('Anda sudah dewasa')
   else:
      print('Anda masih anak-anak')
   ```
   
 5. Perulangan
    Perulangan digunakan untuk mengeksekusi blok kode tertentu secara berulang. `Python` memiliki dua jenis perulangan, yaitu for dan while. 
    ```scss
    contoh:
    for i in range(5):
    print(i)
    ```
    
 6. Fungsi
    Fungsi adalah blok kode yang dapat dipanggil dari bagian lain dari program. `Python` memiliki banyak fungsi bawaan, dan pengguna juga dapat membuat fungsi mereka       sendiri. 
    ```python
    Contoh:
    def penjumlahan(a, b):
      c = a + b
      return c
    ```
    
 7. Modul
    Modul adalah file yang berisi fungsi, variabel, dan kelas yang dapat digunakan dalam program Python. `Python` memiliki banyak modul bawaan, seperti modul math dan     random.
    
 8. Kelas dan Objek
    `Python` adalah bahasa pemrograman berorientasi objek, yang berarti bahwa pengguna dapat membuat kelas dan objek. Kelas digunakan untuk mendefinisikan atribut dan     metode, sementara objek adalah instance dari kelas. 
    ```ruby
    Contoh:
    class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def sapa(self):
        print('Halo, nama saya', self.nama)

    john = Manusia('John', 25)
    john.sapa()
    ```
 9. Input dan Output
    `Python` mendukung input dan output, yang memungkinkan pengguna untuk berinteraksi dengan program. `Input` dapat diterima dari pengguna menggunakan fungsi             `input()`, sedangkan `output` dapat ditampilkan dengan fungsi `print()`. 
    ```python
    Contoh:
    nama = input('Masukkan nama Anda: ')
    print('Halo,', nama)
    ```
