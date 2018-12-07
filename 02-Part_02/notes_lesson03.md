# Python Introduction `Lesson03`

#### Tags
* Título: _Control Flow_
* Autor: AH Uyekita
* Data início: 05/12/2018
* Data fim: 06/12/2018
* Cod: nd110

## _Control Flow_
Nesta aula serão abordados temas como:

* _Conditional statements_ (Famoso _if_ e _else_)
* Expressões booleanas
* Loops usando _for_ e _while_
* Como uma estratégia de parada dos loops _break_ e _continue_
* Zip e enumerate (Isso eu num sei o que é)
* List comprehensions (idem, _no idea_)

### Revisão da `Lesson02`

|Data Structure|Ordered|Mutable|Constructor|Example|
|:-:|:-:|:-:|:-:|:-:|
|int|NA|NA|`int()`|5|
|float|NA|NA|`float()`|6.5|
|string|Yes|No|' ' ou " " ou `str()`|"teste"|
|bool|NA|NA|NA|`True` ou `False`|
|list|Yes|Yes|[  ] ou `list()`|list[1,2]|
|tuple|Yes|No|( ) ou `tuple()`|tuple(1,2)|
|set|NA|Yes|{ } ou `set()`|set(1,2)|
|dictionary|NA|Keys: No|{ } ou `dict()`|dict("jul":1,"jun":2)|

