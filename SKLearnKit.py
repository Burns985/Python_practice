import pandas as pd
from sklearn.impute import KNNImputer

# Read the CSV file into a pandas DataFrame
notebook = pd.read_csv("video_games.csv")

# Assuming that 'notebook' contains the columns with missing values you want to impute

# Extract the numerical columns from the DataFrame (if you have non-numerical columns, you should handle them separately)
numerical_columns = notebook.select_dtypes(include=[float, int]).columns

# Initialize KNNImputer and fit to DataFrame
knn_imputer = KNNImputer(n_neighbors=50)
notebook_imputed_array = knn_imputer.fit_transform(notebook[numerical_columns])

# Convert the imputed array back to a DataFrame
notebook_imputed = pd.DataFrame(notebook_imputed_array, columns=numerical_columns)

# Now 'notebook_imputed' contains the DataFrame with imputed values for the numerical columns.
# Non-numerical columns (if any) are not imputed and still remain in the DataFrame.
