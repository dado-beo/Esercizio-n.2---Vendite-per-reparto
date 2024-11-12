"""
Definisci le seguenti funzioni utilizzando le funzioni predefinite sum, min, max per le liste:

1. **media_gol_partite(tupla_partite)**: una funzione che accetti come parametro la tupla delle partite e restituisca la media dei gol segnati in tutte le partite.

2. **media_gol_squadra(tupla_partite, squadra)**: una funzione che accetti come parametri la tupla delle partite e il nome di una squadra, e restituisca la media dei gol segnati dalla squadra in tutte le partite in cui ha partecipato.

3. **partita_con_piu_gol(tupla_partite)**: una funzione che restituisca una tupla contenente la partita con il maggior numero di gol segnati e i relativi punteggi.

4. **partita_con_meno_gol(tupla_partite)**: una funzione che restituisca una tupla contenente la partita con il minor numero di gol segnati e i relativi punteggi.

5. Prevedi un menu di scelta che consenta all'utente di selezionare un'operazione tra le opzioni disponibili.
"""

tupla_partite = (
    ("SquadraA", "SquadraB", 3, 2),
    ("SquadraC", "SquadraD", 1, 1),
    ("SquadraB", "SquadraC", 2, 4),
    ("SquadraD", "SquadraA", 0, 3),
    ("SquadraB", "SquadraD", 1, 2),
)

# Inizializzo delle liste 
listaSquadraDiCasa = []
listaSquadraOspite = []
listaPunteggioSquadraDiCasa = []
listaPunteggioSquadraOspite = []

# Riempio le lista
for (squadra1, squadra2, punteggio1, punteggio2) in tupla_partite:
        listaSquadraDiCasa.append(squadra1)
        listaSquadraOspite.append(squadra2)
        listaPunteggioSquadraDiCasa.append(punteggio1)
        listaPunteggioSquadraOspite.append(punteggio2)

def media_gol_partite(tupla_partite):
    # Sommo
    somma1 = sum(listaPunteggioSquadraDiCasa)
    somma2 = sum(listaPunteggioSquadraOspite)
    media = (somma1 + somma2) / (len(listaPunteggioSquadraOspite) * 2)
    return round(media, 2)

def media_gol_squadra(tupla_partite, squadra):
    sommaGolSquadra = 0
    contSquadra = 0
    for (squadra1, squadra2, punteggio1, punteggio2) in tupla_partite:
        if(squadra1 == squadra):
            sommaGolSquadra += punteggio1
            contSquadra += 1 

        if(squadra2 == squadra):
            sommaGolSquadra += punteggio2
            contSquadra += 1 

    media = sommaGolSquadra / contSquadra
    return round(media, 2)

def partita_con_più_gol(tupla_partite):
    cont = 0
    for (squadra1, squadra2, punteggio1, punteggio2) in tupla_partite:
        # Inizializzo il valore massimo
        if (cont == 0):
            maxTot = punteggio1 + punteggio2
            cont += 1 

        # Individuo il max
        if(punteggio1 + punteggio2 > maxTot):
            maxTot = punteggio1 + punteggio2

    # Individuo la partita
    for (squadra1, squadra2, punteggio1, punteggio2) in tupla_partite:
        if(punteggio1 + punteggio2 == maxTot):
            return (squadra1, squadra2, punteggio1, punteggio2)
    
def partita_con_meno_gol(tupla_partite):
    cont = 0
    for (squadra1, squadra2, punteggio1, punteggio2) in tupla_partite:
        # Inizializzo il valore minimo
        if (cont == 0):
            minTot = punteggio1 + punteggio2
            cont += 1 

        # Individuo il min
        if(punteggio1 + punteggio2 < minTot):
            minTot = punteggio1 + punteggio2

    # Individuo la partita
    for (squadra1, squadra2, punteggio1, punteggio2) in tupla_partite:
        if(punteggio1 + punteggio2 == minTot):
            return (squadra1, squadra2, punteggio1, punteggio2)

while True:
    print("\nFai la tua scelta:")
    print("1. Media gol partite;")
    print("2. Media gol squadra specifica;")
    print("3. Partita con più gol;")
    print("4. Partita con meno gol;")
    print("0. Esci.")

    risposta = input("Inserisci la tua scelta: ")

    if(risposta == "1"):    
        # media_gol_partite
        print(f"Media gol partite: {media_gol_partite(tupla_partite)}")
    elif(risposta == "2"):
        # media_gol_squadra
        squadra = input("Inserisci il nome della squadra:")
        while(squadra not in listaSquadraDiCasa and squadra not in listaSquadraOspite):
            squadra = input("Nome non valido, reinserisci il nome della squadra:")
        print(f"Media gol squadra ({squadra}): {media_gol_squadra(tupla_partite, squadra)}")
    elif(risposta == "3"):
        # partita_con_più_gol
        print(f"Partita con più gol: {partita_con_più_gol(tupla_partite)}")
    elif(risposta == "4"):
        # partita_con_meno_gol
        print(f"Partita con meno gol: {partita_con_meno_gol(tupla_partite)}")
    elif(risposta == "0"):
        # Chiusura
        print("Sei uscito!")
        break
    else:
        print("Risposta non valida, leggi bene il menù!")
