# Kelime Oyunu
# v0.3
# - İlk oynanabilir sürüm.

import random

# değişkenler

numbers = ["0","1","2","3","4","5","6","7","8","9"]
special_characters = ["!","@","#","$","%","^","&","*","(",")","-","+","?","_","=",",","<",">","/"]
wordList = ['python','kodlama','algoritma','fonksiyon','oyun','kod','liste']
option = ""
word = ""
hword = ""
letter = ""
i = 0
hak = 0
restart = 0

while restart == 0:
    # ui
    print("""
                Kelime Oyununa Hoş Geldiniz!
            Aşağıdan yapmak istediğiniz işlemi seçin:

        1: Kelime Havuzundan bir kelime seçip tahmin et.
                    2: Oyunu Kapat
    """)

    # ui seçenekleri
    while option != "1" or option != "2":
        option = input(":")

        if option == "1":
            print("Kelime oyunu başlıyor!")
            break
        elif option == "2":
            exit()
        else:
            print("Lütfen 1 veya 2 değerlerinden birini girin!")

    # kelime oyunu
    if option == "1":
        word = random.choice(wordList)
        hak = len(word)
        word2 = '_' * len(word)
        print("Kelimeniz:", word2,
              "\nHarf Sayısı:", len(word))

        if hak <= len(word):
            # harf alma
            while letter == "" or letter in numbers or letter in special_characters or len(letter) > 1:
                letter = input("harf girin:")
                hak -= 1
                if letter in numbers:
                    print("Lütfen harf giriniz!")
                elif len(letter) > 1:
                    print("Lütfen harf giriniz!")
                elif letter in special_characters:
                    print("Lütfen harf giriniz!")
                else:
                    print("\n")
                    print('girilen:', letter.lower())
                    if word.find(letter) == -1:
                        print('kelime içindeki yeri: İÇERMİYOR')
                    else:
                        print('kelime içindeki yeri:', word.find(letter))

                    # harf bulma
                    for i in range(len(word)):
                        if (word[i] == letter.lower()):
                            word2 = word2[:i] + letter.lower() + word2[i + 1:]

                    # harf bulunduktan sonraki hal
                    print("kelimenin yeni hali:", word2)
                    if hak != 0:
                        letter = ""
                        print("kalan hakkınız:", hak)
                    else:
                        if word2.lower() == word.lower():
                            print("")
                            print("OYUNU KAZANDINIZ!!!")
                            print()
                            input("Menüye dönmek için 'ENTER' tuşuna basınız.")

                        else:
                            print("")
                            print("OYUNU KAYBETTİNİZ!!!")
                            print('Doğru kelime:', word.capitalize())
                            print()
                            input("Menüye dönmek için 'ENTER' tuşuna basınız.")