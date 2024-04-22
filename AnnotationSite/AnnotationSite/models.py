# models.py

from django.db import models

class Selection(models.Model):
    image_data = models.TextField()  # Dane obrazu w formacie Base64
    x = models.IntegerField()        # Współrzędna x wyboru
    y = models.IntegerField()        # Współrzędna y wyboru
    width = models.IntegerField()    # Szerokość wyboru
    height = models.IntegerField()   # Wysokość wyboru
    created_at = models.DateTimeField(auto_now_add=True)  # Data utworzenia zapisu

    def __str__(self):
        return f"Selection at ({self.x}, {self.y}) with width {self.width} and height {self.height}"
