import pandas as pd

# Load the dataset
file_path = r'C:\Users\sasik\Desktop\bda\Recommendation-System-Hadoop-master\Recommendation-System-Hadoop-master\Source Code\Dataset\u.user'
data = pd.read_csv(file_path, sep='|', header=None)

# Display the first few rows of the dataset
print("Initial Data:")
print(data.head())

# Step 1: Rename columns (if necessary)
data.columns = ['UserID', 'Age', 'Gender', 'Occupation', 'Zip-code']

# Step 2: Remove duplicates
data.drop_duplicates(inplace=True)

# Step 3: Handle missing values
# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# If there are any missing values, you can choose to drop them or fill them
# For example, dropping rows with missing values
data.dropna(inplace=True)

# Step 4: Convert data types (if necessary)
# Example: Ensure 'Age' is of integer type
data['Age'] = data['Age'].astype(int)

# Step 5: Remove any leading or trailing whitespace from string columns
data['Gender'] = data['Gender'].str.strip()
data['Occupation'] = data['Occupation'].str.strip()

# Step 6: Display cleaned data
print("\nCleaned Data:")
print(data.head())

# Optional: Save cleaned data to a new CSV file
cleaned_file_path = r'C:\Users\sasik\Desktop\bda\Recommendation-System-Hadoop-master\Recommendation-System-Hadoop-master\Source Code\Dataset\cleaned_user_data.csv'
data.to_csv(cleaned_file_path, index=False)
