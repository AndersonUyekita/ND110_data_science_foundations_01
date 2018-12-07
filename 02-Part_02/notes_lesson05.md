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

Os _Syntax Erros_ são quando o "interpretador do código" não consegue interpretar o código, isto pode ser ocasionado por uma má digitação (famoso _typo_). Seguramente, esses erros podem ser corrigidos antes de executar o código.

Ao passo que as _Exceptions_ são mais complexos, pois o "interpretador do código" conseguiu ler, mas há alguma inconsistência. Note que esse erro ocorre durante a execução do programa. Há diferentes tipos de _exceptions_:

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
## _Importing scripts_

Geralmente todo _script_ importado deve ser declarado, por convenção, no início do arquivo.

```{py}
import my_script
```
O local desse _script_ tem que ser no mesmo diretório.

```
meu_recente_trabalho.py
|
+-my_script.py
```

**********************************************************
## `Built-in` _functions_

Esta será um lista das funções e qualquer outra coisa que foi apresentado em sala de aula.

### `input()`
```{py}
qualquer_coisa = input("Escreva-me algo interessante: ")
print(str("Isso é interessante hein!") + qualquer_coisa)
```
Pode-se obter informações a partir de entradas usando o _input_. Esse dado de entrada pode ser transformado em _int_, _float_ etc..

### `try()`
```{py}
try:     # Opção a prova de tonterías
    int(input("Digite um número legal: "))  # Digita um número aí... 51
except:  # Caso o operador faça uma burrada o script não vai interromper bruscamente
    print("Tá de sacanagem né!? Eu pedi um número e não uma string!")  # Vai chamar a atenção dele.
```
O _try statement_ juntamente com o `except()` possibilitará que o programador utilize diferentes estratégias para contar possíveis problemas de _inputs_, neste caso exemplo, aparecerá apenas um aviso e nada mais, há a possibilidade de retornar a solicitar um número, mas esse deve ser feito com um _loop_ `while()`.

```{py}
while True:  # Com esse loop o script fica teimoso, só sai quando o operador inserir um número.
    try:
        x = int(input("Digite um número legal: "))
        break # Depois de muita teimosia, por fim, digitou um número. Daí sai do While infinto.
    except:
        print("tá de sacanagem né!?")

print("Se você ler isso é que saiu do loop") # Só para enviar uma mensagem de aviso
```
Observe que se não fosse o `try()` este _script_ teria sido interrompido.

### `except()`
```{py}
while True:
    try:
        x = int(input("Digite um número legal: "))
        break
    except ValueError:
        print("tá de sacanagem né!?")
	  except KeyboardInterrupt:
        print("Apertou Ctrl+C")
        break
    finally:
        print("Digite um valor válido")
```
Note que o `except()` pode ter formas específicas de atuação:

* ValueError: Quando um valor não esperado é atribuído, neste caso quando se digita um texto ao invés de um número;
* KeyboardInterrupt: Quando se interrompe o _script_ ao apertar o <kbd>Ctrl+C</kbd>.

### `finally()`
```{py}
while True:
    try:
        x = int(input("Digite um número legal: "))
        break
    except:
        print("tá de sacanagem né!?")
    finally:
        print("Digite um valor válido")
```
O `finally()` será executado sempre caindo no `try()` ou no `except()`. Não vi muita utilidade **agora**, mas em breve entenderei mais sobre o uso dele. A _Juno Lee_ disse que há um uso muito interessante para os casos de usar o `try()` para carregar (_load_) arquivos, pois quando isso é feito (não sei o porquê) abre-se alguma coisa (ótimo hein) e o `finally()` serviria para fechar essa "abertura".

> Lendo o link do [Stack](https://stackoverflow.com/questions/11551996/why-do-we-need-the-finally-clause-in-python), pode ser útil quando há um `return` no `except`, neste caso o `finally()` será executado **antes** do return.

### `open()`
```{py}
data = open("path/file.txt","r")  # Carregando um arquivo txt localizado pelo path.
                                  # O argumento "r" significa read only.
dataset = data.read()
data.close()
```
O resultado do `open()` será um _file object_, caso seja necessário alguma alteração neste arquivo que é apenas leitura, pode-se usar o _method_ `.read()` para acessar o conteúdo desse arquivo.

Ressalta-se também que o argumento pode ser alterado para `w`, o que significa que o arquivo estará sendo aberto para ser gravado. Tenha cuidado porque o conteúdo desse arquivo será deletado para ser sobreescrito. O `method` usado para a gravação é o `.write()`.

## `Methods`

### `.read()`
```{py}
data = open("path/file.txt","r")  # Carregando um arquivo txt localizado pelo path.
                                  # O argumento "r" significa read only.
dataset = data.read()
data.close()
```
Este _method_ transforma o _file object_ numa string, sendo assim possível a edição e análise.

### `.close()`
```{py}
data = open("path/file.txt","r")  # Carregando um arquivo txt localizado pelo path.
                                  # O argumento "r" significa read only.
dataset = data.read()
data.close()
```
Não me pergunte o por quê, mas se deve fechar o `open()` e por isso que tem essa coisa aqui. Caso isso fique aberto, haverá um uso desnecessário de memória para mantê-lo aberto.

### `.write()`

Serve para gravar um arquivo tipo `txt`.
