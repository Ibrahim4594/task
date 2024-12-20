# -*- coding: utf-8 -*-
"""task1,2,3,4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YZ6gX7tZCLaQZfsyhvZDt9WWxjjpXZvb
"""

pip install openpyxl

import pandas as pd
import numpy as np

# Define columns for the credit scoring dataset
columns = ['Age', 'Income', 'Loan Amount', 'Creditworthy']

# Print the column names
print("Columns in the dataset:", columns)

# Generate random data
np.random.seed(42)  # For reproducibility
data = {
    'Age': np.random.randint(18, 70, 10),  # Random ages between 18 and 70
    'Income': np.random.randint(20000, 120000, 10),  # Random income values
    'Loan Amount': np.random.randint(1000, 50000, 10),  # Random loan amounts
    'Creditworthy': np.random.choice([0, 1], size=10)  # Random binary labels (0 or 1)
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Print the generated data
print("\nRandomly Generated Data:")
print(df)

import numpy as np
import pandas as pd

# Define columns for the audio features and labels
columns = [f'Feature_{i}' for i in range(1, 21)] + ['Emotion']

# Print the column names
print("Columns in the dataset:", columns)

# Generate random data
np.random.seed(42)  # For reproducibility
data = {
    **{f'Feature_{i}': np.random.rand(10) for i in range(1, 21)},  # Random audio feature values
    'Emotion': np.random.choice(['Happy', 'Sad', 'Angry', 'Neutral'], size=10)  # Random emotion labels
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Print the generated data
print("\nRandomly Generated Data for Emotion Recognition:")
print(df)

import numpy as np
import pandas as pd

# Define columns for pixel values and labels
columns = [f'Pixel_{i}' for i in range(1, 785)] + ['Character']  # 28x28 = 784 pixels + 1 label column

# Print the column names
print("Columns in the dataset:", columns[:5], "...", columns[-1])  # Show first 5 and last column for brevity

# Generate random data
np.random.seed(42)  # For reproducibility
data = {
    **{f'Pixel_{i}': np.random.randint(0, 256, 10) for i in range(1, 785)},  # Random pixel values (0-255)
    'Character': np.random.choice(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), size=10)  # Random letters as labels
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Print the generated data
print("\nRandomly Generated Data for Handwritten Character Recognition:")
print(df)

import pandas as pd
import numpy as np

# Define columns for medical data and labels
columns = ['Age', 'Gender', 'Blood Pressure', 'Cholesterol', 'Diabetes', 'Smoking', 'Exercise', 'Disease']

# Print the column names
print("Columns in the dataset:", columns)

# Generate random data
np.random.seed(42)  # For reproducibility
data = {
    'Age': np.random.randint(18, 80, 10),  # Random ages between 18 and 80
    'Gender': np.random.choice(['Male', 'Female'], size=10),  # Random gender
    'Blood Pressure': np.random.choice(['Normal', 'High', 'Low'], size=10),  # Random blood pressure
    'Cholesterol': np.random.choice(['Normal', 'High'], size=10),  # Random cholesterol levels
    'Diabetes': np.random.choice(['Yes', 'No'], size=10),  # Random diabetes status
    'Smoking': np.random.choice(['Yes', 'No'], size=10),  # Random smoking status
    'Exercise': np.random.choice(['Regular', 'Rarely', 'Never'], size=10),  # Random exercise habits
    'Disease': np.random.choice(['Heart Disease', 'Diabetes', 'Hypertension', 'None'], size=10)  # Random disease
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Print the generated data
print("\nRandomly Generated Data for Disease Prediction:")
print(df)