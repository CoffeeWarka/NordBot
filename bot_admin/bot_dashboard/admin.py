from django.contrib import admin
from .models import Promotion, PriceList, BotSettings

@admin.register(PriceList)
class PriceListAdmin(admin.ModelAdmin):
    list_display = ['list_id', 'name', 'product_type', 'upload_date', 'active', 'actions']
    search_fields = ['list_id', 'name', 'product_type']
    list_filter = ['product_type', 'upload_date', 'active']


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['promo_id', 'name', 'content_type', 'priority',
                    'status', 'promotion_start', 'promotion_end', 'actions']
    search_fields = ['promo_id', 'name', 'content_type']
    list_filter = ['status', 'promotion_start', 'promotion_end']


@admin.register(BotSettings)
class BotSettingsAdmin(admin.ModelAdmin):
    list_display = ['key', 'value', 'description']