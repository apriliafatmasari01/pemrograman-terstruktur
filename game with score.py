import random
secret_number = random.randint(1, 100)
print("Hi... My name is Mr. Laptop, I have chosen an integer number between 1-100. Can you quess what it is?")

score = 100

while True:
    answer = int(input("\Input number:"))
    if answer == secret_number:
        print ("Selamat, tebakanmu benar!")
        break
        
    else :
        print(
            "Tebakanmu terlalu",
            "kecil" if answer < secret_number else "besar"
            )
        score = score - 5

print ("your score:",score)
      
