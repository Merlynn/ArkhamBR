import pandas as pd
import json
import os


###############################################################
DIR=os.getcwd()
directory=f"{DIR}\\tmp\\ptc\\"
json_path=f"{DIR}\\tmp\\saida\\"
sheet_path=f"{DIR}\\tmp\\ptc.xlsx"

def tp(var):
    print(type(var))
    quit()


###############################################################
def sheet2json():
    # Carrega Excel para Dataframe
    df = pd.read_excel(sheet_path, engine='openpyxl', sheet_name=None)

    for sheet_name, sheet in df.items():
        print("-------------------------------")
        # Convert DataFrame to JSON
        print(sheet_name)

        sheet_json = pd.DataFrame(sheet)

        # Removendo coluna 'status'
        if 'status' in sheet_json:
            sheet_json = df[sheet_name].drop(['status'], axis=1)

        # Fix 5 digitos para 'code'
        if 'code' in sheet_json:
            sheet_json['code'] = sheet_json['code'].map(lambda x: f'{x:0>5}')
            #pass

        # Drop valores NaN
        sheet_json = sheet_json.apply(lambda x: [x.dropna()], axis=1)

        json_data = sheet_json.to_json(indent=4)

        # Gravar Json no arquivo
        with open(json_path+sheet_name+".json", 'w') as json_file:
            json_file.write(json_data)


def json2sheet():
    for filename in os.scandir(directory):
        if filename.is_file():
            print("------------------------------")
            print(filename.name)
            df = pd.read_json(filename.path)

            with pd.ExcelWriter(sheet_path, engine="openpyxl", mode="a") as writer:
                df.to_excel(writer, sheet_name=filename.name[:-5], index=False, )

###############################################################

#sheet2json()

json2sheet()