Maiores informações acerca das `built-in` _functions_ e `methods` somente acessando as [notes_lesson02.md](https://github.com/AndersonUyekita/udacity_data_science_foundation_01/blob/master/02-Parte/notes_lesson02.md).

## Expressões Booleanas

Algumas expressões booleanas dignas de nota:

#### a < b < c ou a > b > c

Essa expressão pode ser uma condição de avaliação de uma _conditinal statement_, por exemplo.

```{py}
# Exemplo do video
if 18.5 <= weight / height**2 < 25:       # A relação weight / height**2 deve estar
    print("BMI is considered 'normal'")   # entre 18.5 e 25 para que a condição seja aceita
```

**********************************************************
## _Conditional statements_

Note que no Python diferentemente de outras linguagem de programação não possui o maldito abre e fecha de `{}` para definir quando um _conditinal statement_ começa e termina, por este motivo a indentação é fundamental para que a linguagem seja interpretada corretamente pelo compilador. **Não se esquecer do `:`**.

O exemplo abaixo possui dois _if_'s _nested_.

```
if condição:
+---+------------------+      # 1: Espaços necessários para indentar corretamente;
| 1 |        2         |      # 2: área do código que deverá ser executada caso
+---+------------------+      #    a condição seja verdadeira

else:
    if condição2:
    +---+---------------------+  # 3: Espaços necessários para indentar corretamente;
    | 3 |         4           |  # 4: área de código
    +---+---------------------+
    else:
    +---+---------------------+
    | 3 |         4           |
    +---+---------------------+
```

### `if()`
```{py}
if dinheiro < 200:      # Condição
    dinheiro += 200     # Ações caso a condição
    banco -= 200        # seja satisfeita
```
É o principal _conditional statement_ e serve para filtrar, separar, eleger etc. algum elemento para sofrer uma determinada sequencia de comandos.

### `else`
```{py}
if (numero % 2) == 0:                # Se o resto for igual a zero, é um número par
    print(str(numero) + " é par")    # Imprime texto se a condição for verdadeira
else:
    print(str(numero) + " é ímpar")  # Imprime texto se a condição for falsa.
```
É o complemento do _if_ e não requer condição (já que é o resto da condição do _if_), possui uma dualidade entre `0` e `1`, mas em alguns casos há mais de dois estados, nestas situações usa-se o `elif()`.

### `elif()`
```{py}
if numero > 100:
    print("maior que 100")

elif numero > 50:
    print("maior que 50 e menor e igual a 100")

else:
    print("número menor ou igual a 50")
```
Note que o o `elif()` é um intermediário entre o `if()` e o else, onde ele desempenha um papel de diminuir a quantidade de _nested if_.

**********************************************************
## _Loops_

As estruturas (que seriam os bloquinhos de código) do _f0r_ e do _while_ são parecidos com aqueles do _conditional statements_, pois os _loops_ baseiam-se também pela indentação do código.

```
for condição:
+---+------------------+      # 1: Espaços necessários para indentar corretamente;
| 1 |        2         |      # 2: área do código que deverá ser executada caso
+---+------------------+      #    a condição seja verdadeira
```

### `for()`
```{py}
for i in n:     # i é a variável e n é uma lista de elementos
    print(i)    # imprime todos os elementos da lista n
```
O laço for será executado para cada elemento da lista _n_. Após percorrer a lista o laço termina.

### `while()`
```{py}
money = 0
while money < 1000:     # o laço será executo indefinidamente até que a condição seja False
    money += 100        # imprime money
```
A diferença entre _for_ e _while_ é que o segundo não possui limites, ele poderá ser executado indefinidamente até que a condição de parada seja atingida.

## _List Comprehensions_

Isso é algo único da linguagem Python, segundo a **Juno Lee** só em Python tem essa coisa aí.

```{py}
minha_lista = ["anderson", "hitoshi", "uyekita"] # Lista qualquer
nova_lista =[] # Uma nova lista

# Um loop de exemplo.
for nom in minha_lista:
    nova_lista.append(nom.title())

print(nova_lista) # imprime o resultado para comparar

# Em uma linha faz-se tudo.
nova_lista = [nom.title() for nom in minha_lista]

print(nova_lista) # para conferir.
```

Note que o mesmo código que foi feito utilizando algumas linhas, pode ser realizada usando uma única linha.

**********************************************************
## Built-in functions

Esta será um lista das funções e qualquer outra coisa que foi apresentado em sala de aula.

### `range()`
```{py}
start,end,step = 1,6,2 # inicializa os dados
                            # start possui valor default de zero
                            # step possui valor default de 1
lista = range(1,6,2)   # cria um objeto classe range
                            # print(lista) é um <class 'range'>
                             # A lista implícita é: [1, 3, 5]
```
A variável criada _lista_ é um objeto de classe _range_ e só será útil se caso a utilize em associação com o _for_ (ainda não encontrei outras casos de uso do `range()`).

### `sum()`
```{py}
minha_lista = [10, 20, 30, 40] # Um exemplo de lista
sum(minha_lista)               # Retorna a soma dos elementos da lista
```
Simplesmente retorna a soma de todos os elementos de dada lista.

### `Break`

Interrompe a instância de _for_ ou _while_ saindo totalmente do laço.

### `Continue`

Pula a iteração para a próxima. É melhor porque não interrompe repentinamente a execução do _script_.

### `zip()`
```{py}
nome = ["anderson", "hitoshi", "uyekita"] # Uma lista qualquer
index = [1, 2, 3]                         # Outra lista qualquer
print(zip(nome,index))                    # Unindo as duas listas para criar uma lista de tuples
                                          # Note que se pode usar o unpacking também
```
Observe que é possível criar uma lista de _tuple_'s, conforme o exemplo acima, mas para realizar o _unpacking_ deve-se utilizar um "operador" que ainda não foi abordado, mas de uso específico que é o "*".

```{py}
lista_tuples = [('anderson', 1), # lista qualquer de tuples
                ('hitoshi', 2),  # é só um exemplo
                ('uyekita', 3)]

nome, index = zip(*lista_tuples) # Unpacking usando o *
```
Isso é bem prático quando tempos uma lista de _tuple_'s.

### `enumerate`
```{py}
letters = ['anderson', 'hitoshi', 'uyekita']  # Uma lista qualquer.

for i in enumerate(letters):                  # Cria uma lista de tuple's.
    print(i)                                  # Imprime cada tuple da lista criada.
```
A única maneira de entender essa função é aplicando a num _for_. O resultado é a criação de _tuple_'s.

**********************************************************
## Methods

### `.items()`
```{py}
apelidos = {"Chico": 'Francisco',    # Declarando uma biblioteca
            "Tião": 'Sebastião',
            "Zé": 'José'}

for key,value in apelidos.items():   # Emprego do .items()
    print("Apelido: {} e Nome:{}".format(key,value))
```

Nos casos onde é necessário as informações dos _values_ de uma biblioteca, usa-se o `.items()`.
