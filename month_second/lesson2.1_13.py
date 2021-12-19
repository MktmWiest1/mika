class Account:
    def __init__(self, name, password, secret_question):
        self.name = name
        self.password = password
        self.secret_question = secret_question

    def balance(self, summary):
        return f'Summary: {summary}'

    def __str__(self):
        return f'Name:{self.name}\n' \
               f'Password:{self.password}\n' \
               f'Secret_question:{self.secret_question}\n'


acc = Account(name='Adilet',
              password=123,
              secret_question='Something')
print(acc.balance(120))
print(acc.password)
