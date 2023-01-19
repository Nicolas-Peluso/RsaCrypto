asc2Message = [];
publicKey = [];
privateKey = [];
encripetedMessage = [];

def VerificaPrimo(p, q):
    PePrimo = False;
    QePrimo = False;

    for divisor in range(2, p):
        if(p % divisor != 0):
            PePrimo = True;
        else:
            PePrimo = False;
            break;
    
    for divisor in range(2, q):
        if(q % divisor != 0):
            QePrimo = True;
        else:
            QePrimo = False;
            break;

    if(PePrimo == False):
        print("o Valor de P deve ser um numero primo");
        return False;
    elif(QePrimo == False):
        print("o Valor de Q deve ser um numero primo");
        return False;
    else:
        return True;


def DivisorComum(TotN, n1):
    NumerosTemDivisoresComuns = False;

    for divisor in range(2, TotN):
        if(TotN % divisor == 0):
            if(n1 % divisor == 0):
                NumerosTemDivisoresComuns = True;
                print("Os numeros tem divisores comuns, tente outro");
                break;
            else:
                print("o numero {0} pode ser usado como chave publica".format(n1));
                break;

    return NumerosTemDivisoresComuns


def EncriptaAsc2(menssagem):
    for word in range(len(menssagem)):
        ascword = ord(menssagem[word]);
        asc2Message.append(ascword);
    return asc2Message;


def Painel():
    print("");
    print("#_#_#_#_#_#_#_#_RSA_#_#__#_##_#__##_");
    print("1-) Definir chaves");
    print("2-) criptografar ");
    print("3-) descriptografar ");
    print("4-) Manual")
    print("5-) sair");


def Painel_Criptografar():
    print("");
    print("cripto -- RSA --");
    print("1-) criptografar uma menssagem via terminal (Apenas textos pequenos): ");
    print("2-) criptografar uma menssagem em um arquivo: ");
    print("3-) sair");


def Painel_Descriptografar():
    print("");
    print("cripto -- RSA --");
    print("1-) Descriptografar uma menssagem via terminal: ");
    print("2-) Descriptografar uma menssagem em um arquivo: ");
    print("3-) sair");


def man():
    print("---------Manual---------");
    print("Como usar função definir chaves");
    print("1-) Defina dois numeros primos esses numeros não devem se compartilhados com ninguem quanto maior os primos mais seguro");
    print("2-) defina N entre 1 e f(N) desde de que N não tenha um divisor comum com f(N) desconsiderando o 1");
    print("3-) Caso o numero tenha algum divsor com f(N) você tera de escolher outro até achar um que satisfaça");
    print("4-) Em caso de Erro 'Não há inverso multiplicativo modular para este número' voce dvera repetir o passo 2");
    print("5-) Guarde as chaves privadas e as publicas a chaves publicas pode ser compartilada com qualquer um as privadas não");
    print("");
    print("Como usar função Criptografar");
    print("1-) Escolha Se voce quer criptografar uma menssagem pequena no terminal ou um texto grande em um arquivo");
    print("2-) Em ambos os casos Passe a chave Publica E e depois a chave publica N");
    print("3-) Caso escolha a opção 1 digite a menssagem no terminal, e copie a messagem criptografada");
    print("4-) Caso escolha a opção 2 Voce deve ter um arquivo chamado Entrada.txt na raiz do projeto esse arquivo deve conter o texto a ser criptografado");
    print("5-) Após a criptografia ser realizada um arquivo chamado 'Final.txt' sera gerado o Arquivo 'Entrada.txt' com o texto original pode ser deletado");
    print("");
    print("Como usar função Descriptografar");
    print("1-) Escolha Se voce quer Descriptografar uma menssagem pequena no terminal ou um texto grande em um arquivo");
    print("2-) Em ambos os casos Passe a chave privada (NÂO OS NUMEROS PRIMOS ESCOLHIDOS) e depois a chave publica N");
    print("3-) Caso escolha a opção 1 digite a Cole os blocos criptorgrafados no terminal, se tudo correr bem voce tera sua menssagem original");
    print("4-) Caso escolha a opção 2 Voce deve ter um arquivo chamado Final.txt na raiz do projeto esse arquivo deve conter os blocos criptografados");
    print("5-) Nesse mesmo arquivo Final.txt sera gerado o texto original");
    print("LEMBRASSE QUE SE VOCE PERDER A CHAVE PRIVADA NÃO TEM COMO RECUPERAR O ARQUIVO ORIGINAL");
    print("Se voce ja possui as chaves publicas e privadas voce não precisa criar novamente as chaves");
    print("Esse prgrama foi desenvolvido por um estudante da computação não o use para criptografar arquivos senssiveis, use-o por sua conta e risco");


