import numpy as np

class Or:

    def __init__(self, *args, exc=False):

        self.exc = exc
        self.lista_names = []
        for x in args:
            self.lista_names.append(x)        

    def valuate(self, dictionary):

        lista_bool = []
        for x in self.lista_names:
            if isinstance(x, (Or, And, Not)):
                lista_bool.append(x.valuate(dictionary))
            else:
                lista_bool.append(dictionary.get(x, False))

        if not self.exc:
            if True in lista_bool:
                return True
            return False
        else:
            dictionary = {}
            for x in lista_bool:
                if x not in dictionary:
                    dictionary[x] = 1
                else:
                    dictionary[x] += 1
            if True in dictionary.keys():
                if dictionary[True] == 1:
                    return True
            return False
    
    def tt_args(self):
        lista_names = []

        for x in self.lista_names:
            if isinstance(x, (And, Or, Not)):
                lista_names.append(x.tt_args())
            else:
                lista_names.append(x)

        return lista_names
    
    def string(self):
        return f'Or {self.lista_names} exc: {self.exc}'
    
    def tipo(self):
        return f'or{self.exc}'
    
    def __repr__(self):
        return f'Or {self.lista_names} exc: {self.exc}'

class And:

    def __init__(self, *args):

        self.lista_names = []
        for x in args:
            self.lista_names.append(x)

    def valuate(self, dictionary):
        lista_bool = []

        for x in self.lista_names:
            if isinstance(x, (Or, And, Not)):
                lista_bool.append(x.valuate(dictionary))
            else:
                lista_bool.append(dictionary.get(x, False))

        if False in lista_bool:
            return False
        return True
    
    def tt_args(self):
        lista_names = []

        for x in self.lista_names:
            if isinstance(x, (And, Or, Not)):
                lista_names.append(x.tt_args())
            else:
                lista_names.append(x)

        return lista_names
    
    def string(self):
        return f'And {self.lista_names}'
    
    def tipo(self):
        return f'and'

    def __repr__(self):
        return f'And {self.lista_names}'

class Not:

    def __init__(self, *args):

        self.lista_names = []
        for x in args:
            self.lista_names.append(x)

    def valuate(self, dictionary):
        lista_bool = []

        for x in self.lista_names:
            if isinstance(x, (Or, And, Not)):
                lista_bool.append(x.valuate(dictionary))
            else:
                lista_bool.append(dictionary.get(x, False))

        if False in lista_bool:
            return True
        return False
    
    def tt_args(self):
        lista_names = []

        for x in self.lista_names:
            if isinstance(x, (And, Or, Not)):
                lista_names.append(x.tt_args())
            else:
                lista_names.append(x)

        print(lista_names)

        return lista_names
    
    def string(self):
        return f'Not {self.lista_names}'
    
    def tipo(self):
        return 'not'
    
    def __repr__(self):
        return f'Not {self.lista_names}'
