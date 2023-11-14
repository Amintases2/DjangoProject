from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .services import *

from .models import *


@method_decorator(csrf_exempt, name='dispatch')
class FormView(View):

    def post(self, request):
        """
        Возвращение формы по полям и их типам данных
        """
        form_field_types = get_form_validation_type(request.GET)
        conditions = Q()

        for field_name, field_type in form_field_types.items():
            conditions.add((Q(formfield__field_name=field_name) &
                            Q(formfield__field_type=field_type)), Q.OR)

        forms = FormTemplate.objects.filter(conditions)
        unique_forms = forms.distinct()

        for form in unique_forms:
            fields_count_test = list(forms).count(form)
            fields_count_real = FormField.objects.filter(template_name=form).count()

            if fields_count_test == fields_count_real:
                return HttpResponse(form)

        return JsonResponse(form_field_types)
