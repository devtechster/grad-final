import pandas as pd
import numpy as np

# Read the CSV data
data = '''[your CSV data here]'''

# Create a DataFrame from the CSV data
df = pd.read_csv(pd.compat.StringIO(data))

# Generate random prices between 5 CR and 18 CR for each row
random_prices = np.random.uniform(5, 18, size=len(df))

# Add the new column 'Price in Cr INR' to the DataFrame
df['Price in Cr INR'] = random_prices

# Display the modified DataFrame
print(df)
