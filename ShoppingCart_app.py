'''
kelas ini ditunjukan untuk mengidentifikasi barang yang akan dibeli oleh user dengan nama dan harga
barang yang user akan beli. Fungsi init dipakai untuk men-dictionarykan nama dan harga dan fungsi str 
untuk memberi tahu bahwa code tersebut adalah string
'''
class CartItem:    
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price
    
    def __str__(self):
        return f'{self.item_name},{self.item_price}'
        
'''
kelas ini ditunjukan sebagai proses yang dilalui saat user meng-klik salah satu opsi menu dibawah. 
cart berguna untuk menyimpan barang, add_item berfungsi untuk menambahkan barang dengan (added_item),
del_item berfungsi untuk menghapus barang, show_item untuk melihat barang, dan total_item untuk melihat
harga total barang.
'''
class ShoppingCart:
    def __init__(self):
        self.cart = [] # dimana semua belanjaan user akan disimpan
    
    def add_item(self, added):
        self.cart.append(added) # memasukan barang ke cart
    

    def del_item(self, delete):
        for item in self.cart:
            if delete == item.item_name: #item.item_name untuk mengecek semua nama
                self.cart.remove(item)
                print(f'{delete} sudah berhasil dibuang')
                break
            else:
                print('barang tidak ditemukan, silahkan coba lagi')
               
    def show_item(self):
        if len(self.cart) != 0: #mengecek jika keranjang tidak kosong
            print('Barang di keranjang:')
            n = 0 #untuk membuat nomor untuk list (1 untuk list di posisi 1 dan seterusnya)
            for item in self.cart:
                n += 1 #n+1 untuk menambah penomoran
                print(f'{n}. {item.item_name} - Rp {item.item_price}') 
        else: #pesan jika keranjang kosong saat melihat keranjang
            print("keranjang masih kosong, silahkan masukan barang menggunakan menu '1'")
            
    def total_item(self):
        if len(self.cart) != 0:
            total = 0 #total 0 karena merupakan state awal total
            for item in self.cart:
                total += item.item_price
            print(f'total belanja: Rp {total}')
            return total
        else: #pesan jika keranjang kosong saat ingin menghitung total harga
            print("keranjang masih kosong, silahkan masukan barang menggunakan menu '1'")


        '''
        fungsi ini berfungsi sebagai tampilan menu yang akan berinteraksi dengan user. disini user dapat memilih
        opsi 1-5 dimana mereka dapat menjalankan fungsi yang tertera diatas. jika user sudah selesai maka mereka
        bisa memilih opsi '5' untuk menyelesaikan program
        '''
    def main(self):
        while True:

            print('''
            
            ==================================================
            Selamat Datang di Keranjang Belanja Toko Makmur!      
            
            Menu :
            1. menambah barang
            2. hapus barang
            3. tampilkan barang di keranjang
            4. lihat total belanja
            5. exit
            ===================================================
            ''')

            Opsi = input('silahkan pilih menu yang diinginkan (1-5)')

            if Opsi == '1':
                barang = input('Masukan nama barang:')
                harga = int(input('Masukan harga:'))
                item_add = CartItem(barang, harga) #barang di list ke cartitem
                shopping_cart.add_item(item_add)
                print(f'{barang} berhasil dimasukan ke keranjang')

            elif Opsi == '2':
                if len(self.cart) == 0: #jika barang di cart kosong
                    print('keranjang masih kosong silahkan masukan barang terlebih dahulu')
                else:
                    delete_item = input('masukan nama barang yang ingin dihapus: ')
                    shopping_cart.del_item(delete_item)
                
            elif Opsi == '3':
                shopping_cart.show_item()
                
            elif Opsi == '4':
                shopping_cart.total_item()
                
            elif Opsi == '5':
                print(f'Sampai Jumpa! Terima kasih sudah belanja di Toko Makmur.')
                break

            else: #jika user memilih opsi selain yang tertera di menu
                print(f'pilihannya salah. silahkan coba lagi')


'''
kode ini berfungsi untuk mengeksport file ke .py test
'''
if __name__ == '__main__':
    shopping_cart = ShoppingCart()
    shopping_cart.main()







