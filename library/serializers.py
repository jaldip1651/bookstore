from rest_framework import serializers
from .models import Author, Publisher, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        publisher_data = validated_data.pop('publisher')
        author, created = Author.objects.get_or_create(**author_data)
        publisher, created = Publisher.objects.get_or_create(**publisher_data)
        book = Book.objects.create(author=author, publisher=publisher, **validated_data)
        return book

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author')
        publisher_data = validated_data.pop('publisher')

        author, created = Author.objects.get_or_create(**author_data)
        publisher, created = Publisher.objects.get_or_create(**publisher_data)

        instance.author = author
        instance.publisher = publisher
        instance.title = validated_data.get('title', instance.title)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.save()

        return instance
