while True:
    print("\n1- Kayıt Ekle")
    print("2- Kayıt Sayısını Göster")
    print("3- Çıkış")
    seçim = input("Seçiminizi yapınız (1-3): ")

    if seçim == "1":
        veri = input("Eklemek istediğiniz kaydı giriniz: ")
        with open("kayıtlar.txt", "a", encoding="utf-8") as dosya:
            dosya.write(veri + "\n")
        print("Kayıt eklendi.")
        
    elif seçim == "2":
        
        with open("kayıtlar.txt", "r", encoding="utf-8") as dosya:
            kayıtlar = dosya.readlines()
            print(f"Toplam kayıt sayısı: {len(kayıtlar)}")

    elif seçim == "3":
        print("Çıkış yapılıyor...")
        break

    else:
        print("Geçersiz seçim, lütfen tekrar deneyiniz.")