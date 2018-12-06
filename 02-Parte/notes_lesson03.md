# Python Introduction - Control Flow `Lesson03`

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

## _Conditional statements_

Note que no Python diferentemente de outras linguagem de programação não possui o maldito abre e fecha de `{}` para definir quando um _conditinal statement_ começa e termina, por este motivo a identação é fundamental para que a linguagem seja interpretada corretamente pelo compilador.

O exemplo abaixo possui dois _if_'s _nested_.

```
if condição
|---|------------------|      # 1: Espaços necessários para identar corretamente;
| 1 |        2         |      # 2: área do código que deverá ser executada caso
|---|------------------|      #    a condição seja verdadeira
    if condição2
    |---|---------------------|  # 3: Espaços necessários para identar corretamente;
    | 3 |         4           |  # 4: área de código
    |---|---------------------|
    else
    |---|---------------------|
    | 3 |         4           |
    |---|---------------------|
else
|---|------------------|
| 1 |        2         |
|---|------------------|
```

#### `if()`
```
if dinheiro < 200       # Condição
    dinheiro += 200     # Ações caso a condição
    banco -= 200        # seja satisfeita
```
É o principal _conditional statement_ e serve para filtrar, separar, eleger etc. algum elemento para sofrer uma determinada sequencia de comandos.

#### `else`
```
if dia ==   chuvoso       # Condição
    dinheiro += 200     # Ações caso a condição
    banco -= 200        # seja satisfeita
```





#### `elif()`
