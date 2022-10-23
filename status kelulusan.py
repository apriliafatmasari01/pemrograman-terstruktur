a = int(input('Masukkan nilai bahasa_Indonesia'))
b = int(input('Masukkan nilai matematika'))
c = int(input('Masukkan nilai ipa'))

while True :
    if a < 0 :
        print ("Maaf input ada yang tidak valid")
    elif a < 60 :
        print ( "Tidak Lulus")
    else :
        print ("Lulus")


    if b < 0 :
        print ("Maaf input ada yang tidak valid")
    elif b < 60 :
        print ( "Tidak Lulus")
    else :
        print ("Lulus")


    if c < 0 :
        print ("Maaf input ada yang tidak valid")
    elif c < 60 :
        print ( "Tidak Lulus")
    else :
        print ("Lulus")
    break
