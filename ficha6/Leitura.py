def LeituraRespostas(Resp):
    for A in range(0, Resp.shape[0]):
        for J in range(0, Resp.shape[1]):
            Resp[A][J] = input(f"Resposta do aluno {A+1} à perg. {J+1} ")
