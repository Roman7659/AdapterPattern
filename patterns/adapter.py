# Це ваша основна логіка, яку потрібно адаптувати
class OldSystem:
    def specific_request(self):
        return "Old System Request"

# Це клас адаптера, який забезпечує сумісність старої системи з новою
class Adapter:
    def __init__(self, old_system):
        self.old_system = old_system

    def request(self):
        return self.old_system.specific_request()

# Нова система, яка використовує адаптер
class NewSystem:
    def __init__(self, adapter):
        self.adapter = adapter

    def new_request(self):
        return self.adapter.request()

# Використання патерну Адаптер
old_system = OldSystem()
adapter = Adapter(old_system)
new_system = NewSystem(adapter)

result = new_system.new_request()
print(result)  # Виведе: Old System Request
 
