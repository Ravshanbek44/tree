from django.db import models
from trades.models import TypeTree, District


class TreeReport(models.Model):
    STATUS = (
        (1, 'New'),
        (2, 'Two'),
        (3, 'Three'),
    )
    status = models.IntegerField(choices=STATUS, default=1)
    company_stir = models.CharField(max_length=20)
    company_name = models.CharField(max_length=221)
    owner_fio = models.CharField(max_length=221)
    owner_jshshir = models.CharField(max_length=16)
    contract_number = models.CharField(max_length=22)
    description = models.TextField()
    type_tree = models.ForeignKey(TypeTree, on_delete=models.CASCADE)
    count_tree = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    number_report = models.CharField(max_length=20)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.company_name


class ReportImage(models.Model):
    report = models.ForeignKey(TreeReport, on_delete=models.CASCADE, related_name='reports_images')
    image = models.ImageField(upload_to='reports/')

    def __str__(self):
        return self.report.company_name
