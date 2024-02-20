from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from django.db.models import Count
from .models import Server
from .serializer import ServerSerializer
from .schema import server_list_docs
class ServerListViewSet(viewsets.ViewSet):
    
    queryset = Server.objects.all()

    @server_list_docs
    def list(self, request):
        """
        Retrieves a list of items based on  specified query parameters.

        Args:
            request (Request): The request  object containing query parameters.

        Returns:
            QuerySet: A filtered queryset of    items based on the provided    parameters.

        Query Parameters:
            category (str): Filter items by     category name.
            qty (int): Limit the number of  items returned.
            by_user (bool): If True, filter     items by the current user.
            by_member_id (int): Filter items by     a specific member's ID.
            with_num_members (bool): If True,   annotate the queryset with the    number of members.

        Note:
            - The 'by_user' parameter filters items by the currently  authenticated user.
            - The 'by_member_id' parameter  filters items by the specified  member's ID.
            - The 'with_num_members' parameter annotates the queryset with the  number of members associated with each item.
            - If 'qty' is provided, the number  of returned items is limited accordingly.
        """
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