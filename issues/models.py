from django.db import models

class Issue(models.Model):
    """Model for reporting service delivery issues in communities."""
    
    ISSUE_TYPES = [
        ('water_leak', 'Water Leak'),
        ('electricity', 'Electricity Fault'),
        ('pothole', 'Pothole'),
        ('waste', 'Waste Collection'),
        ('other', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('reported', 'Reported'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('rejected', 'Rejected'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    issue_type = models.CharField(max_length=20, choices=ISSUE_TYPES)
    location = models.CharField(max_length=300)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='reported')
    priority = models.IntegerField(default=1, help_text="1=Low, 2=Medium, 3=High")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reporter_name = models.CharField(max_length=150)
    reporter_email = models.EmailField()
    image = models.ImageField(upload_to='issues/', null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Issues"
    
    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"
