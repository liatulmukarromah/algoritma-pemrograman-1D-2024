#cek palindrom
def cek_palindrom(kata):
    kata = kata [::-1]
    if kata == kata:
        print(f"kata {kata} adalah kata palindrom")
    else:
        print(f"kata {kata} bukan kata palindrom")
kata = input("masukkan kata yang akan dicek :")
cek_palindrom(kata)
