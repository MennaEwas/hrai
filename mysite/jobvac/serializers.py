from rest_framework import serializers
from jobvac.models import JobModel

# class JobSerializer(serializers.Serializer):
#     Announcement_id = serializers.CharField(max_length=100)
#     Company_id = serializers.CharField(max_length=100)
#     Creator = serializers.CharField(max_length=100)
#     description = serializers.CharField(max_length=200)
#     is_published = serializers.BooleanField(default=False)
#     is_remote = serializers.BooleanField(default=False)
#     max_recommend = serializers.IntegerField()
#     position_name = serializers.CharField(max_length=100)
#     status = serializers.CharField(max_length=50)

#     def create(self, validated_data):
#         return JobModel.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.Announcement_id = validated_data.get('Announcement_id', instance.Announcement_id)
#         instance.Company_id = validated_data.get('Company_id', instance.Company_id)
#         instance.Creator = validated_data.get('Creator', instance.Creator)
#         instance.description = validated_data.get('description', instance.description)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
#         instance.is_remote = validated_data.get('is_remote', instance.is_remote)
#         instance.max_recommend = validated_data.get('max_recommend', instance.max_recommend)
#         instance.position_name = validated_data.get('position_name', instance.position_name)
#         instance.status = validated_data.get('status', instance.status)

#         instance.save()
#         return instance

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobModel
        fields = ['Announcement_id',
                    'Company_id',
                    'Creator',
                    'description',
                    'is_published',
                    'is_remote',
                    'max_recommend',
                    'position_name',
                    'status']
