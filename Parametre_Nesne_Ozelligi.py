class User:
    def __init__(self, ad):
        ad = ad.upper() # sadece parametre
        self.ad = ad # Nesneye yazıldı
        ad = "Değişti" # parametre değişti
u = User("Ahmet")
print(u.ad)  # Çıktı: AHMET