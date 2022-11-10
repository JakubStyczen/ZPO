import unittest
from collections import Counter
 
from servers import Server, ListServer, Product, Client, MapServer, TooManyProductsFoundError
 
server_types = (ListServer, MapServer)
 
 
class ProductTest(unittest.TestCase):
 
    def test_init_prodcut_valid(self):
        p1 = Product('acd123', 5.0)
        self.assertEqual(p1.name, 'acd123')
        self.assertEqual(p1.price, 5.0)
        
    def test_init_prodcut_without_letter(self):
        self.assertRaises(ValueError, Product, '123', 5.0)
        
    def test_init_prodcut_without_number(self):
        self.assertRaises(ValueError, Product, 'a', 5.0)
    
    def test_init_prodcut_too_many_numbers(self):
        self.assertRaises(ValueError, Product, 'aaa1234', 5.0)
    
 
class ServerTest(unittest.TestCase):
 
    def test_get_entries_returns_proper_entries(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(2)
            self.assertEqual(Counter([products[2], products[1]]), Counter(entries))
    
    def test_get_entried_raise_exception(self):
        products = [Product('PY234', 2), Product('PB234', 2), Product('PP234', 2), Product('PC234', 2)]
        for server_type in server_types:
            server = server_type(products)
            self.assertRaises(TooManyProductsFoundError, server.get_entries, 2)
        
class ClientTest(unittest.TestCase):
    def test_total_price_for_normal_execution(self):
        products = [Product('PP234', 2), Product('PP235', 3)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(5.0, client.get_total_price(2))
            
    def test_total_price_for_empty_entries_execution(self):
        products = [Product('PP234', 2), Product('PP235', 3)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(None, client.get_total_price())
    
    def test_total_price_for_raise_exception(self):
        products = [Product('PP234', 2) for i in range(Server.n_max_returned_entries + 1)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(None, client.get_total_price())
            
    
 
 
if __name__ == '__main__':
    unittest.main()