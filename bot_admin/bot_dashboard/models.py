from django.db import models


class PriceList(models.Model):
    list_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=100)
    PRICE_TYPE = (('О','Обычный'),('Л','Ликвидационный'))
    product_type = models.CharField(max_length=1, choices=PRICE_TYPE)
    upload_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False, verbose_name='Товар активен')
    actions = None #добавить УДАЛИТЬ\РЕДАКТИРОВАТЬ

    class Meta:
        db_table = 'price_lists'


class Promotion(models.Model):
    promo_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=100)
    content_type = models.CharField(max_length=200)
    priority = models.CharField(max_length=100)
    status = models.BooleanField(default=False, verbose_name='Акция активна')
    promotion_start = models.DateTimeField(null=True, blank=True)
    promotion_end = models.DateTimeField(null=True, blank=True)
    actions = None # добавить УДАЛИТЬ\РЕДАКТИРОВАТЬ


    @property
    def is_promotion_active(self):
        if not self.promotion_start or not self.promotion_end:
            return False

        from django.utils import timezone
        now = timezone.now()
        return self.promotion_start <= now <= self.promotion_end

    class Meta:
        db_table = 'promotions'


class BotSettings(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.key