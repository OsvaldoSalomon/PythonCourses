from django.test import TestCase
import models

# "E:/osvaldo/PythonExercises/03ThirdCourse/expense-tracker-api/restapi"


# Create your tests here.
class TestModels(TestCase):
    def test_expense(self):
        expense = models.Expense.objects.create(
            amount=249.99,
            merchant="amazon",
            description="anc headphones",
            category="music",
        )
        inserted_expense = models.Expense.objects.get(ok=expense.id)

        self.assertEqual(249.99, inserted_expense.amount)
        self.assertEqual("amazon", inserted_expense.merchant)
        self.assertEqual("anc headphones", inserted_expense.description)
        self.assertEqual("music", inserted_expense.category)
