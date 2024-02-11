from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Server
from .serializer import ServerSerializer

class ServerListViewSet(viewsets.ViewSet):
    
    queryset = Server.objects.all()

    def list(self, request):
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == 'true' 
        by_member_id = request.query_params.get("by_member_id") 
        print(by_user)

        if category:
            self.queryset = self.queryset.filter(category__name=category)

        if by_user:
            user_id = request.user.id
            self.queryset = self.queryset.filter(member=user_id)

        if by_member_id:
            user_id = request.user.id
            self.queryset = self.queryset.filter(member=by_member_id)

        if qty:
            self.queryset = self.queryset[:int(qty)]



        serializer = ServerSerializer(self.queryset, many=True)

        return Response(serializer.data) 