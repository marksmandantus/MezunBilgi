from rest_framework import serializers
from base.models import Person, University, Event, Graduate
import datetime


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        read_only_fields = ('id',)

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'
        read_only_fields = ('id',)

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('id',)

class GraduateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graduate
        fields = '__all__'
        read_only_fields = ('id',)




# STANDART SERIALIZERS
class PersonDefaultSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ad = serializers.CharField()
    username = serializers.CharField()
    soyad = serializers.CharField()
    email = serializers.CharField()
    tc_kimlik_no = serializers.CharField()
    telefon = serializers.CharField()
    adres = serializers.CharField()
    cinsiyet = serializers.CharField()
    dogum_tarihi = serializers.DateField()
    universite_adi = serializers.CharField()
    website = serializers.CharField()
    facebook = serializers.CharField()
    twitter = serializers.CharField()
    instagram = serializers.CharField()
    linkedin = serializers.CharField()
    github = serializers.CharField()

    def create(self, validated_data):
        return Person.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.ad = validated_data.get('ad', instance.ad)
        instance.username = validated_data.get('username', instance.username)
        instance.soyad = validated_data.get('soyad', instance.soyad)
        instance.email = validated_data.get('email', instance.email)
        instance.tc_kimlik_no = validated_data.get('tc_kimlik_no', instance.tc_kimlik_no)
        instance.telefon = validated_data.get('telefon', instance.telefon)
        instance.adres = validated_data.get('adres', instance.adres)
        instance.cinsiyet = validated_data.get('cinsiyet', instance.cinsiyet)
        instance.dogum_tarihi = validated_data.get('dogum_tarihi', instance.dogum_tarihi)
        instance.universite_adi = validated_data.get('universite_adi', instance.universite_adi)
        instance.website = validated_data.get('website', instance.website)
        instance.facebook = validated_data.get('facebook', instance.facebook)
        instance.twitter = validated_data.get('twitter', instance.twitter)
        instance.instagram = validated_data.get('instagram', instance.instagram)
        instance.linkedin = validated_data.get('linkedin', instance.linkedin)
        instance.github = validated_data.get('github', instance.github)
        instance.save()
        return instance
    
    def validate_ad(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Ad alanı en az 2 karakter olmalıdır.")
        return value
    
    def validate_soyad(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Soyad alanı en az 2 karakter olmalıdır.")
        return value
    
    def validate_tc_kimlik_no(self, value):
        if len(value) != 11:
            raise serializers.ValidationError("Tc Kimlik No alanı 11 karakter olmalıdır.")
        return value
    
    def validate_telefon(self, value):
        if len(value) != 10:
            raise serializers.ValidationError("Telefon alanı 10 karakter olmalıdır.")
        return value
    
    def validate_cinsiyet(self, value):
        if value not in ['E', 'K']:
            raise serializers.ValidationError("Cinsiyet alanı E veya K olmalıdır.")
        return value
    
    def validate_dogum_tarihi(self, value):
        if value > datetime.date.today():
            raise serializers.ValidationError("Doğum Tarihi bugünden büyük olamaz.")
        return value
    
    def validate_website(self, value):
        if not value.startswith('http'):
            raise serializers.ValidationError("Website alanı http ile başlamalıdır.")
        return value
    
    def validate(self, attrs):
        ad = attrs.get('ad')
        soyad = attrs.get('soyad')
        
        if ad == soyad:
            raise serializers.ValidationError("Ad ve Soyad alanları aynı olamaz.")
        
        return attrs

    


