import djqscsv

from django.core.exceptions import FieldError
from django.forms import modelform_factory
from collections import OrderedDict


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
            if field[0] not in model_field_names:
                continue
            search_fields_validated.append(field)
        self.search_fields = search_fields_validated

    def get_extra_search_fields(self):
        return {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.validate_search_fields()
        context["search_form"] = modelform_factory(self.model, fields=[f[0] for f in self.search_fields])
        for name, field in self.get_extra_search_fields().items():
            context["search_form"].base_fields[name] = field[0]
        for name, field in context["search_form"].base_fields.items():
            field.required = False
            field.help_text = ""
            initial = self.request.GET.getlist(name)
            if len(initial) > 1:
                field.initial = initial
            else:
                field.initial = self.request.GET.get(name)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.search_fields = list(OrderedDict.fromkeys(self.search_fields))  # TODO: Nie rozumiem dlaczego tak sie dzieje
        lookups = self.search_fields
        filters = {}
        for name, field in self.get_extra_search_fields().items():
            lookups.append((name, field[1]))
        for field in lookups:
            field_name = field[0]
            operation = field[1]
            if hasattr(self, "search_fields_omitted") and field_name in self.search_fields_omitted:
                continue
            or_lookup = False
            if operation:
                operation = "__" + operation
            else:
                operation = ""
            values = self.request.GET.getlist(field_name)
            if field_name[-4:] == "__OR":
                or_lookup = True
                field_name = field_name[:-4]
            elif field_name[-5:] == "__AND":
                field_name = field_name[:-5]
            if not values or len(values) == 0:
                continue
            for val in values:
                if not val:
                    continue
                if f"{field_name}{operation}" not in filters:
                    if or_lookup:
                        filters[f"{field_name}{operation}"] = [val]
                    else:
                        filters[f"{field_name}{operation}"] = val
                elif or_lookup:
                    filters[f"{field_name}{operation}"].append(val)
                else:
                    queryset = queryset.filter(**{f"{field_name}{operation}": val})
        queryset = queryset.filter(**filters).distinct()
        return queryset


class CSVMixin:
    def get_csv_mapping(self):
        # this is a default to be overwritten in view classes
        return {}

    def get_csv_queryset(self):
        # this is a default to be overwritten in view classes
        return self.get_queryset()

    def get_csv(self, request):
        qs = self.get_csv_queryset()
        return djqscsv.render_to_csv_response(qs, delimiter=";", field_serializer_map=self.get_csv_mapping())

    def get(self, request, *args, **kwargs):
        if "csv" in request.GET:
            return self.get_csv(request)
        return super().get(request, *args, **kwargs)
