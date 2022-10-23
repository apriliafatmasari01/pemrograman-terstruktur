a = int(input('Masukan nilai bahasaindonesia'))
b = int(input('Masukan nilai matematika'))
c = int(input('Masukan nilai ipa'))

while True:
       
       if a < 0 :
          print("Maaf input ada yang tidak valid")
       elif b < 0 :
           print("Maaf input ada yang tidak valid")
       elif c < 0 :
           print("Maaf input ada yang tidak valid")
       elif a < 60 :
          print("TIDAK LULUS")
       elif b < 60:
          print (" TIDAK LULUS")
       elif c < 60 :
           print ("TIDAK LULUS")
       else :
           print ("LULUS")
       break 
