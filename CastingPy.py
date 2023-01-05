# casting
# merubah satu tipe ke tipe yg lain

# INTEGER
print("====INTEGER====")
data_int = 0 # kalo nilai nya 0 maka akan false(salah) kalo 1 atau -1 maka (true)
print("data = ", data_int, ", type =", type(data_int))

data_float = float(data_int) #masukan data yg ingin di ubah
data_string = str(data_int) 
data_bool = bool(data_int) 
print("data = ", data_float, ", type =", type(data_float))
print("data = ", data_string, ", type =", type(data_string))
print("data = ", data_bool, ", type =", type(data_bool))
 
 # FLOAT
print("====FLOAT====")
data_float = 0 #jika 0 maka akan false
print("data = ", data_float, ", type =", type(data_float))

data_int = int(data_float) # akan dibulatkan kebawah dari 9.6 menjadi 9
data_string = str(data_float) 
data_bool = bool(data_float) 
print("data = ", data_int, ", type =", type(data_int))
print("data = ", data_string, ", type =", type(data_string))
print("data = ", data_bool, ", type =", type(data_bool))

# BOOLEAN
print("====BOOLEAN====")
data_bool = True # kalo true(benar) maka nilainya 1 dan 1.0,, jika false(salah) maka nilainya 0 dan 0.0
print("data = ", data_bool, ", type =", type(data_bool))

data_int = int(data_bool) 
data_string = str(data_bool) 
data_float = float(data_bool) 
print("data = ", data_int, ", type =", type(data_int))
print("data = ", data_string, ", type =", type(data_string))
print("data = ", data_float, ", type =", type(data_float))

# STRING
print("====STRING====")
data_string = "11" #jika kosong maka akan false dan harus angkaa
print("data = ", data_string, ", type =", type(data_string))

data_int    = int(data_string) 
data_float  = str(data_string) 
data_bool   = bool(data_string) #jika angka maka akan true
print("data = ", data_int, ", type =", type(data_int))
print("data = ", data_float, ", type =", type(data_float))
print("data = ", data_bool, ", type =", type(data_bool))