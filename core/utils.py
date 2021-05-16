def get_travels_from_examinations(examinations: list):
    travels = []
    for examination in examinations:
        travels += examination.travels.all()
    return travels
