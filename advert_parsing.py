import json


def json_to_dict(json_filename):
    with open(json_filename, encoding="utf-8") as json_file:
        return json.load(json_file)

class ColorizeMixin:
    repr_color_code = 32 # green

class Advert(ColorizeMixin):
    def __repr__(self):
        return f'{self.title} | {self.price} ₽'
    def __init__(self, mapping):
        for atribute in mapping:
            curr_atribute = atribute
            if isinstance((mapping[curr_atribute]), dict):
                curr_dict = mapping[curr_atribute]
                setattr(self, curr_atribute, Advert(curr_dict))
            else:
                setattr(self, curr_atribute, mapping[curr_atribute])
        if hasattr(self, 'price'):
            if self.price < 0:
                raise ValueError('Price must be >= 0')
        else:
            self.price = 0

if __name__ == "__main__":
    dictionary = json_to_dict("sample_ad.json")
    lesson_ad = Advert(dictionary)
    assert lesson_ad.location.address == 'город Москва, Лесная, 7'
    assert lesson_ad.price == 0
    print(lesson_ad)
    
    dictionary2 = json_to_dict("price_test_ad.json")
    lesson_ad2 = Advert(dictionary2)
    