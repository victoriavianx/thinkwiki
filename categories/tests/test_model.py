from categories.models import Categories
from django.test import TestCase


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.category_1_data = {
	        "name": "Pop"
        }


        cls.category_1 = Categories(**cls.category_1_data)
    
    def test_category_fields(self):
        print("executando test_category_fields")
        self.assertEqual(self.category_1.name, self.category_1_data["name"])


    def test_name_max_length(self):
        print("test_name_max_length")
        expected_max_length = 125
        result_max_length = self.category_1._meta.get_field("name").max_length
        msg = "Vefique o max_length de `first_name`"

        self.assertEqual(result_max_length, expected_max_length, msg)
