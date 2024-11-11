tupla_vendite = (
    (("RepartoA","Informatica"),("Prodotto A", ("contanti",1000))),
    (("RepartoA","Informatica"),("Prodotto B", ("carta di credito",1500))),
    (("RepartoA","Informatica"),("Prodotto C", ("carta di credito",1200))),
    (("RepartoA","Informatica"),("Prodotto D", ("contanti",200))),
    (("RepartoA","Informatica"),("Prodotto E", ("contanti",800))),
    (("RepartoA","Informatica"),("Prodotto F", ("N/D",200))),
    (("RepartoB","Elettronica"),("Prodotto A", ("contanti",1500))),
    (("RepartoB","Elettronica"),("Prodotto B", ("carta di credito",900)))
)

def media_globale(tupla_vendite):
    sommaSoldi = 0
    cont = 0
    for (reparto, materia), (prodotto, (pagamento, soldi)) in tupla_vendite:
        sommaSoldi += soldi
        cont += 1

    media = sommaSoldi / cont
    return round(media, 2)

def media(tupla_vendite, categoria, tipologiaPagamento):
    sommaSoldi = 0
    cont = 0
    for (reparto, materia), (prodotto, (pagamento, soldi)) in tupla_vendite:
        if pagamento == tipologiaPagamento and reparto == categoria:
            sommaSoldi += soldi
            cont += 1
    media = sommaSoldi / cont if cont > 0 else 0
    return round(media, 2)

def venditaMax():
    cont = 0
    listaProdotti = []
    for (reparto, materia), (prodotto, (pagamento, soldi)) in tupla_vendite:
        if cont == 0:
            venditaMax = soldi
            cont += 1
        if venditaMax < soldi:
            venditaMax = soldi

    for (reparto, materia), (prodotto, (pagamento, soldi)) in tupla_vendite:
        if venditaMax == soldi:
            listaProdotti.append(prodotto)

    return (venditaMax, listaProdotti)

def venditaMin():
    cont = 0
    for (reparto, materia), (prodotto, (pagamento, soldi)) in tupla_vendite:
        if cont == 0:
            venditaMin = soldi
            cont += 1
        if venditaMin > soldi and reparto == "RepartoA":
            venditaMin = soldi

    return venditaMin

def venditaPer():
    sommaA = 0
    contA = 0
    sommaB = 0
    contB = 0
    for (reparto, materia), (prodotto, (pagamento, soldi)) in tupla_vendite:
        if reparto == "RepartoA":
            sommaA += soldi
            contA += 1
        if reparto == "RepartoB":
            sommaB += soldi
            contB += 1

    perA = (sommaA * 100) / contA
    perB = (sommaB * 100) / contB
    return (round(perA, 2), round(perB, 2))

# Menu di scelta
while True:
    print("\nScegli un'opzione:")
    print("1. Calcola media globale")
    print("2. Calcola media specifica")
    print("3. Trova vendita massima")
    print("4. Trova vendita minima")
    print("5. Percentuale vendite per reparto")
    print("0. Esci")

    scelta = input("Inserisci il numero dell'opzione desiderata: ")

    if scelta == "1":
        print(f"Media globale: {media_globale(tupla_vendite)}")
    elif scelta == "2":
        categoria = input("Inserisci la categoria (es. RepartoA): ")
        tipologiaPagamento = input("Inserisci la tipologia di pagamento (es. contanti): ")
        print(f"Media specifica: {media(tupla_vendite, categoria, tipologiaPagamento)}")
    elif scelta == "3":
        print(f"Vendita massima e prodotti associati: {venditaMax()}")
    elif scelta == "4":
        print(f"Vendita minima in RepartoA: {venditaMin()}")
    elif scelta == "5":
        print(f"Percentuale vendite per reparto: {venditaPer()}")
    elif scelta == "0":
        print("Uscita dal programma.")
        break
    else:
        print("Scelta non valida. Riprova.")