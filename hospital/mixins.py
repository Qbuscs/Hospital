class OrderableMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        order_by = self.request.GET.get("order_by")
        if not order_by:
            return queryset
        order_by = order_by.split(',')
        order_validated = []
        for order in order_by:
            if not order:
                continue
            field_names = [f.name for f in self.model._meta.get_fields()]
            if order not in field_names and (order[0] == "-" and order[1:] not in field_names):
                continue
            order_validated.append(order)
        print(order_validated)
        queryset = queryset.order_by(*order_validated)
        return queryset
