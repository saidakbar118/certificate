from django.db import models

class Certificate(models.Model):
    certificate_number = models.CharField(max_length=20, unique=True)
    passport_series = models.CharField(max_length=2)
    passport_number = models.CharField(max_length=7)
    certificate_image = models.ImageField(upload_to='certificates/')  # sertifikat rasmi

    def __str__(self):
        return f"{self.certificate_number} - {self.passport_series}{self.passport_number}"
