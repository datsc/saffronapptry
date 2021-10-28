import random

random_list = [
"Melancholia",
"Burnt by the sun",
"Dogville",
"Big Fish",
"Borsalino"
]

def get_recommendation(form_data):
    random.shuffle(random_list)
    return form_data
