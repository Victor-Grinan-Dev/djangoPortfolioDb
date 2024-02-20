from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import  OpenApiTypes
from .serializer import ChannelSerializer, ServerSerializer

server_list_docs = extend_schema(
    responses=ServerSerializer(many=True),
    parameters=[
        OpenApiParameter(
            name="category",
            type=OpenApiTypes.STR,
            location = OpenApiParameter.QUERY,
            description = "Category of the server bla bla",
        )
    ],
)