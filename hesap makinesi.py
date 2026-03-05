
def toplama(a, b):
    return a + b


def cikarma(a, b):
    return a - b


def carpma(a, b):
    return a * b


def bolme(a, b):
    return a / b


sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))


islem = input("Yapılacak işlemi giriniz (+, -, *, /): ")


if islem == "+":
    sonuc = toplama(sayi1, sayi2)
elif islem == "-":
    sonuc = cikarma(sayi1, sayi2)
elif islem == "*":
    sonuc = carpma(sayi1, sayi2)
elif islem == "/":
    sonuc = bolme(sayi1, sayi2)
else:
    sonuc = "Geçersiz işlem seçildi."


print("Sonuç:", sonuc)