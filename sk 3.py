a = int(input('Masukkan nilai bahasa Indonesia'))
b = int(input('Masukkan nilai matematika'))
c = int(input('Masukkan nilai ipa'))

while True :
 
    if a < 60 :
        print ( "Status Kelulusan: Tidak Lulus")
        print (" Nilai bahasa indonesia kurang dari 60")
    elif b < 60 :
        print ( "Status Kelulusan: Tidak Lulus")
        print (" Nilai matematika kurang dari 60")
    elif c < 60 :
        print ( "Status Kelulusan: Tidak Lulus")
        print (" Nilai ipa kurang dari 60")
    else :
        print ("Status Kelulusan: Lulus")
    break 
