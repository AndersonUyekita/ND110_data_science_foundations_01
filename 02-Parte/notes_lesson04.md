# Python Introduction `Lesson04`

#### Tags
* Título: Functions
* Autor: AH Uyekita
* Data início: 06/12/2018
* Cod: nd110

## _Functions_

A função nada mais é que a abstração de uma rotina (ou _script_) encapsulado num simples _call_ de uma função _built-in_ (parece mas não é _built-in_ porque nós que a criamos).

### Conteúdo da aula

Essa lição abordou:

* Defining Functions
* Variable Scope
* Documentation
* Lambda Expressions
* Iterators and Generators

### Estrutura de uma função

A função possui uma estrutura que deve ser seguida para que o devido funcionamento.

* Sempre começa com `def`;
* Deve ser indentada;
* Possui argumento;
* Pode ou não retornar (_return_) algum valor (_None_ se não for retornar nada).

```
def my_function(arg1, arg2)
+---+----------------------------+
|   |                            |
| 1 |           2                |
|   |return                      |  # Note que não é uma exigência que tenha o return
+---+----------------------------+

1: área de indentação
2: área de código
```
Ressalta-se que as funções podem ter variáveis locais (_local variable_), isto é, as variáveis internas à função não afetam o _environment_ externo dela (aqui eles chamam de _variable scope_). Contudo, as variáveis definidas no _global scope_ podem ser usadas dentro da função e podem ser até modificadas caso essa variável for um dos argumentos da função.

Além disso, pode-se declarar variáveis _default_ para cada argumento (igual o R). Outra similaridade com o R é com relação ao uso da função.

* Declarar argumentos por posição: my_function(10,5)
* Declarar argumentos por nomes: my_function(arg2 = 5, arg1 = 10)

### _Lambda Expressions_

Não deixa de ser uma função, mas com um escopo menor, não possui nome (por isso que é uma função anônima) e provelmente será empregada para fins mais simples. Abaixo uma comparação entre uma função dita normal/convencional e a lambda.

```{py}
# Função convencional
def multiply(x, y):
    return x * y

# Lambda Expression
multiply = lambda x, y: x * y
```
Note que é possível reduzir a quantidade de linhas, mas o principal é não ter que definir um novo nome para uma função que provavelmente não terá muito uso ao longo do corpo do código.

Conforme a **Juno Lee** as _lambdas expressions_ tornarão importantes no futuro, quando o a quantidade de funções definidas é grande, isto é, fazendo-se pequenas alterações ou combinações entre as funções já definidas o poder da _lambda expression_ pode ser muito grande. Só evoluindo para confirmar isso.

Um exemplo de como podemos associar funções regulares com o _lambda expressions_.

```{py}
def teste(arg1):    # Eleva ao quadrado
    return arg1**2

def teste2(arg2):   # Divide por 100
    return arg2/100

teste3 = lambda x,y: teste(x) * teste2(y) # Lambda Expression que usa as duas funções

print(teste3(3,1)) # Espera-se que imprima o resultado de 9/100
```

## _Documentation_

Asssim já como comentado na `Lesson02`, documentação nada mais que as boas práticas da programação.

* Explicar de maneira clara e concisa o que essa função faz;
* Quais são as entradas e que tipo de variáveis são (`int`, `float`, `list` etc.);
* Qual é a saída (`None`, `list`, `dict` etc.).

Conforme a convenção do PEP (eu acho que é isso) tem uma forma de anotar a documentação que é:

* Usar três `"` para abrir a documentação e outros três para fechar;
* Primeira linha: Discorrer sobre o uso geral da função;
* INPUT: quais são;
* OUTPUT: qual é.

Agora um exemplo de como comentar:

```{py}
def my_function(arg1,arg2):
    """
    Função que não faz nada só serve como exemplo

    INPUT: arg1 é um int - É o tamanho da minha paciência em escrever essas anotações
    OUTPUT: arg2 é um flota - É a expectativa de dias melhores
    """
```

**********************************************************
## Built-in functions

Esta será um lista das funções e qualquer outra coisa que foi apresentado em sala de aula.

### `map()`
```{py}
my_df = [[10,20,30],[5,5,10],[1,50,1]] # Criei uma lista de lista

print(map(sum,my_df)) # Para cada lista irá aplicar a soma
                      # [60, 20, 52]
```
É como se estivesse aplicando as funções da família `apply`.

### `filter()`
```{py}
my_df = [10,20,30] # lista qualquer

teste = lambda x : x > 20 # lambda expression para avaliar

print(filter(teste,my_df)) # filter
                           # retornará os valores que forem avaliados como True da função lambda teste
```
Filtra os elementos com base numa função que avalia.

## Referências para Iteratos e Generators

https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
