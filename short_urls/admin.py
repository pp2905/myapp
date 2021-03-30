from django.contrib import admin

from short_urls.models import ShortUrl


@admin.register(ShortUrl)
class ShortUrlAdmin(admin.ModelAdmin):
    list_display = ['original_url', 'short_url']
    readonly_fields = ['short_path', 'original_url', 'short_url']
    model = ShortUrl

    class Meta:
        fields = '__all__'
