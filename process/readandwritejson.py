import json
import datetime
import json

def write_res(res):
    # Read the existing data from the JSON file
    with open('process/data.json', 'r') as json_file:
        data = json.load(json_file)

    # Initialize the temp dictionary to store updated counts
    temp = data.copy()
    print(temp.keys())
    # Update the counts based on the res input
    for i in res:
        if i in temp.keys():
            temp[i] += 1
        else:
            temp[i] = 1
    sorted_temp = dict(sorted(temp.items()))
    # Write the updated data back to the JSON file
    with open('process/data.json', 'w') as json_file:
        json.dump(sorted_temp, json_file, indent=4)



