# operasi aritmatika

a = 3
b = 9

#operasi pertambahan (+)
hasil = a + b
print(a,'+',b,'=', hasil)

#operasi pengurangan (-)
hasil = a - b
print(a,'-',b,'=', hasil)

#operasi perkalian (*)
hasil = a * b
print(a,'*',b,'=', hasil)

#operasi pembagian (/)
hasil = a / b
print(a,'/',b,'=', hasil)

#operasi eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=', hasil)

#operasi modulus (sisa pembagian) %
hasil = a % b
print(a,'%',b,'=', hasil)

#operasi floor division (sisa pembagian double) // 
hasil = a // b
print(a,'//',b,'=', hasil) # dibulatkan kebawah

# prioritas oprasi, oprational precedence
'''
    1. ()
    2. exsponen **
    3. perkalian dan teman - teman nya * / ** % //
    4. pertambahan dan perkurangan + -
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)

# tanda kurung akan mengambil langkah paling pertama
hasil = (x + y) * z
print('(',x,'+',y,')*',z,'=',hasil)

