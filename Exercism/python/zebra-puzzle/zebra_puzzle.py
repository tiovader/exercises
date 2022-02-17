# $pip install python-constraint
from operator import eq
from constraint import Problem, AllDifferentConstraint, InSetConstraint



COLORS = ('yellow', 'blue', 'red', 'ivory', 'green')
NATIONALS = ('Norwegian', 'Ukrainian', 'Englishman', 'Spaniard', 'Japanese')
DRINKS = ('water', 'tea', 'milk', 'orange juice', 'coffee')
SMOKES = ('Kools', 'Chesterfield', 'Old Gold', 'Lucky Strike', 'Parliament')
PETS = ('fox', 'horse', 'snails', 'dog', 'zebra')

ALL_VAR = (COLORS, NATIONALS, DRINKS, SMOKES, PETS)
RIGHT_OF = lambda a, b: eq(a, b+1)
NEIGHBOUR = lambda a, b: eq(abs(a-b), 1)


problem = Problem()
[problem.addVariables(v, range(1, 6)) for v in ALL_VAR] # Adding all variables of this problem.


res = [(AllDifferentConstraint(), v) for v in ALL_VAR]  #  1. There are five houses.
res.append((eq, ('Englishman', 'red')))                 #  2. The Englishman lives in the red house.
res.append((eq, ('Spaniard', 'dog')))                   #  3. The Spaniard owns the dog.
res.append((eq, ('coffee', 'green')))                   #  4. Coffee is drunk in the green house.
res.append((eq, ('Ukrainian', 'tea')))                  #  5. The Ukrainian drinks tea.
res.append((RIGHT_OF, ('green', 'ivory')))              #  6. The green house is immediately to the right of the ivory house.
res.append((eq, ('Old Gold', 'snails')))                #  7. The Old Gold smoker owns snails.
res.append((eq, ('Kools', 'yellow')))                   #  8. Kools are smoked in the yellow house.
res.append((InSetConstraint({3}), ('milk',)))           #  9. Milk is drunk in the middle house.
res.append((InSetConstraint({1}), ('Norwegian',)))      # 10. The Norwegian lives in the first house.
res.append((NEIGHBOUR, ('Chesterfield', 'fox')))        # 11. The man who smokes Chesterfields lives in the house next to the man with the fox.
res.append((NEIGHBOUR, ('Kools', 'horse')))             # 12. Kools are smoked in the house next to the house where the horse is kept.
res.append((eq, ('Lucky Strike', 'orange juice')))      # 13. The Lucky Strike smoker drinks orange juice.
res.append((eq, ('Japanese', 'Parliament')))            # 14. The Japanese smokes Parliaments.
res.append((NEIGHBOUR, ('Norwegian', 'blue')))          # 15. The Norwegian lives next to the blue house.


[problem.addConstraint(*r) for r in res]                # Updating the solution based on the tips stored in `res`


def solution(key, category=NATIONALS):
    solution = problem.getSolution()
    return {solution[k]: k for k in category}[solution[key]]

drinks_water = lambda : solution('water')
owns_zebra = lambda : solution('zebra')
