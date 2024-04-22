import json

json_text='''
[
    {
        "id": "The_Golden_Rules",
        "title": "As Regras de Ouro",
        "text": "Se o texto deste Guia de Referência contradisser diretamente o texto do Livro de Regras, o texto do Guia de Referência prevalece.\nSe o texto de uma carta contradisser diretamente o texto do Guia de Referência ou do Livro de Regras, o texto da carta prevalece."
    }
]
'''


json_string = json.dumps(json_text)

print(json_string)

