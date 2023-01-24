import time

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
      """
      Decorator untuk mendapatkan lama waktu eksekusi kode dengan format dua angka dibelakang koma
      """
      start_time = time.time()
      result = self.func(*args, **kwargs)
      end_time = time.time()
      print(f"Time taken : {(end_time - start_time):.2f} seconds")
      return result

def main(nama, umur):
  print(nama, umur)


