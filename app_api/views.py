from django.shortcuts import render


# Create your views here.
import pandas
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import DataFile
from .serializers import DataFileSerializer


class DataFileViewSet(viewsets.ModelViewSet):
    queryset = DataFile.objects.all()
    serializer_class = DataFileSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['GET', ])
    def get_data(self, request, pk=None):
        file_obj = self.get_object()
        filepath = file_obj.file.path

        data_file = pandas.read_csv(filepath)

        # Filtering
        filter_by = request.query_params.get('filter_by')
        filter_value = request.query_params.get('filter_value')
        if filter_by and filter_value:
            try:
                data_file = data_file[data_file[filter_by] == filter_value]
            except KeyError:
                return Response({'error': 'filter column is not exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Sorting
        sort_by = request.query_params.get('sort_by')
        if sort_by:
            try:
                data_file = data_file.sort_values(by=sort_by)
            except KeyError:
                return Response({'error': 'sorting column is not exists'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data_file.to_dict(orient='records'), status=status.HTTP_200_OK)
