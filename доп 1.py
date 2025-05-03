class Temperature:
    def __init__(self, celsius):
        # Приватный атрибут для хранения температуры в градусах Цельсия
        self._celsius = None  # сначала устанавливаем в None
        self.celsius = celsius

    @property
    def celsius(self):
        """
        Геттер для температуры в Цельсиях.
        Позволяет обращаться к self.celsius как к обычному атрибуту.
        """
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """
        Проверяет, что значение — число.
        """
        if not isinstance(value, (int, float)):
            raise ValueError("Температура должна быть числом (int или float)")
        self._celsius = value

    @property
    def fahrenheit(self):
        """
        Динамическое свойство для получения температуры в Фаренгейтах.
        Вычисляется на лету по формуле: F = C * 9/5 + 32
        """
        return self._celsius * 9 / 5 + 32

temp = Temperature(25)
print(f"Цельсий: {temp.celsius}")
print(f"Фаренгейт: {temp.fahrenheit}")

temp.celsius = 100  # меняем температуру
print(f"Цельсий: {temp.celsius}")
print(f"Фаренгейт: {temp.fahrenheit}")