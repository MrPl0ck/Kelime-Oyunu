# Kelime Oyunu
# v0.1
# - Girilen değer harf değilse hata mesajı (MrPl0ck)
# - Kullanıcı arayüzü (MrPl0ck)
# - Oyunu Başlatma/Kapatma (MrPl0ck)

numbers = ["0","1","2","3","4","5","6","7","8","9"]

print("""
            Kelime Oyununa Hoş Geldiniz!
        Aşağıdan yapmak istediğiniz işlemi seçin:
        
    1: Kelime Havuzundan bir kelime seçip tahmin et.
                2: Oyunu Kapat
""")
option = ""
while option != "1" or option != "2":
    option = input(":")

    match option:
        case "1":
            print("Kelime oyunu başlıyor!")
            break
        case "2":
            exit()
        case _:
            print("Lütfen 1 veya 2 değerlerinden birini girin!")

if option == "1":
    harf = input(":")
    if harf in numbers:
        print("Lütfen harf giriniz!")
    elif len(harf)>1:
        print("Lütfen harf giriniz")
    else:
        print(harf.lower())