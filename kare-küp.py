while True:
    sayı1 = int(input(" Lütfen Bir Sayı Giriniz: "))
    n = 0
    toplam_Kup = 0
    toplam_kare = 0
    while (n < sayı1):
        n =  n+ 1
        if (n % 2 == 0):
            toplam_Kup = toplam_Kup + n ** 3
            print(f"Küplü Sayıların Toplamı: {toplam_Kup}")
        else:
            toplam_kare = toplam_kare + n ** 2

            print(f"Kareli Sayıların Toplamı: {toplam_kare}")

