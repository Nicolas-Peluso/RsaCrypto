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
    print("cripto -- RSA --");
    print("1-) Definir chaves");
    print("2-) criptografar ");
    print("3-) descriptografar ");
    print("4-) sair");


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


def criptografar(chaveE, chaveN, opt):
    Menssagem = str(input("Digite a menssagem a ser criptografada (lembresse que textos não podem ser colados, devem ser escritos no terminal): "));
    if(len(Menssagem) == 0):
        print("menssagem não pode estar vazia");
        
    EncriptaAsc2(Menssagem);

    for index in range(len(asc2Message)):
        C = asc2Message[index] ** chaveE % chaveN;
        encripetedMessage.append(C);
    if(opt == 1):
        print("Tudo certo copie sua menssagem abaixo e lembresse de salvar sua chave privada rsa. (os numeros primos não podem ser usados na descriptografia)");
        print(encripetedMessage);
    else:
        ArqFinal = open("Final.txt", "w");
        for blocks in encripetedMessage:
            ArqFinal.write(str(blocks))
            ArqFinal.write("\n")
        ArqFinal.close()


def descriptografar(Chave, modN, DescriOpt):
    FinalMessage = "";
    for index in range(len(asc2Message)):
        M = encripetedMessage[index] ** Chave % modN;
        FinalMessage += chr(M);
    
    print("SUCESSO");
    print(FinalMessage);


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
        opcao = int(input("digite uma das opções acima"));

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
                    optDescri = int(input(">>"))
                    Private1 = int(input("digite a chave privada: "))
                    ModN = int(input("digite o a chave publica N (DEVE SER A CHAVE N): "))

                    descriptografar(Private1, ModN, DecriptOpt)
            case 4:
                break;
            case _:
                print("opção invalida");

main();
