#fungsi fibonaci
def fibonaci(n):
    if n < 0:
        print("masukkan angka positif")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)

n = int(input("masukkan bilangan: "))
print(f"deret fibonaci ke {n} adalah",fibonaci(n))