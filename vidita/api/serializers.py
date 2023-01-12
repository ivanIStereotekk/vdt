from rest_framework import serializers


from .models import User_Model, Picture_Model


class User_Serializer(serializers.ModelSerializer):
    on_pictures = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Picture_Model.objects.all()
    )

    class Meta:
        model = User_Model
        fields = '__all__'
        depth = 5


class Picture_Serializer(serializers.ModelSerializer):
    uploaded_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=User_Model.objects.all()
    )
    tagged_people = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User_Model.objects.all()
    )

    class Meta:
        model = Picture_Model
        fields = "__all__"
        depth = 5
