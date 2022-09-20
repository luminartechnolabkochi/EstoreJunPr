from rest_framework import serializers

from api.models import Reviews
class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    author=serializers.CharField()
    price=serializers.IntegerField()
    publisher=serializers.CharField()
    qty=serializers.IntegerField()



        # fields=["name","author","price","publisher","qty"]

class ReviewSerializer(serializers.ModelSerializer):
    created_date=serializers.CharField(read_only=True)
    class Meta:
        model=Reviews
        fields="__all__"
        # exclude=("created_date",)
        # fields=["book","user","comment","rating"]