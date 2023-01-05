# operator Bitwise, operasi biner, binary

a = 6
b = 5

# Bitwise OR (|)
c = a | b
print('\n=====OR=====')
print('nilai :',a,' ,binary :',format(a,'08b'))
print('nilai :',b,' ,binary :',format(b,'08b'))

print('----------------------------(| di jumblahkan)')
print('nilai :',c,' ,binary :',format(c,'08b'))

#bitwise (and)
c = a & b
print('\n=====AND=====')
print('nilai :',a,' ,binary :',format(a,'08b'))
print('nilai :',b,' ,binary :',format(b,'08b'))

print('----------------------------(&)')
print('nilai :',c,' ,binary :',format(c,'08b'))

# bitwise XOR(^)
c = a ^ b 
print('\n=====XOR=====')
print('nilai :',a,' ,binary :',format(a,'08b'))
print('nilai :',b,' ,binary :',format(b,'08b'))

print('----------------------------(^)')
print('nilai :',c,' ,binary :',format(c,'08b'))

# bitwise 
c = -a
print('\n=====NOT=====')
print('nilai :',a,' ,binary :',format(a,'08b'))
print('----------------------------(-)')
print('nilai :',c,' ,binary :',format(c,'08b'))

# kalau mau di flip menjadi 1111111 emnggunakan XOR
print('----------------------(^)')
d = 0b0000001001
e = 0b1111111111
print('nilai :',e^d,',binary :',format(e^d,'08b'))

# shifting
# shift right (>>)
c = a >> 1
print('\n======>>======')
print('nilai :',a,' ,binary :',format(a,'08b'))
print('----------------------------(>>)')
print('nilai :',c,' ,binary :',format(c,'08b'))

# shift lift (<<)
c = a << 1
print('\n======<<======')
print('nilai :',a,' ,binary :',format(a,'08b'))
print('----------------------------(<<)')
print('nilai :',c,' ,binary :',format(c,'08b'))


