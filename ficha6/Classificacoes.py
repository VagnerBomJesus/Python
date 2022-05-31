def ClassifTotais(Chave, Cotacao, Resp):
    print(f"\n Aluno Classificação")
    for A in range(0, Resp.shape[0]):
        final = (Resp[A] == Chave)*Cotacao
        print(f"{A+1:^5}{final.sum():^15}")
