class French:
    def __init__(self, lang):
        self.lang = lang

    def greeting(self):
        return f'Bonjuor'

class English:
    def __init__(self, lang):
        self.lang = lang

    def greeting(self):
        return f'Hello'

class Japanese:
    def __init__(self, lang):
        self.lang = lang

    def greeting(self):
        return f'Konnichiwa'


fren = French('french')
english = English('english')
jap = Japanese('japanese')
print(fren.greeting(), english.greeting(), jap.greeting())
