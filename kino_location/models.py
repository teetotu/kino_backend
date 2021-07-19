from django.db import models
import ast


class Location(models.Model):
    Link = models.CharField(max_length=255)
    Title = models.CharField(max_length=255)
    Description = models.TextField(default="[' ', ' ']")
    Photo = models.TextField(default="[' ', ' ']")
    Address = models.CharField(max_length=1000, blank=True, null=True, default='N/A')

    class Meta:
        ordering = ('Title',)

    def __str__(self) -> str:
        return self.Title

    def get_absolute_url(self):
        return f'/{self.id}/'

    def get_first_photo(self):
        if self.Photo:
            lst = ast.literal_eval(self.Photo)
            if len(lst):
                return lst[0]
        return 'https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg'

    def get_photos(self):
        if self.Photo:
            lst = ast.literal_eval(self.Photo)
            if len(lst):
                return lst
        return ['https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg', ]

    def get_descriptions(self):
        if self.Photo:
            lst = ast.literal_eval(self.Description)
            return ', '.join(lst)
