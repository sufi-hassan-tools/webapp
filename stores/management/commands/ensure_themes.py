from django.core.management.base import BaseCommand
from stores.models import Theme

class Command(BaseCommand):
    help = 'Ensures that all theme templates are registered in the database'

    def handle(self, *args, **options):
        # Mini Shop Theme
        mini_shop, created = Theme.objects.get_or_create(
            name='Mini Shop',
            defaults={
                'template_dir': 'mini_shop',
                'description': 'A modern, clean, and responsive e-commerce theme with a focus on product presentation.',
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Successfully created theme: {mini_shop.name}'))
        else:
            self.stdout.write(f'Theme already exists: {mini_shop.name}')

        # EShopper Theme
        eshopper, created = Theme.objects.get_or_create(
            name='EShopper',
            defaults={
                'template_dir': 'eshopper',
                'description': 'A feature-rich e-commerce theme with a clean and professional design.',
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Successfully created theme: {eshopper.name}'))
        else:
            self.stdout.write(f'Theme already exists: {eshopper.name}')

        self.stdout.write(self.style.SUCCESS('All themes have been registered successfully')) 