from rest_framework import serializers

from work_with_users_db.models import User_db, Castomer


class User_serializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    secondname= serializers.CharField(max_length=120)

    def create(self, validated_data):
        return User_db.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.secondname = validated_data.get('secondname', instance.secondname)

        instance.save()
        return instance

class CastomerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)

    def create(self, validated_data):
        return Castomer.objects.create(**validated_data)
