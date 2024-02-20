from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from django.db.models import Count
from .models import Server
from .serializer import ServerSerializer

class ServerListViewSet(viewsets.ViewSet):
    
    queryset = Server.objects.all()

    def list(self, request):
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == 'true' 
        by_member_id = request.query_params.get("by_member_id") 
        # print(by_user)
        with_num_members = request.query_params.get("with_num_members") 

        if category:
            self.queryset = self.queryset.filter(category__name=category)

        if by_user:
            user_id = request.user.id
            self.queryset = self.queryset.filter(member=user_id)

        if by_member_id:
            user_id = request.user.id
            self.queryset = self.queryset.filter(member=by_member_id)

        if with_num_members:
            self.queryset = self.queryset.annotate(num_members=Count("member"))

        if qty:
            self.queryset = self.queryset[:int(qty)]


        serializer = ServerSerializer(self.queryset, many=True, context={"num_members":with_num_members})

        return Response(serializer.data) 