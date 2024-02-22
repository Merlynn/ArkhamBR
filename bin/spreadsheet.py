import pandas as pd
import os


###############################################################
directory="/home/merlynn/Development/Arkham/ArkhamBR/tmp/"
json_path="/home/merlynn/Development/Arkham/ArkhamBR/tmp/saida/"
sheet_path="/home/merlynn/Development/Arkham/ArkhamBR/tmp/core.xlsx"

###############################################################
def sheet2json():
    # Load Excel to DataFrame
    df = pd.read_excel(sheet_path, engine='openpyxl', sheet_name=None)

    for sheet_name, sheet in df.items():
        print("-------------------------------")
        # Convert DataFrame to JSON
        print(sheet_name)
        json_data = df[sheet_name].to_json(orient='records', indent=4, )
        # Write JSON data to a file
        with open(json_path+sheet_name+".json", 'w') as json_file:
            json_file.write(json_data)


def json2sheet():
    for filename in os.scandir(directory):
        if filename.is_file():
            print("------------------------------")
            print(filename.name)
            df = pd.read_json(filename.path)

            with pd.ExcelWriter(sheet_path, engine="openpyxl", mode="a") as writer:
                df.to_excel(writer, sheet_name=filename.name[:-5], index=False)

###############################################################

sheet2json()

#json2sheet()