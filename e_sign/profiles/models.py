from django.db import models
from django.contrib.auth.models import User

# Gender choices tuple
GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
]
COUNTRY_CHOICES = [
    ("US", "United States"),
    ("IN", "India"),
    ("GB", "United Kingdom"),
    ("CA", "Canada"),
    ("DE", "Germany"),
    ("FR", "France"),
    ("ES", "Spain"),
    ("IT", "Italy"),
    ("NL", "Netherlands"),
    ("BE", "Belgium"),
    ("NO", "Norway"),
    ("SE", "Sweden"),
    ("DK", "Denmark"),
    ("FI", "Finland"),
    ("PL", "Poland"),
    ("PT", "Portugal"),
    ("IE", "Ireland"),
    ("LU", "Luxembourg"),
    ("AT", "Austria"),
    ("CH", "Switzerland"),
    ("CZ", "Czech Republic"),
    ("HU", "Hungary"),
    ("SK", "Slovakia"),
    ("RO", "Romania"),
    ("BG", "Bulgaria"),
    ("GR", "Greece"),
    ("CY", "Cyprus"),
    ("MT", "Malta"),
    ("LI", "Liechtenstein"),
    ("VA", "Vatican City"),
    ("MC", "Monaco"),
    ("SM", "San Marino"),
    ("VA", "Vatican City"),
]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, null=True
    )

    def __str__(self):
        return f"{self.user.username} Profile"
