from itertools import permutations as perm

def permutations(s):
    result = set(perm(s))
    return ["".join(p) for p in result]
    
permutations(('abc'))

# perm genera todas las permutaciones por posición, set elimina duplicados
# une las tuplas en strings

# Sin permutations library

'''
def permutations(string):
  if len(string) == 1: return set(string)
  first = string[0]
  rest = permutations(string[1:])
  result = set()
  for i in range(0, len(string)):
    for p in rest:
      result.add(p[0:i] + first + p[i:])
  return result
'''