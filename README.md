# copilador-2020
## Compilador desenvolvido em python para a cadeira de compiladores

*Utilizar python3.6 ou mais atual

## Instalar dependências
pip install -r requirements.txt

## Compilador
Foi desenvolvida uma tela para o compilador que pode ser executada da seguinte maneira:
*python compilador/interface_compilador.py*

Nesta interface, um código pode ser carregado e compilado. O código carregado fica à direita e o compilado à esquerda. Esta interface também mostra alertas de erro na compilação e indica qual a linha do erro.

Ao compilar, é chamado o analisador léxico que limpa e tokeniza o código, verificando se cada token faz parte da linguagem e criando uma tabela de tokens.
Em seguida o analisador sintático consome os tokens da tabela, verifica a estrutura ao mesmo tempo em que gera o código de saída por instrução semânticas inseridas junto da análise sintática.

Após compilado, um arquivo .txt é criado na pasta do compilador, com o nome *cod_saida.txt* com a mesma saída observada no lado direito da interface do compilador, em caso de sucesso.

## Máquina virtual
Foi desenvolvida uma interface de máquina virtual onde é possível carregar o arquivo *cod_saida.txt* e verificar a execução do código gerado. É possível colocar breakpoints, e ver o que acontece na representação da pilha da máquina.

## Arquivos de apoio

Todas as instruções do código de saída podem ser consultadas no arquivo *Instruções.pdf*

A gramática utilizada está no arquivo *gramatica_sintatico.txt*

Um exemplo de código de entrada pode ser visto no arquivo *entrada_semantico.txt*


