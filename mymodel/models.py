from django.db import models
from django.core.validators import (
    EmailValidator,
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
)
from django.core.exceptions import ValidationError


class MyModel(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    phone = models.IntegerField(blank=False, null=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

    def clean(self):
        errors = {}

        # name length validation
        try:
            MinLengthValidator(5, message="Please enter a valid name")(self.name)
        except ValidationError as e:
            errors['name'] = e.messages

        # email validation
        try:
            EmailValidator(message="Please enter a valid email address")(self.email)
        except ValidationError as e:
            errors['email'] = e.messages

        # salary min validation
        try:
            MinValueValidator(30000, message="Salary cannot be less than 30000")(self.salary)
        except ValidationError as e:
            errors['salary'] = e.messages

        # salary max validation
        try:
            MaxValueValidator(400000, message="Salary cannot be greater than 400000")(self.salary)
        except ValidationError as e:
            errors['salary'] = e.messages

        if errors:
            raise ValidationError(errors)
