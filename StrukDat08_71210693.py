class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan

    def getNamaPelanggan(self):
        return self._namaPelanggan
    
    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru
        

class Kasir:
    DEFAULT_CAPACITY = 3 #isi sesuai dengan ketentuan soal
    def __init__(self): #konstruktor
        self._data = []
       
    def __len__(self): #mengembalikan ukuran Queue
        return len(self._data)

    def is_empty(self): #mengecek apakah Queue kosong
        return self.__len__() == 0

    def dequeue(self): #menghapus data paling depan (front)     
        data = self._data[0]
        self._data.remove(data)
        print(f"### Pelanggan {NodePelanggan.getNamaPelanggan(data)} Selesai Membayar ###")
        print()
        return data

    def enqueue(self, namaPelanggan): #menambah data ke list
        new = NodePelanggan(namaPelanggan)
        if self.__len__() >= self.DEFAULT_CAPACITY:
            self.resize()
        self._data.append(new)

    def resize(self): #mengubah ukuran queue pada list
        self.DEFAULT_CAPACITY = self.DEFAULT_CAPACITY*2
        print("### Melakukan Resize ###")
        print()

    def printAll(self): #menampilkan daftar pelanggan dalam sebuah kasir
        print("=== Kasir ===")
        for i in range(0, self.DEFAULT_CAPACITY):
            if i >= self.__len__():
                print(f"{i+1}. Kosong")
            else:
                print(f"{i+1}.", NodePelanggan.getNamaPelanggan(self._data[i]))
        print()

# test case program
tempatKasir = Kasir()
tempatKasir.enqueue("Haniif")
tempatKasir.enqueue("Sindu")
tempatKasir.enqueue("Dedi")
tempatKasir.printAll()

tempatKasir.enqueue("Beatrix")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

tempatKasir.enqueue("Shalom")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

