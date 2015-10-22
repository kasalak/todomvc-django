from rest_framework import serializers

class TodoSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Todo
