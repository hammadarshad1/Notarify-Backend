from django.http.response import FileResponse
from rest_framework.views import APIView

from .serializers import PDFSerializer
from utils.generate_pdf import generate_pdf

class PDFView(APIView):
    serializer_class = PDFSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        print("done")
        serializer.is_valid(raise_exception=True)
        doc = generate_pdf(serializer.validated_data)
        return FileResponse(
            open(doc.filename, 'rb')
        )
