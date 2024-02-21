from django.shortcuts import redirect
from rest_framework.generics import DestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.pagination import LimitOffsetPagination

from .api.serializers import PostSerializer
from .models import Post


from rest_framework import filters


class PostView(ListAPIView, LimitOffsetPagination):
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "username",
    ]

    def get_queryset(self):
        if "search" in self.request.GET:
            if self.request.GET["search"]:
                queryset = Post.objects.filter(
                    **{self.search_fields[0]: self.request.GET["search"]}
                )
                return self.paginate_queryset(queryset)
        return self.paginate_queryset(Post.objects.all())

    def get(self, format=None):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        context = self.get_paginated_response(serializer.data)
        return context

    def post(self, request, format=None):
        if not request.data:
            return redirect("posts")

        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(serializer.data, status=400)


class DeletePostView(DestroyAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.filter(id=self.kwargs["pk"])
        return queryset

    def get(self, request, pk, format=None):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        if serializer.is_valid():
            if not serializer.data:
                return Response({"detail": "Not found."}, status=400)
            return Response(serializer.data, status=200)

    def destroy(self, request, pk, format=None):
        instance = self.get_object()
        if instance == True:
            return Response({"detail": "Not found."}, status=404)
        self.perform_destroy(instance)

        return Response()

    def patch(self, request, pk, format=None):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)
