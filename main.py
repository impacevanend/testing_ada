from datetime import datetime
import unittest
from unittest.mock import Mock

class Greeter:
    def __init__(self, clock=datetime.now):
        self.clock = clock

    def greet(self, name):
        name = name.strip().capitalize()
        current_hour = self.clock().hour

        if 6 <= current_hour < 12:
            saludo = "Buenos días"
        elif 18 <= current_hour < 22:
            saludo = "Buenas tardes"
        elif 22 <= current_hour or current_hour < 6:
            saludo = "Buenas noches"
        else:
            saludo = "Hola"

        return f"{saludo} {name}"

class GreeterTest(unittest.TestCase):
    def test_saludo(self):
        greeter = Greeter()
        self.assertEqual(greeter.greet("Bob"), "Hola Bob")

    def test_saludo_recorta_espacios(self):
        greeter = Greeter()
        self.assertEqual(greeter.greet("  Bob  "), "Hola Bob")

    def test_saludo_capitaliza_primera_letra(self):
        greeter = Greeter()
        self.assertEqual(greeter.greet("bob"), "Hola Bob")

    def test_saludo_en_la_mañana(self):
        mock_clock = Mock(return_value=datetime(2023, 1, 1, 7, 0, 0))
        greeter = Greeter(clock=mock_clock)
        self.assertEqual(greeter.greet("Bob"), "Buenos días Bob")

    def test_saludo_en_la_tarde(self):
        mock_clock = Mock(return_value=datetime(2023, 1, 1, 19, 0, 0))
        greeter = Greeter(clock=mock_clock)
        self.assertEqual(greeter.greet("Bob"), "Buenas tardes Bob")

    def test_saludo_en_la_noche(self):
        mock_clock = Mock(return_value=datetime(2023, 1, 1, 23, 0, 0))
        greeter = Greeter(clock=mock_clock)
        self.assertEqual(greeter.greet("Bob"), "Buenas noches Bob")

if __name__ == '__main__':
    unittest.main()
