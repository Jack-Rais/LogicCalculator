# LogicCalculator
A logic calculator capable of solving complex boolean expression

This model can be used like this:

```
model = Resolver()
model.add_conn(And('name1', Or('name2', 'name3'))

for result in model.calc_poss():
  print(result)
```
