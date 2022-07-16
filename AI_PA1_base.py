# AI PA1: NQueens
# Group member:

# Emre YILDIZ, 200315092

# Readme
# Found an association between state's array indices and values. This helped to solve checking diaogonals for queens.
# Tested for N = 88888. It executed nearly 37 min. (for N = 8888 only 27 sec)

# Give some information about your Python version, development environment, etc.
# Emacs editor with python(3.9.2) shell in terminal.

# Part 1: Class definition
# This is the part that you will implement. See the comments in the code and read the assignment description.

# import files if needed
import random
from math import comb
# class definition for NQueens


class NQueens():
    """ class constructor
    initializes the instance attributes N and state """

    def __init__(self, N):
        self.N = N
        self.state = self.set_state()

    """ returns a formatted string
    that represents the instance """

    def __str__(self):
        string = ''.join([str(item)
                         for item in self.state])  # stackoverflow.com
        return 'N: ' + str(self.N) + ', state: ' + string

    """ Sets the instance attribute state by displaying
    a menu to the user. The user either enters the state
    manually or prompts the system to generate a random state.
    Check if the input state is a valid state. """

    def set_state(self):
        while(True):
            print("How do you want to set state?\n1. Set state manually\n2. Set state randomly\nEnter Selection: ")
            selection=input()
            if(selection == '1'):
                print('Enter state: ')
                state_input=input()
                try:
                    str_to_list=[]
                    str_to_list[:0]=state_input
                    str_to_list=list(map(int, str_to_list))
                    if(self._is_valid(str_to_list)):
                        return str_to_list
                    else:
                        print('invalid state, try again!\n')

                except:
                    print('invalid state, try again!\n')
            else:
                break

        return self.generate_random_state()
    """ generates and returns a valid random state """

    def generate_random_state(self):
        state_list=[]
        for i in range(0, self.N):
            state_list.insert(i, random.randint(1, self.N))

        return state_list

    """ This is an internal function that takes a state_str as input
    and return if this is a valid state or not """

    def _is_valid(self, state_str):
        a_list=list(range(1, self.N + 1))
        is_in_default=True

        for item in state_str:
            if item not in a_list:
                is_in_default=False

        return is_in_default and len(state_str) == self.N

    """ This is the primary function of this class.
    It returns the number of attacking pairs in the board.
    """

    def count_attacking_pairs(self):
        n=self.N

        def horiz_pairs(state):
            count=0
            pairs=0

            for num in range(1, n+1):
                for char in state:
                    if(int(char) == num):
                        count += 1

                if(count > 1):
                    pairs += comb(count, 2)
                count=0
            return pairs

        def diag_pairs(state):

            pairs=0
            count=0

            for ind_num_add in range(n-4, n+5):

                for indice in range(0, n):
                    if(indice + int(state[indice]) == ind_num_add):
                        count += 1

                if(count > 1):
                    pairs += comb(count, 2)
                count=0

            for ind_num_subs in range(-1 * (n-1), n-2):

                for indice in range(0, n):
                    if(indice - int(state[indice]) == ind_num_subs):
                        count += 1

                if(count > 1):
                    pairs += comb(count, 2)
                count=0

            return pairs

        
        if(n <= 1):
            return 0

        return 'Attacking pairs: '+ str(diag_pairs(self.state) + horiz_pairs(self.state))

# Part 2: Testing
# Do not change this part. This is the test code.


# This is a test code. You can try with different N values and states.
problem=NQueens(0)  # create NQueens instance
print(problem) # print the description of the problem
print(problem.count_attacking_pairs()) # print(problem.count_attacking_pairs()) #print the total number of attacking pairs in the board
