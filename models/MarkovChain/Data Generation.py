# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 14:40:28 2024

@author: kashy
"""

import random

class MarkovModel:
    def __init__(self, transition_matrix):
        """
        Initialize the Markov model with a user-defined transition matrix.

        Parameters:
            transition_matrix (dict): A dictionary representing the transition probabilities.
                Keys are states, and values are dictionaries where keys are possible next states
                and values are the corresponding transition probabilities.
        """
        self.transition_matrix = transition_matrix

    def generate_sequence(self, initial_state, length):
        """
        Generate a sequence of states from the Markov model.

        Parameters:
            initial_state: The initial state of the sequence.
            length (int): The length of the sequence to generate.

        Returns:
            list: A sequence of states generated from the Markov model.
        """
        sequence = [initial_state]
        current_state = initial_state
        for _ in range(length - 1):
            next_state = random.choices(
                list(self.transition_matrix[current_state].keys()),
                weights=list(self.transition_matrix[current_state].values())
            )[0]
            sequence.append(next_state)
            current_state = next_state
        return sequence

# User-defined transition matrix
transition_matrix = {
    'A': {'A': 0.2, 'B': 0.5,'C':0,'D':0.1},
    'B': {'A': 0.4, 'B': 0.4,'C':0.1,'D':0.1},
    'C': {'A': 0.6, 'B': 0.1,'C':0.2,'D':0.1},
    'D': {'A': 0, 'B': 0,'C':0,'D':1},
}

# Create the Markov model with user-defined transition matrix
markov_model = MarkovModel(transition_matrix)

# Generate a sequence of states
initial_state = 'A'
sequence_length = 10
generated_sequence = markov_model.generate_sequence(initial_state, sequence_length)

print("Generated Sequence:", generated_sequence)
