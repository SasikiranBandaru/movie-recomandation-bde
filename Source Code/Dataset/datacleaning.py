import pandas as pd

# File paths
input_file_path = r'C:\Users\sasik\Desktop\bda\Recommendation-System-Hadoop-master\Recommendation-System-Hadoop-master\Source Code\Dataset\u.item'  # Input file path
output_file_path = r'C:\Users\sasik\Desktop\bda\Recommendation-System-Hadoop-master\Recommendation-System-Hadoop-master\Source Code\Dataset\outputfile.csv'  # Output file path for cleaned data

# Define column names for the dataset
columns = ['MovieID', 'Title', 'ReleaseDate', 'IMDbURL'] + \
          ['Unknown', 'Action', 'Adventure', 'Animation', 'Children', 'Comedy', 
           'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 
           'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

# Load the dataset
df = pd.read_csv(input_file_path, sep='|', header=None, names=columns, encoding='ISO-8859-1')

# Print the shape of the DataFrame after loading
print(f"Shape of DataFrame after loading: {df.shape}")

# Drop the unnecessary 'VideoReleaseDate' column if it exists
df = df.drop(columns=['VideoReleaseDate'], errors='ignore')

# Convert 'ReleaseDate' to a proper date format and handle missing or incorrect date formats
df['ReleaseDate'] = pd.to_datetime(df['ReleaseDate'], errors='coerce')

# Drop rows with any missing values
df.dropna(inplace=True)

# Display the number of columns and rows
print(f"Number of rows: {df.shape[0]}, Number of columns: {df.shape[1]}")

# Display dataset info
print(df.info())

# Show the numbers of null values
print("Number of null values in each column:")
print(df.isnull().sum())

# Split 'ReleaseDate' into separate 'ReportedDate', 'From_Date', 'Year', 'Month', 'Day'
df['ReportedDate'] = df['ReleaseDate'].dt.date
df['From_Date'] = df['ReleaseDate'].dt.strftime('%Y-%m-%d')
df['Year'] = df['ReleaseDate'].dt.year
df['Month'] = df['ReleaseDate'].dt.month
df['Day'] = df['ReleaseDate'].dt.day

# Drop the original 'ReleaseDate' column
df.drop(columns=['ReleaseDate'], inplace=True)

# Display the updated number of columns and rows
print(f"Updated number of rows: {df.shape[0]}, Updated number of columns: {df.shape[1]}")

# Save the cleaned data to a new file
df.to_csv(output_file_path, index=False)

# Preview the first few rows of cleaned data
print(df.head())
