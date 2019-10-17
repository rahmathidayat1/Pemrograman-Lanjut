import satuankuantitas

def main():
	
	print ("Konversi kuantitas dari lusin ke buah")
	a = int(input("Masukkan Nilai lusin: "))
	
	hasil = satuankuantitas.lusinkebuah (a)
	print ("Hasil konversi: ", hasil, "buah")
	
	print ("\nKonversi kuantitas dari gros ke lusin")
	b = int(input("Masukkan Nilai gros: "))
	
	hasil1 = satuankuantitas.groskelusin (b)
	print ("Hasil konversi: ", hasil1, "lusin")
	
	print ("\nKonversi kuantitas dari gros ke buah")
	c = int(input("Masukkan Nilai gros: "))
	
	hasil2 = satuankuantitas.groskebuah (c)
	print ("Hasil konversi: ", hasil2, "buah")
	
if __name__ == "__main__":
	main()

