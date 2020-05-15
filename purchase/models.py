from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book category (e.g. Science Fiction, Programming etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Learnbook(models.Model):
    title = models.CharField(max_length=200)
    tutor = models.ForeignKey('Tutor', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    category = models.ManyToManyField(Category, help_text="Select a category for this book")

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('purchases-detail', args=[str(self.id)])

    def display_category(self):
        """
        Creates a string for the Tutor. This is required to display tutor in Admin.
        """
        return ', '.join([category.name for category in self.category.all()[:3]])

    display_category.short_description = 'Category'


class Tutor(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, help_text="Info about Tutor / Информация о преподавателе")

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('tutor-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        # return '%s, %s' % (self.last_name, self.first_name)
        return '%s %s' % (self.last_name, self.first_name)
