#fungsi fibonacci
def faktorial(n):
    if n < 0:
        print("masukkan angka positif")
    elif n == 0:
        return 1
    else:
        faktorial = 1
        for i in range(1,n+1):
            faktorial *= i
        return faktorial

n = int(input("masukkan bilangan: "))
print(f"hasil dari {n}! adalah", faktorial(n))
