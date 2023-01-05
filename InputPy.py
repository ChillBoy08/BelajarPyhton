#input user (mengambil input dari user)
#data yang dimasukan pasti string
data = input("masukan data: ")
print("data = ",data,",type =", type(data))

# jika kita ingin mengambil integer(int), maka
data_int = int(input("masukan angka; "))
print("data = ",data_int,",type =", type(data_int))

# data_int bisa diganti menjadi angka atau float
angka = float(input("masukan angka"))
angka = int(input("masukan angka"))
print("data = ",angka,",type =",type(angka))

# menggunakan boolean
# di casting ke integer hbs itu casting ke boolean
biner = bool(int(input("masukan nilai boolean: ")))
print("data =",biner,",type =",type(biner))

