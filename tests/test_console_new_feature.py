import unittest
from io import StringIO
from console import HBNBCommand

class TestCreateCommand(unittest.TestCase):
    
    def setUp(self):
        self.cli = HBNBCommand()
        self.stdout = StringIO()

    def tearDown(self):
        self.cli.do_destroy("BaseModel 123")
        self.cli.do_destroy("User 123")
        self.cli.do_destroy("State 123")
        self.cli.do_destroy("City 123")
        self.cli.do_destroy("Amenity 123")
        self.cli.do_destroy("Place 123")
        self.cli.do_destroy("Review 123")
        self.stdout.close()

    def test_create_base_model(self):
        self.cli.onecmd("create BaseModel")
        self.assertEqual(self.stdout.getvalue().strip(), "*** Unknown syntax: create BaseModel\n")

        self.cli.onecmd('create BaseModel name="My House"')
        output = self.stdout.getvalue().strip()
        self.assertTrue(output.startswith("{}".format(self.cli.last_id)))
        self.assertIn("'name': 'My House'", output)
        self.assertEqual(len(self.cli.all()["BaseModel"].values()), 1)

        self.cli.onecmd('create BaseModel name="My House" number=123')
        output = self.stdout.getvalue().strip()
        self.assertTrue(output.startswith("{}".format(self.cli.last_id)))
        self.assertIn("'name': 'My House'", output)
        self.assertIn("'number': 123", output)
        self.assertEqual(len(self.cli.all()["BaseModel"].values()), 2)

        self.cli.onecmd('create BaseModel name="My House" number=123 email="example@example.com"')
        output = self.stdout.getvalue().strip()
        self.assertTrue(output.startswith("{}".format(self.cli.last_id)))
        self.assertIn("'name': 'My House'", output)
        self.assertIn("'number': 123", output)
        self.assertIn("'email': 'example@example.com'", output)
        self.assertEqual(len(self.cli.all()["BaseModel"].values()), 3)

    def test_create_user(self):
        self.cli.onecmd("create User")
        self.assertEqual(self.stdout.getvalue().strip(), "*** Unknown syntax: create User\n")

        self.cli.onecmd('create User first_name="John" last_name="Doe" email="johndoe@example.com" password="password"')
        output = self.stdout.getvalue().strip()
        self.assertTrue(output.startswith("{}".format(self.cli.last_id)))
        self.assertIn("'first_name': 'John'", output)
        self.assertIn("'last_name': 'Doe'", output)
        self.assertIn("'email': 'johndoe@example.com'", output)
        self.assertIn("'password': 'password'", output)
        self.assertEqual(len(self.cli.all()["User"].values()), 1)

if __name__ == "__main__":
    unittest.main()
