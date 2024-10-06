# import pandas as pd
# from collections import defaultdict
# import os
#
# # Load the Excel file
# file_path = 'docops.xlsx'  # Replace with your actual file path
# sheet_name = '-content-dam-broadcom-techdocs-'  # Replace with the correct sheet name if needed
# column_name = 'PATH'  # Replace with the correct column name that contains the paths
#
# # Read the Excel file
# df = pd.read_excel(file_path, sheet_name=sheet_name)
#
# # Dictionary to store counts
# folder_counts = defaultdict(int)
#
# # Define the base path to start counting after
# base_path = "/content/dam/broadcom/techdocs/us/en/assets/docops/"
# print(len(df[column_name]))
# # Process each path in the column
# for path in df[column_name]:
#     # Remove the base path
#     relative_path = path.replace(base_path, "")
#
#     # Split the remaining path into parts (folders/files)
#     parts = relative_path.split(os.sep)
#
#     # Count each folder in the path
#     for i in range(len(parts) - 1):  # Exclude the last part (file)
#         folder = os.sep.join(parts[:i + 1])
#         folder_counts[folder] += 1
#
# # Convert the results to a DataFrame
# result_df = pd.DataFrame(list(folder_counts.items()), columns=['Folder Path', 'Count'])
#
# # Save the results to a new Excel file
# output_file_path = 'folder_counts_output.xlsx'
# result_df.to_excel(output_file_path, index=False)
#
# print(f"Folder counts have been saved to {output_file_path}")




import pandas as pd
from collections import defaultdict
import os

# Load the Excel file
file_path = 'docops.xlsx'  # Replace with your actual file path
sheet_name = '-content-dam-broadcom-techdocs-'  # Replace with the correct sheet name if needed
column_name = 'PATH'  # Replace with the correct column name that contains the paths

# Read the Excel file
try:
    df = pd.read_excel(file_path, sheet_name=sheet_name)
except Exception as e:
    print(f"Error reading Excel file: {e}")
    raise

# Check if the column exists
if column_name not in df.columns:
    raise ValueError(f"Column '{column_name}' not found in sheet '{sheet_name}'")

# Dictionary to store counts
folder_counts = defaultdict(int)

# Define the base path to start counting after
base_path = "/content/dam/broadcom/techdocs/us/en/assets/docops/"

# Print the number of paths read
print(f"Number of paths read: {len(df[column_name])}")

# Process each path in the column
for path in df[column_name].dropna():  # Drop any NaN values
    # Remove the base path
    relative_path = path.replace(base_path, "", 1)  # Limit the replacement to avoid issues

    # Split the remaining path into parts (folders/files)
    parts = relative_path.split('/')

    # Count each folder in the path
    for i in range(len(parts) - 1):  # Exclude the last part (file)
        folder = '/'.join(parts[:i + 1])
        folder_counts[folder] += 1

# Convert the results to a DataFrame
result_df = pd.DataFrame(list(folder_counts.items()), columns=['Folder Path', 'Count'])

# Save the results to a new Excel file
output_file_path = 'folder_counts_output.xlsx'
try:
    result_df.to_excel(output_file_path, index=False)
    print(f"Folder counts have been saved to {output_file_path}")
except Exception as e:
    print(f"Error saving Excel file: {e}")
