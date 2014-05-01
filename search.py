
class Problem:
    '''This is the abstract class for defining a problem, and your cunstom
    problem should implement successor, possiblly __init__, goal_test, and
    path_test, then you could use the specific search funciton to solve
    your problem'''
    def __init__(self, initial, goal = None):
        self.initial = initial; self.goal = goal

    def successor(self, state):
        '''Given a state, return a sequence of (action state) pairs reachable
        from the state. If there are many successors, consider an iterator
        which yields one of successors at one time, rather than building then
        all at ones.'''
        abstract

    def goal_test(self, state):
        '''Default method check if equavilent to current state'''
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        '''c cost to get to state1'''
        return c + 1

    def value(self):
        abstract


class foo:
    def __init__(self, name, age):
        self.name = name; self.age = age    

    def renew(self):
        self.update(self, "steven", 24)

    def __repr__(self):
        return self.name + " with age is %s" & (self.age)



import random

random.rand





    
