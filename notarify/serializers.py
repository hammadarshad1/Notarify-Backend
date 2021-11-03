from rest_framework import serializers


class PDFSerializer(serializers.Serializer):
    name = serializers.CharField()
    dob = serializers.CharField()
    country = serializers.CharField()
    vat_number = serializers.CharField()
    address = serializers.CharField()
    city = serializers.CharField()
    doc = serializers.CharField()
    released_date = serializers.CharField()
    expiry_date = serializers.CharField()
    capacity_resistance = serializers.CharField()
    commerce_registeration_number = serializers.CharField()
    office_add = serializers.CharField()
    office_town = serializers.CharField()
    office_state = serializers.CharField()

    class Meta:
        fields = ('__all__', )
