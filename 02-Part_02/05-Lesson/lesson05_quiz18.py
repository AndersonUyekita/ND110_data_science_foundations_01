# Primeira parte
with open("camelot.txt") as song: # Carrega arquivo
    print(song.read(2)) # We
    print(song.read(8)) # 're the
    print(song.read())  # knights of the round
                        # We dance whenever we're able

# O argumento do read() determina a quantidade de caracteres que serão lidos
# Nota-se que os espaços são caracteres também e há um tipo
# de fatiamento caso a leitura não seja completa.

print("\n")

# Segunda parte após alterações
camelot_lines = [] # Cria lista

with open("camelot.txt") as f: # Carrega arquivo
    for line in f:
        camelot_lines.append(line.strip()) # Agrega numa lista palavra por palavra por causa do .strip()
                                           # Cada verso será um elemento

print(camelot_lines) # imprime a lista

print("\n")

# Terceiro - O meu caso sozinho
with open("camelot.txt") as f: # Carrega arquivo
    print(f.read())

# Fiquei curioso e quis imprimir todo o arquivo f para conferir como ficava.
