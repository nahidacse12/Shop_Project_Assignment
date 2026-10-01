from decimal import Decimal
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product
class ProductAPITests(APITestCase):
    def setUp(self):
        self.user=User.objects.create_user(username='testuser',password='testpass123')
        self.token=Token.objects.create(user=self.user)
        self.url='/api/products/'
    def auth(self): self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
    def test_get_public(self):
        Product.objects.create(name='Notebook',description='100 pages',price=Decimal('120.00'),stock=25)
        r=self.client.get(self.url); self.assertEqual(r.status_code,status.HTTP_200_OK)
    def test_create_authenticated(self):
        self.auth(); r=self.client.post(self.url,{'name':'Notebook','description':'100 pages','price':'120.00','stock':25},format='json')
        self.assertEqual(r.status_code,status.HTTP_201_CREATED)
    def test_create_without_token_denied(self):
        r=self.client.post(self.url,{'name':'Notebook','description':'100 pages','price':'120.00','stock':25},format='json')
        self.assertEqual(r.status_code,status.HTTP_401_UNAUTHORIZED)
    def test_empty_name(self):
        self.auth(); r=self.client.post(self.url,{'name':'','description':'x','price':'120.00','stock':25},format='json')
        self.assertEqual(r.status_code,status.HTTP_400_BAD_REQUEST)
    def test_zero_price(self):
        self.auth(); r=self.client.post(self.url,{'name':'Notebook','description':'x','price':'0.00','stock':25},format='json')
        self.assertEqual(r.status_code,status.HTTP_400_BAD_REQUEST)
    def test_negative_stock(self):
        self.auth(); r=self.client.post(self.url,{'name':'Notebook','description':'x','price':'120.00','stock':-5},format='json')
        self.assertEqual(r.status_code,status.HTTP_400_BAD_REQUEST)
    def test_page_two_contains_sixth(self):
        self.auth()
        for i in range(6):
            r=self.client.post(self.url,{'name':f'Product {i+1}','description':'x','price':'10.00','stock':10},format='json')
            self.assertEqual(r.status_code,status.HTTP_201_CREATED)
        r=self.client.get(self.url+'?page=2'); self.assertEqual(r.status_code,status.HTTP_200_OK)
        self.assertEqual(r.data['results'][0]['name'],'Product 6')
