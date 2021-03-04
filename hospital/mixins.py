from django.core.exceptions import FieldError
from django.forms import modelform_factory


class OrderableMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        order_by = self.request.GET.get("order_by")
        if not order_by:
            return queryset
        order_by = order_by.split(',')
        order_validated = []
        for order in order_by:
            try:
                queryset.order_by(order)
                order_validated.append(order)
            except FieldError:
                pass
        queryset = queryset.order_by(*order_validated)
        return queryset


class SearchableMixin:
    def validate_search_fields(self):
        search_fields_validated = []
        model_field_names = [f.name for f in self.model._meta.get_fields()]
        for field in self.search_fields:
            if field not in model_field_names:
                continue
            search_fields_validated.append(field)
        self.search_fields = search_fields_validated

    def get_extra_search_fields(self):
        return {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.validate_search_fields()
        context["search_form"] = modelform_factory(self.model, fields=self.search_fields)
        for name, field in self.get_extra_search_fields().items():
            context["search_form"].base_fields[name] = field
        for name, field in context["search_form"].base_fields.items():
            field.required = False
            field.help_text = ""
            field.initial = self.request.GET.get(name)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        for field in self.search_fields + list(self.get_extra_search_fields().keys()):
            val = self.request.GET.get(field)
            if not val:
                continue
            queryset = queryset.filter(**{f"{field}__icontains": val})
        return queryset
