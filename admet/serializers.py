from rest_framework import serializers
from .models import Click


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        fields = self.context['request'].query_params.get('fields')
        if('group_by' in self.context['request'].query_params):
            fields += ','+ self.context['request'].query_params.get('group_by')
        if fields:
            ffields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(ffields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class CustomSerializer(DynamicFieldsModelSerializer, serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Click
        fields = ("date","channel","country","os","impressions","clicks","installs","spend","revenue","cpi");


    def to_representation(self, instance):
        original_representation = super().to_representation(instance)
        if(isinstance(instance,Click)):
            instance.save()
            return original_representation
        for ke in instance.keys():
            if(ke in original_representation):
                pass
            else:
                original_representation[ke] = instance[ke]
        return original_representation
