ket = """selamat datang di perhotungan rumus :
        1. untuk menghitung luas persegi
        2. untuk menghitung luas lingkaran
        3. untuk menghitung luas segitiga"""
print(ket)
pilihan = input("pilihanmu?")

match pilihan:
    case "1": 
        print("Rumus persegi adalah")
        sisi =int(input("masukkan panjang sisi persgi"))
        luasP = sisi*sisi
        print("luas persegi adalah", luasP )
    case "2":
        print("rumus lingkaran adalah")
        jari2 = float(input("masukkan jari jari"))
        luasL = 3.14 * jari2 * jari2
        print("luas lingkaran yang jari2nya", luasL)
    case "3":
        print("rumus segitiga adalah")
        alas = int(input("masukan nilai alas"))
        tinggi = float(input("masukkan nilai alas"))
        luasS = (0.5)*alas*tinggi
        print("luas segitiga adalah", luasS)      
    case _:
        print("pilihanmu salah!")  



