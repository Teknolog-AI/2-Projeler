from fastapi import FastAPI

app = FastAPI()


@app.get("/topla")
def topla(a: float, b: float):
    return  a + b

@app.get("/cikar")
def cikar(a: float, b: float):
    return a - b

@app.get("/carp")
def carp(a: float, b: float):
    return a * b

@app.get("/bol")
def bol(a: float, b: float):
    if b == 0:
        return {"hata": "Bölen sıfır olamaz"}
    return a / b
while True:
    print("1- Toplama")
    print("2- Çıkarma")
    print("3- Çarpma")
    print("4- Bölme")

    secim = input("İşlem Seçiniz 1-2-3-4:")

    s1 = float(input("1.Sayı giriniz:"))
    s2 = float(input("2.Sayı giriniz:"))

    if secim == '1':
        sonuc = topla(s1, s2)
        print("Sonuç:", sonuc)
    elif secim == '2':
        sonuc = cikar(s1, s2)
        print("Sonuç:", sonuc)
    elif secim == '3':
        sonuc = carp(s1, s2)
        print("Sonuç:", sonuc)
    elif secim == '4':
        sonuc = bol(s1, s2)
        print("Sonuç:", sonuc)
    else:
        print("Geçersiz İşlem Seçimi")
    
    