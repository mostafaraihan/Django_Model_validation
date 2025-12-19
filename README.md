# Django_Model_validation

A Django project demonstrating a model with **built-in and custom validations**, and a **JSON API endpoint** to create model instances safely.

---

## Overview

This project provides a simple API for creating records in a `MyModel` database table. It ensures data integrity using **Django validators** and **custom validation logic**.

The model includes fields such as `name`, `age`, `email`, `phone`, and `salary`, with both **built-in** and **custom validations** applied.

---

## Features

- Django model with multiple fields:
  - `name` (CharField)
  - `age` (IntegerField)
  - `email` (EmailField, unique)
  - `phone` (CharField)
  - `salary` (DecimalField)
- Built-in validations:
  - Name minimum length
  - Email format and uniqueness
  - Salary range (30,000–400,000)
- Custom validations:
  - Salary must exceed 10,000
  - Phone number must contain only digits
- API endpoint for creating model instances via POST requests

---

## Usage

### API Endpoint

- **URL:** `/api/`  
- **Method:** POST  
- **Content-Type:** `application/json`  

**Request Body Example:**

```json
{
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com",
    "phone": "1234567890",
    "salary": 50000
}
```
Successful Response:
```
{
    "message": "successfully added"
}
```
Error Response Example:
```
{
    "error": "Phone number must contain only digits"
}
```
Validations
```
Built-in

MinLengthValidator for name

EmailValidator for email

MinValueValidator / MaxValueValidator for salary
```

```
Custom

salary must be greater than 10,000

phone must contain only numeric digits

All validations are enforced when calling full_clean() before saving.
```

---

API View Example

The endpoint is defined in views.py:
```
@csrf_exempt
def index(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            result = MyModel(
                name=data.get('name'),
                age=data.get('age'),
                email=data.get('email'),
                phone=data.get('phone'),
                salary=data.get('salary'),
            )
            result.full_clean()
            result.save()
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        return JsonResponse({'message': 'successfully added'}, status=201)
    return JsonResponse({'error': 'Only POST method allowed'}, status=405)
```

