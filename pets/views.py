from django.forms import model_to_dict
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
import groups
from groups.models import Group
from pets.serializers import PetSerializer
from traits.models import Trait
from .models import Pet
from rest_framework.pagination import PageNumberPagination
import ipdb


# Create your views here.
class PetsView(APIView, PageNumberPagination):
    def get(self, req):
        pets = Pet.objects.all()
        req_qp = req.query_params
        if req_qp:
            petsfiltred = Pet.objects.filter(traits__in=req_qp["trait"])
            print(req_qp["trait"])
            print(petsfiltred)
        pages = self.paginate_queryset(pets, req)
        serializer = PetSerializer(pages, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, req):
        serializer = PetSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)

        group = serializer.validated_data.pop("group")
        traits = serializer.validated_data.pop("traits")

        try:
            find_group = Group.objects.get(
                scientific_name__iexact=group["scientific_name"]
            )
        except Group.DoesNotExist:
            find_group = Group.objects.create(**group)

        pet_created = Pet.objects.create(**serializer.validated_data, group=find_group)
        for trait in traits:
            try:
                trait_find = Trait.objects.get(name__iexact=trait["name"])
                pet_created.traits.add(trait_find)
            except Trait.DoesNotExist:
                trait_find = Trait.objects.create(**trait)
                pet_created.traits.add(trait_find)

        data_response = PetSerializer(pet_created)
        return Response(data_response.data, 201)


class PetsDetailsView(APIView):
    def get(self, req, pet_id):
        print(pet_id)
        user = get_object_or_404(Pet, id=pet_id)
        serializer = PetSerializer(user)
        return Response(serializer.data)

    def patch(self, req, pet_id):
        print(pet_id)
        pet = get_object_or_404(Pet, id=pet_id)
        serializer = PetSerializer(pet, data=req.data, partial=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, req, pet_id):
        pet = get_object_or_404(Pet, id=pet_id)
        pet.delete()
        return Response(status=204)
