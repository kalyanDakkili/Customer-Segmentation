import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)

# Generate 2000 Customer IDs
customer_ids = np.arange(1, 2001)

# Randomly assign genders
genders = np.random.choice(["Male", "Female"], size=2000)

# Generate ages between 18 and 70
ages = np.random.randint(18, 70, size=2000)

# Generate annual incomes between 10k$ and 150k$
annual_incomes = np.random.randint(10, 150, size=2000)

# Generate spending scores between 1 and 100
spending_scores = np.random.randint(1, 101, size=2000)

# Create DataFrame
df = pd.DataFrame({
    "CustomerID": customer_ids,
    "Gender": genders,
    "Age": ages,
    "Annual Income (k$)": annual_incomes,
    "Spending Score (1-100)": spending_scores
})

# Save to CSV
df.to_csv("dataset/customers.csv", index=False)

print("Dataset 'customers.csv' with 2000 records has been generated successfully!")
