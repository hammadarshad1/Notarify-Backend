from django.http.response import FileResponse
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import status

from drf_pdf.response import PDFFileResponse

from .serializers import PDFSerializer
from utils.generate_pdf import generate_pdf

class PDFView(APIView):
    serializer_class = PDFSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        print("done")
        serializer.is_valid(raise_exception=True)
        doc = generate_pdf(serializer.validated_data)
        return PDFFileResponse(
            file_path=doc.filename,
            status=status.HTTP_200_OK
        )
