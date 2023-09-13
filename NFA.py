class NFA:
    def __init__(self, states, alphabet, transition, initial_states, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transition = transition
        self.initial_states = initial_states
        self.final_states = final_states

    def is_valid_input(self, input_string):
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
        return True

    def process_input(self, input_string):
        if not self.is_valid_input(input_string):
            return False

        current_states = self.initial_states
        for symbol in input_string:
            next_states = set()
            for state in current_states:
                if (state, symbol) in self.transition:
                    next_states.update(self.transition[(state, symbol)])
            current_states = next_states

        return any(state in self.final_states for state in current_states)

# Example usage:
if __name__ == "__main__":
    # Define the NFA (conversion from the given DFA)
    states = {'q0', 'q1', 'q2'}
    alphabet = {'0', '1'}
    transition = {
        ('q0', '0'): {'q0'},
        ('q0', '1'): {'q1'},
        ('q1', '0'): {'q2'},
        ('q1', '1'): {'q0'},
        ('q2', '0'): {'q1'},
        ('q2', '1'): {'q2'},
    }
    initial_states = {'q0'}
    final_states = {'q0'}

    nfa = NFA(states, alphabet, transition, initial_states, final_states)

    # Test the NFA with input strings
    input_strings = ['010101', '0110', '1001', '101010', '', '1']
    for input_string in input_strings:
        result = nfa.process_input(input_string)
        if result:
            print(f"'{input_string}' is accepted.")
        else:
            print(f"'{input_string}' is rejected.")
