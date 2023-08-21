from django.db import models
from django.urls import reverse


class Category(models.Model):
    PRODUCTS_CATEGORY_CHOICES = [
        ('new', 'New items'),
        ('amp', 'Amplifiers'),
        ('tt', 'Turntables'),
        ('riaa', 'Riaa-correctors'),
        ('cs', 'Channel selectors'),
        ('cb', 'Cables'),
    ]

    name = models.CharField(max_length=4, choices=PRODUCTS_CATEGORY_CHOICES, default='new', db_index=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('product_list_by_category', args=[self.slug])


class Product(models.Model):
    COLOR_CHOICES = [
        ('dw', 'Dark wood'),
        ('lw', 'Light wood'),
        ('nc', 'No color'),
    ]

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.CharField(max_length=100, db_index=True, unique=True)
    main_image = models.ImageField(upload_to=f'products/main_image/', blank=True)
    description = models.TextField(max_length=1500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    color = models.CharField(max_length=2, choices=COLOR_CHOICES, default='nc')
    customize = models.BooleanField(default=False)
    is_recommend = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Product image'
        verbose_name_plural = 'Product images'

    def image_upload_path(self, filename):
        return f'products/{self.product.slug}/{filename}'

    image = models.ImageField(upload_to=image_upload_path, blank=True)

    def get_absolute_path(self):
        return f'products/{self.product.slug}/'


