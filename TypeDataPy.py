# tipe data 
# a = 10, a adalah variabel dengan nilai 10
# tipe data : angka satuan (integer)
data_integer = 1 # ini boleh apa saja 1000 maupun 100000
print(type(data_integer))
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

# tipe data: desimal / angka dengan koma (float)
data_floar = 1.5
print("data : ", data_floar)
print("- bertipe : ", type(data_floar))

# tipe data: kumpulan karakter (string)
data_string = "wkwkwk"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

#tipe data: biner true / false (boolean)
#tipe data 01 
data_bool = True
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

## tipe data: khusus

# bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

# tipe data dari bahasa C

from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))