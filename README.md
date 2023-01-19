# RsaCrypto
No canal Fabrica de noobs no youtube eu assiti um video muito bom sobre criptografia rsa, resolvi criar um systema que criptografa.

<h3>Como usar função definir chaves"</h3>
     <p>Defina dois numeros primos esses numeros não devem se compartilhados com ninguem quanto maior os primos mais seguro
     defina N entre 1 e f(N) desde de que N não tenha um divisor comum com f(N) desconsiderando o 1
     Caso o numero tenha algum divsor com f(N) você tera de escolher outro até achar um que satisfaça
     Em caso de Erro 'Não há inverso multiplicativo modular para este número' voce dvera repetir o passo 2
     Guarde as chaves privadas e as publicas a chaves publicas pode ser compartilada com qualquer um as privadas não</p>

<h3>o usar função Criptografar</h3>
     <p>Escolha Se voce quer criptografar uma menssagem pequena no terminal ou um texto grande em um arquivo
     Em ambos os casos Passe a chave Publica E e depois a chave publica N
     Caso escolha a opção 1 digite a menssagem no terminal, e copie a messagem criptografada
     Caso escolha a opção 2 Voce deve ter um arquivo chamado Entrada.txt na raiz do projeto esse arquivo deve conter o texto a ser criptografado
     Após a criptografia ser realizada um arquivo chamado 'Final.txt' sera gerado o Arquivo 'Entrada.txt' com o texto original pode ser deletado</p>

<h3>o usar função Descriptografar</h3>
    <p>Escolha Se voce quer Descriptografar uma menssagem pequena no terminal ou um texto grande em um arquivo
    Em ambos os casos Passe a chave privada (NÂO OS NUMEROS PRIMOS ESCOLHIDOS) e depois a chave publica N
    Caso escolha a opção 1 digite a Cole os blocos criptorgrafados no terminal, se tudo correr bem voce tera sua menssagem original
    Caso escolha a opção 2 Voce deve ter um arquivo chamado Final.txt na raiz do projeto esse arquivo deve conter os blocos criptografados
    Nesse mesmo arquivo Final.txt sera gerado o texto original
    BRASSE QUE SE VOCE PERDER A CHAVE PRIVADA NÃO TEM COMO RECUPERAR O ARQUIVO ORIGINAL
    voce ja possui as chaves publicas e privadas voce não precisa criar novamente as chaves</p>

<h1>e programa foi desenvolvido por um estudante da computação para fins didaticos. <strong>não</strong> o use para criptografar arquivos senssiveis, use-o por sua conta e risco</h1>