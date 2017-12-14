from collections import defaultdict


def tree(): return defaultdict(tree)

def dicts(t): return {k: dicts(t[k]) for k in t}

def add(t, path):
# add(t, 'Animalia>Chordata>whale'.split('>'))
  for node in path:
    t = t[node]

def print_tree(t, depth = 0):
    """ print a tree """
    for k in t.keys():
        print("%s %2d %s" % ("".join(depth * ["    "]), depth, k))
        depth += 1
        print_tree(t[k], depth)
        depth -= 1