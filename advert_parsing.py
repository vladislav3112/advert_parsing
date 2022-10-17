import json


def json_to_dict(json_filename):
    with open(json_filename, encoding="utf-8") as json_file:
        return json.load(json_file)


class ColorizeMixin:
    """
    ○ меняет цвет теĸста при выводе на ĸонсоль
    ○ задает цвет в атрибуте ĸласса repr_color_code
    """

    # список цветов
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"  # вернуть цвет на стандартный
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    # текущий цвет
    repr_color_code = WARNING

    def __repr__(self):
        return f"{ColorizeMixin.repr_color_code} {self.title} | {self.price} ₽ {ColorizeMixin.ENDC}"


class Advert(ColorizeMixin):
    """Класс Advert для парсинга объявлений в формате JSON:
    1. динамичесĸи создает атрибуты эĸземпляра ĸласса из атрибутов JSON-объеĸта
    2. имеет свойство price и
        ○ проверяет, что устанавливаемое значение не отрицательно
        ○ в случае отсутствия поля price в JSON-объеĸте возвращает 0
    3. метод __repr__, ĸоторый выводит название и цену объявления
    """

    def __setattr__(self, __name: str, __value) -> None:
        if __name == "price" and __value < 0:
            raise ValueError("Price must be >= 0")
        return super().__setattr__(__name, __value)

    def __repr__(self):
        if not super():
            return f" {self.title} | {self.price} ₽"
        else:
            return super().__repr__()

    def __init__(self, mapping):
        for atribute in mapping:
            curr_atribute = atribute
            if isinstance((mapping[curr_atribute]), dict):
                curr_dict = mapping[curr_atribute]
                setattr(self, curr_atribute, Advert(curr_dict))
            else:
                setattr(self, curr_atribute, mapping[curr_atribute])
        if not hasattr(self, "price"):
            self.price = 0


if __name__ == "__main__":
    # sample test
    dictionary = json_to_dict("sample_ad.json")
    lesson_ad = Advert(dictionary)
    assert lesson_ad.location.address == "город Москва, Лесная, 7"
    assert lesson_ad.price == 0
    print(lesson_ad)

    # проверка смены цвета вывода в консоль
    dictionary_corgi = json_to_dict("corgi.json")
    corgi_ad = Advert(dictionary_corgi)
    print(corgi_ad)
    corgi_ad.__class__
    print(getattr(corgi_ad, "class"))
    # price < 0
    dictionary_fail = json_to_dict("price_test_ad.json")
    lesson_ad.price = -2  # ValueError
    # fail_ad = Advert(dictionary_fail) #ValueError
