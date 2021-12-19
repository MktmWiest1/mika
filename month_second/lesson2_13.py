class Junior:
    def __init__(self, laptop, salary, prog_lang):
        if isinstance(laptop, bool):
            self.laptop = laptop
        else:
            raise ValueError('Laptop should be boolean')
        if isinstance(salary, int):
            self.salary = salary
        else:
            raise ValueError('salary should be interger')

        if isinstance(prog_lang, str):
            self.prog_lang = prog_lang

        else:
            raise ValueError('prog_lang should be str')

    def can_copy_pasted(self, source):
        return f'Can you copy paste cod from {source}'

    def __str__(self):
        return f'Laptop: {self.laptop}\n' \
               f'salary: {self.salary}$\n' \
               f'prog_lang: {self.prog_lang}'


proger = Junior(laptop=True, salary=350, prog_lang='Python')
print(proger)
print(proger.can_copy_pasted('StackOverFlow'))

class Middle(Junior):
    def __init__(self, laptop, salary, prog_lang, experience, responsibility):
        super().__init__(laptop, salary, prog_lang)
        if isinstance(experience, float):
            self.exp = experience

        else:
            raise ValueError(' Experience should be float')

        if isinstance(responsibility, bool):
            self.resp = responsibility

        else:
            raise ValueError(' Responsibility should be boolean')

    def can_be_mentor(self):
        return f'Can be mentor to {proger}'

    def __str__(self):
        return super(Middle, self).__str__() + f'Experience: {self.exp}\n' \
                                               f'Responsibility: {self.resp}\n'


mid_proger = Middle(laptop=True, salary=1200, prog_lang='Python',
                    experience=2.5, responsibility=True)
print(mid_proger)
print(mid_proger.can_be_mentor())

class Senior(Middle):
    def __init__(self, laptop, salary, prog_lang, experience, responsibility,archi_fav):
        super().__init__(laptop, salary, prog_lang, experience, responsibility)
        if isinstance(archi_fav, str):
            self.arch = archi_fav
        else:
            raise ValueError('Favourit Architecture should be str')

    def advance_skills(self, lang):
        if lang == 'Python':
            return 'Can do same Machine Learning'
        elif lang == 'C#':
            return 'Can do some cool GameDev projects '
        elif lang == 'Golang':
            return 'Can do some cool microservices '

    def __str__(self):
        return super(Senior, self).__str__()+ f'\nFavourit Architecture: {self.arch}'


sen_proger = Senior(laptop=True, salary=4000, prog_lang='Python', experience=5.0, responsibility=True,
                    archi_fav ='MVC')
print(sen_proger)
print(sen_proger.can_copy_pasted('Stack'))
print(sen_proger.can_be_mentor())
print(sen_proger.advance_skills('Python'))











