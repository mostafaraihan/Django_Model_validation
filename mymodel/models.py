from django.core.exceptions import ValidationError
from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    phone = models.CharField(blank=False, null=False)
    salary = models.DecimalField(max_digits=15, decimal_places=2, blank=False, null=False)


    #build in properties
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



    #Custom Validation
    def clean(self):
        super().clean()
        errors = {}

        # Salary validation
        if self.salary < 10000:
            errors['salary'] = 'Salary must be greater than 10000'

        # Phone validation (integer-safe check)
        if not self.phone.isdigit():
            errors['phone'] = 'Phone number must contain only digits'

        if errors:
            raise ValidationError(errors)
