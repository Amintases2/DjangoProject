from django.db import models


class FormTemplate(models.Model):
    """
    Название шаблона формы
    """
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class FormField(models.Model):
    """
    Поле формы
    """
    filed_types = [
        ("date", "date"),
        ("phone", "phone"),
        ("email", "email"),
        ("text", "text"),
    ]

    template_name = models.ForeignKey(FormTemplate, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=64)
    field_type = models.CharField(choices=filed_types, max_length=64)
