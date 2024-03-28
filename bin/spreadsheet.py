import pandas as pd
import os
import openpyxl


###############################################################
EXP="eoe"
DIR=f"{os.getcwd()}/tmp/"

directory_in=f"{DIR}Download/pack/{EXP}/"
directory_out=f"{DIR}saida/{EXP}/"

if not os.path.exists(directory_in):
    os.makedirs(directory_in)
if not os.path.exists(directory_out):
    os.makedirs(directory_out)

def pq(var):
    from pprint import pprint
    pprint(var)
    quit()


############################################################
# Transforma as planilhas (PT) em Json traduzidos (PT)
def sheet2json():
    json_path=f"{directory_out}"
    sheet_path=f"{directory_in}_{EXP}.xlsx"

    # Carrega Excel para Dataframe
    df = pd.read_excel(sheet_path, engine='openpyxl', sheet_name=None)

    for sheet_name, sheet in df.items():
        print("-------------------------------")
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
        with open(json_path+sheet_name+".json", 'w+') as json_file:
            json_file.write(json_data)

############################################################
# Converte os Json (EN) nas planilhas para traduzir (PT)
def json2sheet():
    # planilha gerada com os json
    sheet_path=f"{directory_out}_{EXP}.xlsx"

    # Verifica se existe planilha antes de processar
    if not os.path.isfile(sheet_path):
        openpyxl.Workbook().save(sheet_path)

    # Varre diretorio em busca dos arquivos
    for filename in os.scandir(directory_in):
        if filename.is_file(): # and filename.endswith(".json")
            print("------------------------------")
            print(filename.name)
            df = pd.read_json(filename.path)

            # Converte e grava JSON nas Planilhas
            with pd.ExcelWriter(sheet_path, engine="openpyxl", mode="a") as writer:
                df.to_excel(writer, sheet_name=filename.name[:-5], index=False, )



###############################################################
print("O que deseja gerar:")
print("1) Planilha para traduzir")
print("2) JSON traduzidos")
match input():
    case "1" :
        json2sheet()
    case "2" :
        sheet2json()
    case _:
        print("Opção invalida")
        quit()