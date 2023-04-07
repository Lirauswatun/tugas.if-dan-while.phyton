#program menghitung nilai mahasiswa dari yang terbesar ke yang terkecil
print ("------menghitung hasil ujian mahasiswa-------")
nama = input ("masukkan nama mahasiswa: ")
nim =input ("masukkan nim mahasiswa: ")
mk = input ("masukkan mata kuliah hari ini: ")
nilai =int(input ("masukan nilai ujian mahasiswa: "))

if (nilai >=90) and (nilai >=95) :
    grade = "A+ (lulus)"
elif (nilai >=70) and (nilai >=80) :
    grade = "A (lulus)"
elif (nilai >=50) and (nilai >=65) :
    grade = "B (lulus)"
elif (nilai >=35) and (nilai >=40) :
    grade = "C (tidak lulus)"
elif (nilai >=20) and (nilai >=25) :
    grade = "D (tidak lulus)"
else :
    grade = "E (TIDAK LULUS = DROUT UOT)"


print("--------------------------------")
print("nama mahasiswa: ", nama)
print("nim mahasiswa: ", nim)
print("mata kuliah: ", mk)
print("hasil dari nilai ujian mahasiswa", "adalah = ", grade)
