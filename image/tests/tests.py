# import io
#
# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
#
#
# from PIL import Image as Im
#
#
# class TestApi(APITestCase):
#
#     def generate_photo_file(self):
#         file = io.BytesIO()
#         image = Im.new('RGBA', size=(100, 100), color=(155, 0, 0))
#         image.save(file, 'png')
#         file.seek(0)
#         return SimpleUploadedFile("test.jpg", file.getvalue())
#
#     def test_upload_photo(self):
#         url = reverse('image-list')
#         photo_file = self.generate_photo_file()
#         data = {
#                 'photo': photo_file
#             }
#         response = self.client.post(url, data, format='multipart')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)