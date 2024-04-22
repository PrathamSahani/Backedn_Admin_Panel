from django.db import models

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    
    request_type = models.CharField(max_length=100)
    details = models.TextField()
    attached_file = models.FileField(upload_to='attachments/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.request_type} - {self.status}"
    
    def get_file_url(self):
        if self.attached_file:
            return settings.MEDIA_URL + str(self.attached_file)
        return None
