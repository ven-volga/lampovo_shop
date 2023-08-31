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
        return dict(self.PRODUCTS_CATEGORY_CHOICES)[self.name]

    def get_absolut_url(self):
        return reverse('product_list_by_category', args=[self.slug])


class Product(models.Model):
    PRODUCT_AVAILABLE_CHOICES = [
        ('PTO', 'Production to order'),
        ('IS', 'In stock'),
        ('RTS', 'Ready to ship'),
    ]

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.CharField(max_length=100, db_index=True, unique=True)
    main_image = models.ImageField(upload_to=f'products/main_image/', blank=True)
    description = models.TextField(max_length=1500, blank=True)
    specifications = models.JSONField(blank=True, default=dict)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    availability = models.CharField(max_length=4, choices=PRODUCT_AVAILABLE_CHOICES, default='PTO')
    production_time = models.SmallIntegerField(blank=True, null=True, default=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_recommend = models.BooleanField(default=False)
    ordering = models.SmallIntegerField(default=1)

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])

    def get_availability_display(self):
        return dict(Product.PRODUCT_AVAILABLE_CHOICES)[self.availability]


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
