from rest_framework import serializers
from . import models
import json

class Numbo_textSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Numbo_text
        fields = '__all__'

    # def create(self, validated_data):
    #     first = validated_data['first']
    #     second = validated_data['second']
    #     third = validated_data['third']
    #     fourth = validated_data['fourth']
    #     fifth = validated_data['fifth']
    #     data1 = {'data': [{
    #         'first': first,
    #         'second': second,
    #         'third': third,
    #         'fourth': fourth,
    #         'fifth': fifth
    #     }]}
    #     data2 = json.dumps(data1)
    #     with open('my_data.json', 'w')as file:
    #         file.write(data2)
    #     file.close()
    #     obj = models.Numbo_text.objects.crea
    #     te(**validated_data)
    #     return obj



