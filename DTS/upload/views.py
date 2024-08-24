# upload/views.py
from django.shortcuts import render, redirect
from django.views import View
from .models import Document

class UploadDocumentView(View):
    def get(self, request):
        return render(request, 'upload/upload_document.html')

    def post(self, request):
        title = request.POST.get('title')
        file = request.FILES.get('file')
        assigned_to = request.POST.get('assigned_to')
        from_person = request.POST.get('from_person')
        remarks = request.POST.get('remarks')

        if title and file:
            document = Document(
                title=title,
                file=file,
                assigned_to=assigned_to,
                from_person=from_person,
                remarks=remarks
            )
            document.save()
            return redirect('upload:success')
        return render(request, 'upload/upload_document.html', {
            'error': 'Title and file are required fields.'
        })

class SuccessView(View):
    def get(self, request):
        return render(request, 'upload/upload_success.html')
