# Python Introduction `Lesson05`

#### Tags
* Título: Functions
* Autor: AH Uyekita
* Data início: 06/12/2018
* Cod: nd110

## _Scripting_

Escrever e editar _scripts_, tendo até entradas de dadas externas (_inputs_) do usuário.

### Conteúdo da aula

Essa lição abordou:

* Python Installation and Environment Setup
* Running and Editing Python Scripts
* Interacting with User Input
* Handling Exceptions
* Reading and Writing Files
* Importing Local, Standard, and Third-Party Modules
* Experimenting with an Interpreter

## Erros e Exceções

Os _Syntax Erros_ são quando o compilador não consegue interpretar o código, isto pode ser ocasionado por uma má digitação (famoso _typo_). Seguramente, esses erros podem ser corrigidos antes de executar o código.

Ao passo que as _Exceptions_ são mais complexos, pois o compilador conseguiu ler, mas há alguma inconsistência. Note que esse erro ocorre durante a execução do programa. Há diferentes tipos de _exceptions_:

#### ValueError
```{py}
x = int(input("Digite um número: "))
```
Caso a entrada seja um texto, por exemplo, "ten". Ocorrerá o problema de _ValueError_.

Tradução: Quando o objeto está correto, mas o valor declarado/passado como input é inapropriado para aquela função (_built-in_ ou auela que criamos mesmo).

#### AssertionError:
Tradução: Quando uma condição assetiva falha...

#### NameError
```{py}
# ValueError: Quando a variável a não foi declarada ainda
sum(a + 1)
```
#### IndexError:
```{py}
teste = ["a","b"]

print(teste[100])
```
Ultrapassagem dos limites de uma lista.

#### TypeError
```{py}
# TypeError: Tipo erro de quando soma _str_ com _int_
sum("a" + 1)
```
Tentar somar um _str_ com um _int_.

**********************************************************
## Built-in functions

Esta será um lista das funções e qualquer outra coisa que foi apresentado em sala de aula.

### `input()`
```{py}
qualquer_coisa = input("Escreva-me algo interessante: ")
print(str("Isso é interessante hein!") + qualquer_coisa)
```
Pode-se obter informações a partir de entradas usando o _input_. Esse dado de entrada pode ser transformado em _int_, _float_ etc..

### `try()`



### `except()`




### `finally()`
