print("## RESTAURANT STT ##")
print(" + Menu Makanan + ")
print(" 1. Mie Rebus | Rp. 4.000,- | 0.3 kalori ")
print(" 2. Sate Ayam | Rp. 12.000,- | 2.3 kalori")
print(" + Menu Minuman + ")
print(" 1. Es Teh | Rp. 3.000,- | 1.2 kalori")
print(" 2. Jus Mangga | Rp. 7.000,- | 1.9 kalori")
print("-------------------FORM PEMESANAN---------------------")
nama = input("Nama kamu : ")
makan = int(input("Mau makan apa hari ini ? (1/2) : "))
minum = int(input("Minumnya apa ? (1/2) : "))
print("------------------------------------------------------")
print("\n")
k_mie = 0.3
k_teh = 1.2
k_sate = 2.3
k_jus = 1.9
if makan & minum == 1:
    total = 4000 + 3000
    j_kalori = k_mie + k_teh
    print("-------------------STRUK PEMESANAN---------------------")
    print(" Nama pemesan :",nama,("\n"),"Menu yang dipesan : Mie Rebus & Es Teh",("\n"),"Total kalori :",j_kalori,("\n"),"Total harga :",total)
    print("-------------------------------------------------------")
elif makan & minum == 2:
    total = 12000 + 7000
    j_kalori = k_sate + k_jus
    print("-------------------STRUK PEMESANAN---------------------")
    print(" Nama pemesan :",nama,("\n"),"Menu yang dipesan : Sate Ayam & Jus Mangga",("\n"),"Total kalori :",j_kalori,("\n"),"Total harga :",total)
    print("-------------------------------------------------------")
elif makan == 1 and minum == 2:
    total = 4000 + 7000
    j_kalori = k_mie + k_jus
    print("-------------------STRUK PEMESANAN---------------------")
    print(" Nama pemesan :",nama,("\n"),"Menu yang dipesan : Mie Rebus & Jus Mangga",("\n"),"Total kalori :",j_kalori,("\n"),"Total harga :",total)
    print("-------------------------------------------------------")
elif makan == 2 and minum == 1:
    total = 12000 + 3000
    j_kalori = k_sate + k_teh
    print("-------------------STRUK PEMESANAN---------------------")
    print(" Nama pemesan :",nama,("\n"),"Menu yang dipesan : Sate Ayam & Es Teh",("\n"),"Total kalori :",j_kalori,("\n"),"Total harga :",total)
    print("-------------------------------------------------------")
else:
    print("Maaf pesanan tidak valid")