def criptografar(chaveE, chaveN, opt):
    if(opt == 1):
        Menssagem = str(input("Digite a menssagem a ser criptografada (lembresse que textos não podem ser colados, devem ser escritos no terminal): "));
        if(len(Menssagem) == 0):
            print("menssagem não pode estar vazia");

    if(opt == 2):
        File = open("Entrada.txt", "r");
        text = File.read();
        EncriptaAsc2(text);
        File.close();

    else:
        EncriptaAsc2(Menssagem);

    for index in range(len(asc2Message)):
        C = asc2Message[index] ** chaveE % chaveN;
        encripetedMessage.append(C);

    if(opt == 2):
        ArqFinal = open("Final.txt", "w");
        for blocks in encripetedMessage:
            ArqFinal.write(str(blocks));
            ArqFinal.write("\n");
        ArqFinal.close();

    print("Tudo certo copie sua menssagem abaixo e lembresse de salvar sua chave privada rsa. (os numeros primos não podem ser usados na descriptografia)");
    print(encripetedMessage);
   # else:
     


def descriptografar(Chave, modN, DescriOpt):
    FinalMessage = "";

    if(DescriOpt == 1):
        for index in range(len(asc2Message)):
            M = encripetedMessage[index] ** Chave % modN;
            FinalMessage += chr(M);
    else:
        Arquivo = open('Final.txt', 'r');
        lista = Arquivo.readlines();
        Arquivo.close();

        for line in lista:
            M = int(line) ** Chave % modN;
            FinalMessage += chr(M);
        
        Final = open("Final.txt", "w");
        Final.write(FinalMessage);
        Final.close();

    print("SUCESSO");


def DefinirChaves():
    
    while True:
        if(len(privateKey) > 0):
            print("Voce ja possui chaves cadastradas e não é possivel visualiza-las");
            break;
        
        print("digite os numeros primos para começarmos");
        
        while True:
            p = int(input("digite o valor de p: "));
            q = int(input("digite o valor de q: "));

            if(VerificaPrimo(p, q) == True):
                privateKey.append(p);
                privateKey.append(q);
                break;
        
        n = p*q;
        TotienteN = (p - 1) * (q - 1);
        
        publicKey.append(n);

        while True:
            e = int(input('escolha um numero entre 1 e {0}: (lembrando que o numero não pode ser um divisor comum de {0})'.format(TotienteN)));
            if(DivisorComum(TotienteN, e) == False):
                try:
                    InversoMultiplicativo = pow(e, -1, TotienteN);
                    publicKey.append(e);
                    privateKey.append(InversoMultiplicativo);
                    break;
                except ValueError:
                    print("Não há inverso multiplicativo modular para este número inteiro Escolha outro");


        print("Cahves Criadas com sucesso")
        print("Suas chaves são: ")
        print("Publicas: CHave E: {0}, Chave N: {1}".format(publicKey[1], publicKey[0]))
        print("privada: ", privateKey[2])
        break;


def main():
    while True:
        Painel();
        opcao = int(input(">> "));

        match opcao:
            case 1:
                DefinirChaves();
            case 2: 
                    Painel_Criptografar();
                    criptOpt = int(input(">> "))
                    
                    E = int(input("digite a chave publica E: "));
                    N = int(input("digite a chave publica N: "));
                    criptografar(E, N, criptOpt);
            case 3:
                    Painel_Descriptografar();
                    optDescri = int(input(">> "));
                    Private1 = int(input("digite a chave privada: "));
                    ModN = int(input("digite o a chave publica N (DEVE SER A CHAVE N): "));

                    descriptografar(Private1, ModN, optDescri);
            case 4:
                man()
            case 5:
                break;
            case _:
                print("opção invalida")

main();
