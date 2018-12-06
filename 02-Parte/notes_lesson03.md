# Python Introduction `Lesson03`

#### Tags
* Título: Control Flow
* Autor: AH Uyekita
* Data: 05/12/2018
* Cod: nd110

## Control Flow
Nesta aula serão abordados temas como:

* _Conditional statements_ (Famoso _if_ e _else_)
* Expressões booleanas
* Loops usando _for_ e _while_
* Como uma estratégia de parada dos loops _break_ e _continue_
* Zip e enumarate (Isso eu num sei o que é)
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

## _Conditional statements_

Note que no Python diferentemente de outras linguagem de programação não possui o maldito abre e fecha de `{}` para definir quando um _conditinal statement_ começa e termina, por este motivo a indentação é fundamental para que a linguagem seja interpretada corretamente pelo compilador. **Não se esquecer do `:`**.

O exemplo abaixo possui dois _if_'s _nested_.

```
if condição:
|---|------------------|      # 1: Espaços necessários para indentar corretamente;
| 1 |        2         |      # 2: área do código que deverá ser executada caso
|---|------------------|      #    a condição seja verdadeira

else:
    if condição2:
    |---|---------------------|  # 3: Espaços necessários para indentar corretamente;
    | 3 |         4           |  # 4: área de código
    |---|---------------------|
    else:
    |---|---------------------|
    | 3 |         4           |
    |---|---------------------|
```

#### `if()`
```{py}
if dinheiro < 200:      # Condição
    dinheiro += 200     # Ações caso a condição
    banco -= 200        # seja satisfeita
```
É o principal _conditional statement_ e serve para filtrar, separar, eleger etc. algum elemento para sofrer uma determinada sequencia de comandos.

#### `else`
```{py}
if (numero % 2) == 0:                # Se o resto for igual a zero, é um número par
    print(str(numero) + " é par")    # Imprime texto se a condição for verdadeira
else:
    print(str(numero) + " é ímpar")  # Imprime texto se a condição for falsa.
```
É o complemento do _if_ e não requer condição (já que é o resto da condição do _if_), possui uma dualidade entre `0` e `1`, mas em alguns casos há mais de dois estados, nestas situações usa-se o `elif()`.

#### `elif()`
```{py}
if numero > 100:
    print("maior que 100")

elif numero > 50:
    print("maior que 50 e menor e igual a 100")

else:
    print("número menor ou igual a 50")
```
Note que o o `elif()` é um intermediário entre o `if()` e o else, onde ele desempenha um papel de diminuir a quantidade de _nested if_.
