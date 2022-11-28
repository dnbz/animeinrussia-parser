#!/usr/bin/env python3
from .models import Show
from rest_framework import serializers

class ShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Show
        fields = [
            "created_at",
            "source_url",
            "description",
            "title_orig",
            "title_ru",
            "image_url",
            "pub_date",
        ]
