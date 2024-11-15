def calculate_discount(total_belanja,keanggotaan):
    if keanggotaan == 'gold':
        diskon = 0.15
    elif keanggotaan == 'silver':
        diskon = 0.10
    elif keanggotaan == 'bronze':
        diskon = 0.05
    else:
        diskon = 0.0
    
    if total_belanja > 1000000:
        diskon += 0.05

    total_diskon = total_belanja * diskon
    harga_setelah_diskon = total_belanja - total_diskon
    return harga_setelah_diskon


total_belanja = int(input("Masukkan total belanja: "))
keanggotaan = input("Masukkan jenis keanggotaan (Gold/Silver/Bronze/Tidak ada): ").lower()

harga_setelah_diskon = calculate_discount(total_belanja,keanggotaan)
print(f"Harga setelah diskon: {harga_setelah_diskon}")