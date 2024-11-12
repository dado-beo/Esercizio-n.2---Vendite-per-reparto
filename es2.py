"""
Definisci una funzione analizza_consumi_energetici che
riceva come parametro il nome della città e il nome della risorsa energetica e restituisca una tupla con la seguente struttura:
(media_risorsa, (max_risorsa, meseMax_risorsa))

Dove:
- `media_risorsa` è il consumo medio della risorsa.
- `max_risorsa` è il valore massimo di consumo della risorsa.
- `mese_max_risorsa` è il mese in cui si è verificata il consumo massimo per quella risorsa.

Aggiungi alla tupla altre citta e mesi.

Assicurati di gestire correttamente i casi in cui il nome della citta o della risorsa forniti come parametro non siano presenti nella tupla dei dati.
"""

tupla_consumi_energetici = (
    ("Milano", [
        ("gennaio", ("elettrico", 300)),
        ("gennaio", ("gas", 150)),
        ("febbraio", ("elettrico", 280)),
        ("febbraio", ("gas", 120)),
        ("marzo", ("elettrico", 400)),
        ("marzo", ("gas", 110)),
    ]),
    ("Brescia", [
        ("gennaio", ("elettrico", 280)),
        ("gennaio", ("gas", 140)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 130)),
        ("marzo", ("elettrico", 300)),
        ("marzo", ("gas", 150)),
    ]),
    ("Torino", [
        ("gennaio", ("elettrico", 280)),
        ("gennaio", ("gas", 140)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 130)),
        ("marzo", ("elettrico", 320)),
        ("marzo", ("gas", 160)),
    ])
)

# Inizializzo liste
listaNomiCitta = []
listaNomiRisorse = []
listaMesiMaxRisorsa = [] # Includo il caso in cui ci siano più mesi

# Riempio le liste
for citta1, dati in tupla_consumi_energetici:
    listaNomiCitta.append(citta1)
    for mese, *dato in dati:
        for dato1, dato2 in dato:
            listaNomiRisorse.append(dato1)

# Restituisci una tupla con la seguente struttura
# (media_risorsa, (max_risorsa, meseMax_risorsa)
def analizza_consumi_energetici(citta, risorsa):
    # Utilizzo per calcolo media
    sommaValoriRisorsa = 0
    cont1 = 0
    cont2 = 0

    for citta1, dati in tupla_consumi_energetici:
        if(citta1 == citta):
            # print(citta)
            # print(dati)
            for mese, *dato in dati:
                # print(mese)
                for dato1, dato2 in dato:
                    if(risorsa == dato1):
                        #print(dato1)
                        #print(dato2)
                        sommaValoriRisorsa += dato2
                        cont1 += 1

                        # Inizializzo max_risorsa
                        if(cont2 == 0):
                            max_risorsa = dato2
                            cont2 += 1
                        # Individuo il max_risorsa
                        if(max_risorsa < dato2):
                            max_risorsa = dato2
    
    # Calcolo media
    media_risorsa = sommaValoriRisorsa/ cont1
    
    # Ciclo per individuare i mesi max (o il mese max)
    for citta1, dati in tupla_consumi_energetici:
        if(citta1 == citta):
            for mese, *dato in dati:
                for dato1, dato2 in dato:
                    # Individuo i mesi max (o il mese)
                    if(max_risorsa == dato2):
                        listaMesiMaxRisorsa.append(mese)
 
    return (round(media_risorsa, 2), (max_risorsa, listaMesiMaxRisorsa))
            



# Esempio di utilizzo
#risultato_analisi = analizza_consumi_energetici("Milano", "elettrico")
#print(risultato_analisi)

citta = input("Inserisci il nome della città: ")
while(citta not in listaNomiCitta):
    citta = input("Città non valida, reinserisci il nome della città: ")

risorsa = input("Inserisci la risorsa: ")
while(risorsa not in listaNomiRisorse):
    risorsa = input("Risorsa non valida, reinserisci la risorsa: ")

print(f"Ecco a te la tupla: {analizza_consumi_energetici(citta, risorsa)}")