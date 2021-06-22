from afflictions.models import Fungus, Medicine


def get_travels_from_examinations(examinations: list):
    travels = []
    for examination in examinations:
        travels += examination.travels.all()
    return travels


def filter_examinations_travel_time(queryset, country, days_min, days_max):
    queryset = queryset.filter(travels__country=country)
    to_be_removed = []
    for examination in queryset:
        valid = False
        for travel in examination.travels.all():
            min_check = False if days_min else True
            max_check = False if days_max else True
            if travel.country != country:
                continue
            if days_min and travel.days() >= days_min:
                min_check = True
            if days_max and travel.days() <= days_max:
                max_check = True
            if min_check and max_check:
                valid = True
                break
        if not valid:
            to_be_removed.append(examination.pk)
    queryset = queryset.exclude(pk__in=to_be_removed)
    return queryset


def filter_examinations_fungus_resistance(queryset, fungus, medicine, resistance):
    try:
        fungus = Fungus.objects.get(pk=fungus)
    except Fungus.DoesNotExist:
        return queryset
    try:
        medicine = Medicine.objects.get(pk=medicine)
    except Medicine.DoesNotExist:
        return queryset
    queryset = queryset.filter(fungi__fungus=fungus)
    to_be_removed = []
    for examination in queryset:
        valid = False
        for examination_fungus in examination.fungi.all():
            if examination_fungus.fungus != fungus:
                continue
            if (not resistance and (medicine in examination_fungus.high_resistance.all() or
                                    medicine in examination_fungus.mid_resistance.all() or
                                    medicine in examination_fungus.low_resistance.all())):
                valid = True
                break
            elif resistance == 0 and medicine in examination_fungus.high_resistance.all():
                valid = True
                break
            elif resistance == 1 and medicine in examination_fungus.mid_resistance.all():
                valid = True
                break
            elif resistance == 2 and medicine in examination_fungus.low_resistance.all():
                valid = True
                break
        if not valid:
            to_be_removed.append(examination.pk)
    queryset = queryset.exclude(pk__in=to_be_removed)
    return queryset
