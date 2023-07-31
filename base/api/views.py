from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Person, University, Event
from base.api.serializers import PersonSerializer, UniversitySerializer, EventSerializer

#class views
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class PersonListCreateAPIView(APIView):
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PersonDetailAPIView(APIView):
    def get_object(self, pk):
        person = get_object_or_404(Person, pk=pk)
        return person
    
    def get(self, request, pk):
        person = self.get_object(pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    
    def put(self, request, pk):
        person = self.get_object(pk)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        person = self.get_object(pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class UniversityListCreateAPIView(APIView):
    def get(self, request):
        universities = University.objects.all()
        serializer = UniversitySerializer(universities, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UniversitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UniversityDetailAPIView(APIView):
    def get_object(self, pk):
        university = get_object_or_404(University, pk=pk)
        return university
    
    def get(self, request, pk):
        university = self.get_object(pk)
        serializer = UniversitySerializer(university)
        return Response(serializer.data)
    
    def put(self, request, pk):
        university = self.get_object(pk)
        serializer = UniversitySerializer(university, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        university = self.get_object(pk)
        university.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class EventListCreateAPIView(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EventDetailAPIView(APIView):
    def get_object(self, pk):
        event = get_object_or_404(Event, pk=pk)
        return event
    
    def get(self, request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)
    
    def put(self, request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




### FUNCTION BASED VIEWS ###
# @api_view(['GET', 'POST'])
# def person_list_create_api_view(request):
#     if request.method == 'GET':
#         persons = Person.objects.all()
#         serializer = PersonSerializer(persons, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = PersonSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# @api_view(['GET', 'PUT', 'DELETE'])
# def person_detail_api_view(request, pk):
#     try:
#         person = Person.objects.get(pk=pk)
#     except Person.DoesNotExist:
#         return Response({'error': {
#             'code': 404,
#             'message': 'Person not found!'
#         }}, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = PersonSerializer(person)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = PersonSerializer(person, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         person.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)