from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.management import call_command


# Create your tests here.
class ProductTest(APITestCase):
    def test_product_list(self):
        call_command("init_products")

        url = "/api/product/all/"
        result = self.client.get(url)
        print("product", result.data)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result.data['result']), 3)

    def test_product_list_title_filter(self):
        call_command("init_products")

        url = "/api/product/all/"
        search_title = "iPhone 13"
        parameters = dict(
            title=search_title
        )
        result = self.client.get(url, params=parameters)
        print("!!! Product title", result.data)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['result'][0]['title'], search_title)

    def test_product_list_price_filter(self):
        call_command("init_products")

        url = "/api/product/all/"
        search_price = "{:.2f}".format(900.00)
        parameters = dict(
            price=search_price
        )
        result = self.client.get(url, params=parameters)
        print("! price >", result.data)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['result'][0]['price'], search_price)

    def test_product_list_old_price_filter(self):
        call_command("init_products")

        url = "/api/product/all/"
        search_old_price = "{:.2f}".format(1000.00)
        parameters = dict(
            old_price=search_old_price
        )
        result = self.client.get(url, params=parameters)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['result'][0]['old_price'], search_old_price)

