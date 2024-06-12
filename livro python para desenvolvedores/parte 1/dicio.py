def confere(dic):
    soma = sum(dic.values())
    media = soma / len(dic.values())
    variacao = max(dic.values()) - min(dic.values())
    return soma, media, variacao


a = {"a": 1, "b": 2, "c": 3}
print(confere(a))