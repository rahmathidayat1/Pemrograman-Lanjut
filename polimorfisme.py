# mendefinisikan kelas BilanganBulat
class BilanganBulat(object):
   def __init__(self, nilai):
      if not isinstance(nilai, int):
         raise TypeError("Nilai harus bertipe bilangan bulat")
      self.nilai = nilai

 
   def __or__(self, objek):
      if isinstance(objek, int):
         return self.nilai | objek
      elif isinstance(objek, float):
         return float(self.nilai | objek)
      elif isinstance(objek, BilanganBulat):
         return self.nilai | objek.nilai
      else:
         raise TypeError("Objek harus bertipe numerik")

   # overload terhadap operator ==
   def __xor__(self, objek):
      if isinstance(objek, int):
         return self.nilai ^ objek
      elif isinstance(objek, float):
         return float(self.nilai) ^ objek
      elif isinstance(objek, BilanganBulat):
         return self.nilai ^ objek.nilai
      else:
         raise TypeError("Objek harus bertipe numerik")

def main():

   a = BilanganBulat(1)
   b = BilanganBulat(0)
   c = 1
   d = 0
   print("DATA")
   print("a = 1" "\nb = 0" "\nc =", c, "\nd =", d)
   print("\nhasil dari operasi or")
   print("a or b: ", a | b)
   print("b or d: ", b | d)
   print("\nhasil dari operasi xor")
   print("a xor c: ", a ^ c)
   print("a xor b: ", a ^ b)
if __name__ == "__main__":
   main()
