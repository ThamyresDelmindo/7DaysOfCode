import requests
import json

personagens = requests.get("https://last-airbender-api.fly.dev/api/v1/characters") 

respostaPersonagens = personagens.json()

print("Desafio #1".upper().center(165))
print()
print("#7DaysOfCode".upper().center(165))
print()
print("Avatar a Lenda de Aang - Personagens".upper().center(165))

print("_" * 165)

print("Personagens".upper().center(25) + 
"|" + "Grupo".upper().center(25) + 
"|" + "Inimigos".upper().center(25) + 
"|" + "Aliados".upper().center(25) + 
"|" + "ID Personagem".upper().center(30) +
"|" + "Foto Personagem".upper().center(30)
)
print("_" * 165)

for personagem in respostaPersonagens:
    nome = personagem.get("name")
    grupo = personagem.get("affiliation", "Sem grupo")
    inimigos = personagem.get("enemies", [])
    if isinstance(inimigos, list) and inimigos:
        inimigos_listas = ", ".join(inimigos)
    else:
        inimigos_listas = "Nenhum"
    aliados = personagem.get("allies", [])
    if isinstance(aliados, list) and aliados:
        aliados_listas = ", ".join(aliados)
    else:
        aliados_listas = "Nenhum"
    id = personagem.get("_id", "Sem id")
    foto = personagem.get("photoUrl")
    if not foto:
        foto = "Sem foto"

    print(nome[:25].center(25) + 
    "|" + grupo[:25].center(25) + 
    "|" + inimigos_listas[:25].center(25) + 
    "|" + aliados_listas[:25].center(25) + 
    "|" + id[:25].center(30) +
    "|" + foto[:25].center(30)
    )

print("_" * 165 )


#formatação alfabética, mas ainda ruim no visual
#print(
#    json.dumps(
#        respostaPersonagens, 
#        indent=2, 
#        ensure_ascii=False, 
#        sort_keys=True
#    )
#)

#imprime o json in natura
#print(respostaPersonagens)

#Imprime em lista somente os nomes dos personagens
    #for personagem in respostaPersonagens:
       #    print(personagem["name"])