from rest_framework import serializers
from .models import PerevalAdd, Coord, Users, Level, Images
from drf_writable_nested import WritableNestedModelSerializer


class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    data = serializers.URLField()

    class Meta:
        model = Images
        fields = ['data', 'title']


class PerevalSerializer(WritableNestedModelSerializer):
    user_id = UsersSerializer()
    coords_id = CoordSerializer()
    level_diff = LevelSerializer(allow_null=True)
    image = ImageSerializer(many=True)

    class Meta:
        model = PerevalAdd
        fields = ['id', 'user_id', 'coords_id', 'level_diff', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'image', 'status']   #'id', 'images', 'user', 'coords', 'level', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time'

    def validate(self, data):
        if self.instance is not None:
            user_instance = self.instance.user_id
            user_data = data.get('user_id')
            valid_user_fields = [
                user_instance.email != user_data['email'],
                user_instance.full_name != user_data['full_name'],
                user_instance.phone != user_data['phone']
            ]
            if user_data and any(valid_user_fields):
                raise serializers.ValidationError({'cant be changed'})
        return data
