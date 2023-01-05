# operasi komperasi
# setiap hasil dari operasi komperasi adalaan boolean
# >, >, >=, <=, ==, !=, is, is not

a = 4
b = 2

# lebih besar dari >
print('======> Lebih besar dari (>)')
hasil = a > 3
print(a,'>',3,'=', hasil)
hasil = b > 2
print(b,'>',2,'=', hasil)

# kurang dari <
print('======> kurang dari (<)')
hasil = a < 3
print(a,'<',3,'=', hasil)
hasil = b < 2
print(b,'<',2,'=', hasil)

# lebih besar sama dengan >=
print('======> kurang dari (>=)')
hasil = a >= 3
print(a,'>=',3,'=', hasil)
hasil = b >= 2
print(b,'>=',2,'=', hasil)
 
# kurang dari sama dengan <=
print('======> kurang dari (<=)')
hasil = a <= 3
print(a,'<=',3,'=', hasil)
hasil = b <= 2
print(b,'<=',2,'=', hasil)

# sama dengan (==)
print('======> sama dengan (==)')
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)

# tidak sama dengan (!=)
print('======> tidak sama dengan (!=)')
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

# 'is' sebagai komperasi object identity
print('======> object identity (IS)')
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =,',x,',id = ',hex(id(x)))
print('nilai y =,',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x =,',x,',id = ',hex(id(x)))
print('nilai y =,',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

# 'is not' sebagai komperasi object identity
print('======> object identity (is not)')
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =,',x,',id = ',hex(id(x)))
print('nilai y =,',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is y =',hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x =,',x,',id = ',hex(id(x)))
print('nilai y =,',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is y =',hasil)

# catatan: tulis di terminal ====> python
# tulis x = 5
# tulis x lalu enter 
# nanti ada tulisan (5)
# setelah itu tulis id(x)
# maka akan kelihatan alamat (x)nya
# setelah itu tulis hex(id(x))
# nanti muncul alamat (x)nya