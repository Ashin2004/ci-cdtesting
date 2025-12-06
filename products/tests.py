# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from .models import Product
#
# class ProductAPITests(APITestCase):
#     def setUp(self):
#         self.product_data = {
#             'name': 'Test Product',
#             'description': 'This is a test product.',
#             'price': 100.00,
#             'stock': 10
#         }
#         self.product = Product.objects.create(**self.product_data)
#         self.list_url = reverse('product-list')
#         self.detail_url = reverse('product-detail', args=[self.product.id])
#
#     def test_create_product(self):
#         """
#         Ensure we can create a new product object.
#         """
#         data = {
#             'name': 'New Product',
#             'description': 'Description for new product',
#             'price': 200.00,
#             'stock': 5
#         }
#         response = self.client.post(self.list_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Product.objects.count(), 2)
#         self.assertEqual(Product.objects.get(id=2).name, 'New Product')
#
#     def test_create_product_invalid(self):
#         """
#         Ensure we cannot create a product with invalid data.
#         """
#         data = {
#             'name': '',  # Invalid: empty name
#             'description': 'Description',
#             'price': 200.00,
#             'stock': 5
#         }
#         response = self.client.post(self.list_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(Product.objects.count(), 1)
#
#     def test_list_products(self):
#         """
#         Ensure we can list products.
#         """
#         response = self.client.get(self.list_url, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
#
#     def test_retrieve_product(self):
#         """
#         Ensure we can retrieve a specific product.
#         """
#         response = self.client.get(self.detail_url, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['name'], self.product_data['name'])
#
#     def test_update_product(self):
#         """
#         Ensure we can update a product.
#         """
#         data = {
#             'name': 'Updated Product',
#             'description': 'Updated description',
#             'price': 150.00,
#             'stock': 8
#         }
#         response = self.client.put(self.detail_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.product.refresh_from_db()
#         self.assertEqual(self.product.name, 'Updated Product')
#
#     def test_delete_product(self):
#         """
#         Ensure we can delete a product.
#         """
#         response = self.client.delete(self.detail_url, format='json')
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Product.objects.count(),0)





from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product

class SimpleAPITest(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test', description='Desc', price=10.0, stock=5
        )
        self.list_url = reverse('product-list')
        self.detail_url = reverse('product-detail', args=[self.product.id])

    def test_fetch_product(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test')

    def test_update_product(self):
        data = {'name': 'Updated', 'description': 'Desc', 'price': 10.0, 'stock': 5}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated')

    def test_delete_product(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(),0)
