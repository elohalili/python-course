import array
import datetime
from collections import Counter, OrderedDict, defaultdict

li = [1, 2, 3, 4, 5, 5, 6, 7, 7, 7]
print(Counter(li))
# returns a dict with
# key: each item of the given iterable
# value: frequency of the item inside the iterable
# Counter({7: 3, 5: 2, 1: 1, 2: 1, 3: 1, 4: 1, 6: 1})


# these dicts will retain the order of the given items
d1 = OrderedDict(username='Elo', age=23)
d1['skill'] = 'over 9000'

d2 = OrderedDict()
d2['username'] = 'Elo'
d2['age'] = 23
d2['skill'] = 'over 9000'
# hence in case of checking the equality, also the order has an impact
print(d1 == d2)


# this will simply return the given default value in case of
# trying to retrieve a non existing item
def_d = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print(def_d['c'])

# just today...
print(datetime.date.today())

# creates a typed array ('i' typecode for int)
# performs better than lists
arr = array.array('i', [1, 2, 3])
print(arr)
