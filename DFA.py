class DFA:
    def __init__(self, states, alphabet, transition, initial_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transition = transition
        self.initial_state = initial_state
        self.final_states = final_states

    def is_valid_input(self, input_string):
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
        return True

    def process_input(self, input_string):
        if not self.is_valid_input(input_string):
            return False
        
        current_state = self.initial_state
        for symbol in input_string:
            if current_state not in self.states:
                return False  # Invalid state
            current_state = self.transition.get((current_state, symbol), None)
            if current_state is None:
                return False  # No transition defined

        return current_state in self.final_states

# Example usage:
if __name__ == "__main__":
    # Define the DFA
    states = {'q0', 'q1', 'q2'}
    alphabet = {'0', '1'}
    transition = {
        ('q0', '0'): 'q0',
        ('q0', '1'): 'q1',
        ('q1', '0'): 'q2',
        ('q1', '1'): 'q0',
        ('q2', '0'): 'q1',
        ('q2', '1'): 'q2',
    }
    initial_state = 'q0'
    final_states = {'q0'}

    dfa = DFA(states, alphabet, transition, initial_state, final_states)

    # Test the DFA with input strings
    input_strings = ['010101', '0110', '1001', '101010']
    for input_string in input_strings:
        result = dfa.process_input(input_string)
        if result:
            print(f"'{input_string}' is accepted.")
        else:
            print(f"'{input_string}' is rejected.")
