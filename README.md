# LogicCalculator
A logic calculator capable of solving complex boolean expression

## For resolution of boolean expressions
This model can be used like this:

```
model = Resolver.logicConn()
model.add_conn(And('name1', Or('name2', 'name3', exc=True), 'name2')

for result in model.calc_poss():
  print(result)
```

### Output
```
{'name1' : True,
 'name2' : True,
 'name3' : False}
```

### To choose an element in a preset list of known parameters
This model can be used like this:

```
known_parameters = {'animal': And(Or('fly', 'swim', exc=False), Or('carnivorous', 'omnivorous', 'erbivorous', exc=True)),
                    'plant': And(Or('green', 'brown', exc=False), Or('tall', 'small', exc=True), Or('fruit', 'flower', exc=False))}

model = Resolver.dictConn()
model.load_dict(known_parameters)

predictions = model.calc_poss_dict(And('brown', 'tall'))

for prediction in predictions:
  print(predictions)
```

### Output
```
{'animal' : False,
 'plant' : True}
```
