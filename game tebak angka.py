import random

def main():
    print("Selamat datang di GAME TEBAK ANGKA!")
    print("Saya punya angka dari 1 sampai 100. Tebak angka punyaku?")

    tebak_angka = random.randint(1, 100)

    while True:
        try:
            tebak = int(input("Tebak angkaku: "))
            usaha += 1

            if tebak < tebak_angka:
                print("Terlalu rendah! Coba lagi.")
            elif tebak > tebak_angka:
                print("Terlalu tinggi! Coba lagi.")
            else:
                print(f"Selamat! benar dengan {usaha} percobaan.")
                break
        except KeyError:
            print("Input salah. Masukkan angka yang benar.")

def new_func():
    usaha = 0
    return usaha

if __name__ == "__main__":
    main()
