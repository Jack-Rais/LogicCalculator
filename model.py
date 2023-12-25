from boolean import And, Or, Not
import numpy as np

class Resolver:
        
    class logicConn:

        def __init__(self):

            self.lista_names = []
            self.lista_conn = []

        def add_variable(self, variable):

            if isinstance(variable, str):
                if variable not in self.lista_names:
                    self.lista_names.append(variable)

        def add_conn_int(self, conn):

            if isinstance(conn, (And, Or, Not)):
                for x in conn.tt_args():
                    self.add_conn_int(x)

            elif isinstance(conn, list):
                for u in conn:
                    if u not in self.lista_names:
                        self.lista_names.append(u)

            else:
                if x not in self.lista_names:
                    self.lista_names.append(x)

        def add_conn(self, conn):
            self.lista_conn.append(conn)

            for x in conn.tt_args():
                if isinstance(x, (list, And, Or, Not)):
                    self.add_conn_int(x)
                else:
                    if x not in self.lista_names:
                        self.lista_names.append(x)

        def calc_dictionary(self):
            lista = []
            lista.append(list('0' * len(self.lista_names)))

            for x in range(2**len(self.lista_names) - 1):
                int_p = ''.join( lista[-1])
                int_plus = bin( int( ''.join( lista[-1] ), 2 ) + 1 )[2:]
                aggiunta = '0' * (len(int_p)-len(int_plus))
                lista.append(list(aggiunta+int_plus))

            lista = np.array(lista).astype(bool)
            lista = [list(x) for x in lista]
                
            return lista
        
        def evaluation(self, lista):
            if all(elemento == lista[0] for elemento in lista):
                if lista[0]:
                    return 'True'
                else:
                    return 'False'
            return 'Maybe'

        def calc_poss(self):

            list_bool = self.calc_dictionary()
            
            result = self.calc_risultato(list_bool)

            for x in result.keys():
                val = self.evaluation(result[x])
                yield { x : val }


        def calc_risultato(self, list_bool):

            result = {self.lista_names[x]: [] for x in range(len(self.lista_names))}

            for y in list_bool:

                dictionary = {self.lista_names[x]:y[x] for x in range(len(self.lista_names))}
                lista_values = []

                for x in self.lista_conn:
                    if isinstance(x, (And, Or, Not)):
                        lista_values.append(x.valuate(dictionary))
                    else:
                        lista_values.append(dictionary[x])

                if False not in lista_values:
                    for x in result.keys():
                        result[x].append(dictionary[x])

            return result
        
        def clear(self):

            self.lista_conn = []
            self.lista_names = []
    
    class dictionaryConn:

        def __init__(dictConn):
            dictConn.lista_conn = []
            dictConn.lista_names = {}
            dictConn.known = None

        def load_dict(dictConn, dictionary, **var):

            if not dictConn.known:
                if dictionary:
                    dictConn.known = dictionary
                if var:
                    if not dictConn.known:
                        dictConn.known = {}
                    for key, v in var.items():
                        dictConn.known[key] = v
            else:
                if dictionary:
                    for key, v in dictionary.items():
                        dictConn.known[key] = v
                if var:
                    for key, v in var.items():
                        dictConn.known[key] = v
            
        def calc_poss_dict(dictConn, *chars):

            for variable in chars:
                dictConn.lista_conn.append(variable)

                if isinstance(variable, (And, Or, Not)):
                    list_var = variable.tt_args()
                    for var in list_var:
                        if var not in dictConn.lista_names.keys():
                            dictConn.lista_names[var] = True
                else:
                    if not variable in dictConn.lista_names:
                        dictConn.lista_names[variable] = True

            for name, valdata in dictConn.calc_int().items():
                yield {name: bool(valdata)}

        def calc_int(dictConn):
            risultato = dict((x, []) for x in dictConn.known.keys())

            for key, val in dictConn.known.items():

                if isinstance(val, (Not, And, Or)):
                    risultato[key].append(val.valuate(dictConn.lista_names))
                else:
                    risultato[key].append(dictConn.lista_names.get(val, False))
                
            return risultato
