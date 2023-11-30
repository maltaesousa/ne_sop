from ne_sop_api.models import (
    Entity,
    EntityType,
    Item,
    ItemType,
    ItemStatus,
    Event,
    EventType,
    Template,
    User,
)
from ne_sop_api.serializers import (
    EntitySerializer,
    EntityListSerializer,
    EntityTypeSerializer,
    ItemSerializer,
    ItemTypeSerializer,
    ItemStatusSerializer,
    EventSerializer,
    EventListSerializer,
    EventTypeSerializer,
    TemplateSerializer,
    UserSerializer,
)

from ne_sop_api.paginations import (
    CustomPagination,
)

from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from django.core.paginator import Paginator

# %% FILTERS -----------------------------------------------------------------------------------


""" class ItemFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method="my_custom_filter", label="Search")

    class Meta:
        model = Item
        fields = ["q"]

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(
            Q(loc__icontains=value)
            | Q(loc_mansioned__icontains=value)
            | Q(loc_country__icontains=value)
            | Q(loc_modern__icontains=value)
        )
 """


# %% Users
class UserViewSet(viewsets.ViewSet):
    """
    Users viewset
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        responses=UserSerializer,
        tags=["Users"],
    )
    def list(self, request):
        serializer = UserSerializer(self.queryset, many=True)
        return Response(serializer.data)


# %% Entities
class EntityTypeViewSet(viewsets.ViewSet):
    """
    Entity types viewset
    """

    queryset = EntityType.objects.all()
    serializer_class = EntityTypeSerializer

    @extend_schema(
        responses=EntityTypeSerializer,
        tags=["Entity type"],
    )
    def list(self, request):
        serializer = EntityTypeSerializer(self.queryset, many=True)
        return Response(serializer.data)


class EntityViewSet(viewsets.ViewSet):
    """
    Entities viewset
    """

    serializer_class = EntitySerializer
    search_fields = ["name", "email", "telephone"]

    # queryset = Entity.objects.all()
    # name = self.request.query_params.get("name")

    # queryset = Entity.objects.all()
    # queryset = queryset.filter(name__icontains=name)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Entity.objects.all()
        name = self.request.query_params.get("name")
        # type = self.request.query_params.get("type")
        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        # return super().get_queryset()  # queryset
        return queryset

    @extend_schema(
        request=EntitySerializer,
        responses={201: EntitySerializer},
        tags=["Entities"],
    )
    def list(self, request):
        filter = filters.SearchFilter()
        queryset = filter.filter_queryset(request, Entity.objects.all(), self)

        # queryset = Entity.objects.all()
        # name = request.query_params.get("name")
        name = request.GET.get("name", "")
        type = request.query_params.get("type")
        page = int(request.GET.get("page", "1"))
        size = int(request.GET.get("size", "10"))

        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        # if type # is not None:
        if type:
            queryset = queryset.filter(type__in=type.split(","))

        paginator = Paginator(queryset.order_by("id"), size)
        queryset = paginator.page(page)

        # paginator = Paginator(queryset, per_page=2)
        # page_object = paginator.get_page(page)
        # context = {"page_obj": page_object}

        serializer = EntityListSerializer(queryset, many=True)

        # queryset = self.filter_queryset(self.get_queryset())
        # page = self.paginate_queryset(queryset)
        # serializer = EntitySerializer(queryset, many=True)

        ## serializer = EntitySerializer(self.get_queryset(), many=True)

        # if page is not None:
        #    serializer = self.get_serializer(page, many=True)
        #    return self.get_paginated_response(serializer.data)

        # serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    @extend_schema(
        tags=["Entities"],
    )
    def create(self, request):
        serializer = EntitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"msg": "New entity created"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=["Entities"],
    )
    def retrieve(self, request, pk=None):
        queryset = Entity.objects.all()
        # entity = get_object_or_404(self.queryset, pk=pk)
        # entity = get_object_or_404(self.get_queryset(), pk=pk)
        entity = get_object_or_404(queryset, pk=pk)
        serializer = EntitySerializer(entity)
        return Response(serializer.data)

    @extend_schema(
        tags=["Entities"],
    )
    def update(self, request, pk=None):
        queryset = Entity.objects.all()
        # entity = get_object_or_404(self.queryset, pk=pk)
        # entity = get_object_or_404(self.get_queryset(), pk=pk)
        entity = get_object_or_404(queryset, pk=pk)
        serializer = EntitySerializer(entity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=["Entities"],
    )
    def destroy(self, request, pk=None):
        queryset = Entity.objects.all()
        entity = get_object_or_404(queryset, pk=pk)
        # entity = get_object_or_404(self.queryset, pk=pk)
        # entity = get_object_or_404(self.get_queryset, pk=pk)
        entity.delete()
        return Response({"msg": "Entity deleted"})


# %% Items
class ItemTypeViewSet(viewsets.ViewSet):
    """
    Item types viewset
    """

    queryset = ItemType.objects.all()
    serializer_class = ItemTypeSerializer

    @extend_schema(
        responses=ItemTypeSerializer,
        tags=["Item types"],
    )
    def list(self, request):
        serializer = ItemTypeSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ItemStatusViewSet(viewsets.ViewSet):
    """
    Item status viewset
    """

    queryset = ItemStatus.objects.all()
    serializer_class = ItemStatusSerializer

    @extend_schema(
        responses=ItemStatusSerializer,
        tags=["Item status"],
    )
    def list(self, request):
        serializer = ItemStatusSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ItemViewSet(viewsets.ViewSet):
    """
    Items viewset
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    search_fields = ["title", "number"]

    @extend_schema(
        responses=ItemSerializer,
        tags=["Items"],
    )
    def list(self, request):
        filter = filters.SearchFilter()
        queryset = filter.filter_queryset(request, Item.objects.all(), self)

        # queryset = Item.objects.all()
        # name = request.query_params.get("name")
        title = request.query_params.get("title", "")
        number = request.GET.get("number", "")
        page = int(request.GET.get("page", "1"))
        size = int(request.GET.get("size", "10"))

        if title is not None:
            queryset = queryset.filter(title__icontains=title)

        if number is not None:
            queryset = queryset.filter(number__icontains=number)

        paginator = Paginator(queryset.order_by("id"), size)
        queryset = paginator.page(page)

        # paginator = Paginator(queryset, per_page=2)
        # page_object = paginator.get_page(page)
        # context = {"page_obj": page_object}

        serializer = ItemSerializer(queryset, many=True)
        # serializer = ItemSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        tags=["Items"],
    )
    def create(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Item created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=["Items"],
    )
    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    @extend_schema(
        tags=["Items"],
    )
    def update(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=["Items"],
    )
    def destroy(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        item.delete()
        return Response({"msg": "Item deleted"})


# %% Events


class EventTypeViewSet(viewsets.ViewSet):
    """
    Event types viewset
    """

    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer

    @extend_schema(
        responses=EventTypeSerializer,
        tags=["Event types"],
    )
    def list(self, request):
        serializer = EventTypeSerializer(self.queryset, many=True)
        return Response(serializer.data)


class EventViewSet(viewsets.ViewSet):
    """
    Events viewset
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @extend_schema(
        responses=EventSerializer,
        tags=["Events"],
    )
    def list(self, request):
        queryset = Event.objects.all()

        page = int(request.GET.get("page", "1"))
        size = int(request.GET.get("size", "10"))

        paginator = Paginator(queryset.order_by("id"), size)
        queryset = paginator.page(page)
        serializer = EventListSerializer(queryset, many=True)

        return Response(serializer.data)

    @extend_schema(
        tags=["Events"],
    )
    def create(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Event created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=["Events"],
    )
    def retrieve(self, request, pk=None):
        event = get_object_or_404(self.queryset, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    @extend_schema(
        tags=["Events"],
    )
    def update(self, request, pk=None):
        event = get_object_or_404(self.queryset, pk=pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=["Events"],
    )
    def destroy(self, request, pk=None):
        event = get_object_or_404(self.queryset, pk=pk)
        event.delete()
        return Response({"msg": "Event deleted"})


class TemplateViewSet(viewsets.ViewSet):
    """
    Templates viewset
    """

    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

    @extend_schema(
        responses=TemplateSerializer,
        tags=["Templates"],
    )
    def list(self, request):
        serializer = TemplateSerializer(self.queryset, many=True)
        return Response(serializer.data)


# %% GENERICS ------------------------------------------------------------------------


# %% ENTITY
class EntityListViewSet(generics.ListCreateAPIView):
    # queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    pagination_class = CustomPagination
    search_fields = ["name", "email", "telephone"]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Entity.objects.all()
        name = self.request.query_params.get("name")
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        # return super().get_queryset()  # queryset
        return queryset


# %% EVENT

# %% ITEM
