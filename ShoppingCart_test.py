'''
=============================================================
Graded Challenge 1 (test)

Nama : Achmad Abdillah Ghifari
Batch : BSD-006

Program ini dibuat untuk mengetes program yang dibuat sebelumnya. Program ini akan mengecek
dengan cara menambahkan, menghapus, dan mentotal barang yang telah dipilih. jika hasil dari tes
adalah 'ok', artinya program dapat berjalan dengan lancar
============================================================
'''

'''
kita mengimport unittest dan file app dari tugas sebelumnya menggunakan command ini 
'''
import unittest
from Ghifari_app import ShoppingCart, CartItem

'''
kelas ini berguna untuk mengetes fungsi dari tugas sebelumnya mulai dari menambahkan
menghapus, dan mentotal harga barang.
'''
class ShoppingCartTest(unittest.TestCase):
    def setUp(self): #menambahkan item ke cart untuk mengecek apakah cart berfungsi
        self.shopping = ShoppingCart()
        self.item1 = CartItem('jeruk', 200)
        self.item2 = CartItem('apel', 300)
        self.shopping.add_item(self.item1)
        self.shopping.add_item(self.item2)
        

    def test_add_item(self): #mengecek apakah item bisa dimasukan ke cart
        self.shopping = ShoppingCart()
        added_item = CartItem('anggur', 500)
        self.shopping.add_item(added_item)
        self.assertIn(added_item, self.shopping.cart) #mengecek jika value (anggur, 500) sudah ada di keranjang 

    def test_del_item(self): #mengecek apakah item bisa dihapus dari kart
        
        self.shopping = ShoppingCart()
        added_item2 = CartItem('apel', 200)
        self.shopping.add_item(added_item2) #memasukan item ke cart untuk dibuang
        self.shopping.del_item('apel') #membuang item dengan nama apple dari cart
        self.assertNotIn(added_item2, self.shopping.cart) #mengecek jika item apel tidak ditemukan di cart

    def test_total_item(self):

        self.shopping = ShoppingCart()
        added_item3 = CartItem('anggur', 200)
        added_item4 = CartItem('semangka', 300)
        self.shopping.add_item(added_item3) #memasukan item ke cart untuk ditotal
        self.shopping.add_item(added_item4) #memasukan item ke cart untuk ditotal
        self.assertEqual(self.shopping.total_item(), 500) #mengecek jika total harga dari cart adalah 500 (200+300)
        
'''
kode ini berfungsi untuk melakukan unittest dan tidak diganti
'''
if __name__ == "__main__":
    unittest.main()


