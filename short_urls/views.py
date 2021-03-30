from django.http import JsonResponse, HttpResponseRedirect
from django.utils.crypto import get_random_string
from rest_framework import serializers, mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.serializers import Serializer

from myapp.settings import BASE_URL
from short_urls.models import ShortUrl


class ShortUrlSerializer(serializers.ModelSerializer):
    original_url = serializers.CharField(required=True)

    def validate_original_url(self, value):
        if not value.startswith(BASE_URL, 0):
            raise serializers.ValidationError(f'Original link should start with: {BASE_URL}')
        return value

    class Meta:
        model = ShortUrl
        fields = ['original_url', 'short_url']


class ShortUrlViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ShortUrlSerializer

    def create(self, request, *args, **kwargs):
        ser: Serializer = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)

        original_path = request.data['original_url'].split(BASE_URL)[1]
        slug = get_random_string(length=9)

        short_url_model = ShortUrl.objects.create(original_path=original_path, slug=slug)
        short_url_model.save()

        serializer = ShortUrlSerializer(instance=short_url_model)
        return JsonResponse(serializer.data)


def redirect_from_short_link(request, slug: str):
    su: ShortUrl = get_object_or_404(ShortUrl.objects.all(), slug=slug)
    url = BASE_URL + su.original_path
    return HttpResponseRedirect(url)
