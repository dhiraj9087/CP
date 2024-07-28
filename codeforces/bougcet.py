# import math
# import sys
# input=sys.stdin.readline
# def main():
#     n,m=map(int,input().split())
#     a=list(map(int,input().split()))
#     a.sort()
#     print(a)
    
# for _ in range(int(input())):
#    main()


import numpy as np

class SimpleNeuron:
    def __init__(self):
        # Initialize weight and bias with random values
        self.weight = np.random.randn()
        self.bias = np.random.randn()
        
    def activate(self, x):
        # Simple step function
        return 1 if x > 0 else 0
    
    def predict(self, input):
        # Calculate the weighted sum of input plus bias
        weighted_sum = input * self.weight + self.bias
        return self.activate(weighted_sum)
    
    def train(self, input, target, learning_rate=0.1):
        # Make a prediction
        prediction = self.predict(input)
        
        # Calculate error
        error = target - prediction
        
        # Update weight and bias
        self.weight += error * input * learning_rate
        self.bias += error * learning_rate

# Create a neuron
neuron = SimpleNeuron()

# Training data: (input, target)
training_data = [
    (2, 0), (4, 0), (6, 1), (8, 1)
]

# Train the neuron
for _ in range(100):  # Train for 100 epochs
    for input, target in training_data:
        neuron.train(input, target)

# Test the trained neuron
test_data = [1, 3, 5, 7, 9]
for input in test_data:
    prediction = neuron.predict(input)
    print(f"Input: {input}, Prediction: {prediction}")

print(f"\nFinal weight: {neuron.weight:.2f}")
print(f"Final bias: {neuron.bias:.2f}")

