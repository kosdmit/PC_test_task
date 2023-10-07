from django.shortcuts import render


# Create your views here.
import pandas as pd
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import DataFile
from .serializers import DataFileSerializer


class DataFileViewSet(viewsets.ModelViewSet):
    queryset = DataFile.objects.all()
    serializer_class = DataFileSerializer

    @action(detail=True, methods=['GET', ])
    def get_data(self, request, pk=None):
        file_obj = self.get_object()
        filepath = f"/files/{file_obj.name}"

        df = pd.read_csv(filepath)

        # Filtering
        filter_by = request.query_params.get('filter_by')
        filter_value = request.query_params.get('filter_value')
        if filter_by and filter_value:
            df = df[df[filter_by] == filter_value]

        # Sorting
        sort_by = request.query_params.get('sort_by')
        if sort_by:
            df = df.sort_values(by=sort_by)

        return Response(df.to_dict(orient='records'), status=status.HTTP_200_OK)
