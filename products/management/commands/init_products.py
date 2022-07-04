from django.core.management import BaseCommand
from products.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Product.objects.create(
        #     title="iPhone 13",
        #     price=900,
        #     old_price=1000,
        #     quantity=10,
        #     description="test"
        # )
        products=[]
        products.append(
            dict(
                title="iPhone 13",
                price=900,
                old_price=1000,
                quantity=10,
                description="test"
            )
        )

        products.append(
            dict(
                title="iPhone 12",
                price=800,
                old_price=900,
                quantity=10,
                description="test2"
            )
        )

        products.append(
            dict(
                title="iPad Pro",
                price=600,
                old_price=700,
                quantity=12,
                description="test3"
            )
        )

        for product in products:
            Product.objects.get_or_create(**product)

        print("Data transfer completed")