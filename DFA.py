class DFA :
    # Q: set of states
    # Sigma: set of symbols
    # delta: transition function
    # q0: initial state
    # F: set of final states
    def __init__(self, Q, Sigma, delta, q0, F) :
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta
        self.q0 = q0
        self.F = F

    def run (self, symbols) :
        q = self.q0 # starting state

        while symbols != "" :
            q = self.delta[(q, symbols[0])] # transition
            symbols = symbols[1:] # next symbol
        
        return q in self.F
    
# DFA_0
# accepts symbols containing 'ab'
# (0) -b-> 1 -a-> (2)
#  a       b      a,b
D0 = DFA(
    {0, 1, 2},
    {"a", "b"},
    {
        (0, "a"):0,
        (0, "b"):1,
        (1, "a"):2,
        (1, "b"):1,
        (2, "a"):2,
        (2, "b"):2,
    },
    0,
    {0, 2}
)

# DFA_1
# accepts symbols with even/odd number of 'a's and 'b's
# (0) -a,b-> 1
#     <-a,b-
D1 = DFA(
    {0, 1},
    {"a", "b"},
    {
        (0, "a"):1,
        (0, "b"):1,
        (1, "a"):0,
        (1, "b"):0,
    },
    0,
    {0}
)