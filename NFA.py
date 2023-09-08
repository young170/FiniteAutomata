class NFA : 
    # Q: set of states
    # Sigma: set of symbols
    # delta: transition relation
    # S: set of initial states
    # F: set of final states
    def __init__(self, Q, Sigma, delta, S, F) :
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta
        self.S = S
        self.F = F

    def do_delta(self, q, x) :
        try :
            return self.delta[(q, x)] # set of transition states
        except KeyError :
            return set({})
        
    def run (self, symbols) :
        P = self.S # initial state

        while symbols != "" :
            Pnew = set ({})

            for q in P : # for all the states in P
                Pnew = Pnew | self.do_delta(q, symbols[0]) # get a new state and union of the new states

            symbols = symbols[1:] # next symbol
            P = Pnew

        return (P & self.F) != set({}) # intersection of P and final state shouldn't be empty
    
N0 = NFA(
    {0, 1, 2},
    {"0", "1"},
    {
        (0, "0"):{0},
        (0, "1"):{0, 1},
        (1, "0"):{2},
        (1, "1"):{2}
    },
    {0},
    {2}
)