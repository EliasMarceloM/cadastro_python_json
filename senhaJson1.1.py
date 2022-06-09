import json
#-------cria a senha no json 
dadosUsuario = {"usuario":"",
  "senha": ""
}
f = open("senha.json", "w")
dadosUsuario["usuario"] = input("cadastre um usuario:") #grava a senha 
dadosUsuario["senha"] = input("cadastre um senha:") #grava a senha 

f.write(json.dumps(dadosUsuario,indent=1)) # grava a usuário no json 
#-------cria a senha no json 

#-------verifica se o usuário e senha são corretos  

jsonDadosUsuario = {
  "usuario": "xxxxx",
  "senha": "xxxxx"
}
f = open("senha.json", "r") # abre o json 
#print(type(f))

jsonDadosUsuario = json.load(f) 
'''
for x in jsonDadosUsuario.values():
  print(x)
  print(passada)
'''
''' 
print(jsonDadosUsuario["usuario"])
print(jsonDadosUsuario["senha"])
'''
dadosUsuario["usuario"] = input("cadastre um usuario:") #grava a senha 
dadosUsuario["senha"] = input("cadastre um senha:") #grava a senha 
if dadosUsuario["usuario"] == jsonDadosUsuario["usuario"]:
  print("usurário correto")
else:
  print("usurário errado")
if dadosUsuario["senha"] == jsonDadosUsuario["senha"]:
  print("senha correta")
else:
  print("senha errada")
#-------verifica se o usuário e senha são corretos
f.close()