import re

from afflictions.models import Parasite


def get_parasite_species_list_safe():
    parasite_species = [x[0] for x in list(Parasite.objects.all().values_list("species"))]
    parasite_species_safe = []
    regularExp = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    for species in parasite_species:
        if regularExp.search(species) is None and species not in parasite_species_safe:
            parasite_species_safe.append(species)
    return parasite_species_safe
