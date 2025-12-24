# Programma gioco Carta, Forbice, Sasso
# L'utente può scegliere tra carta (C), forbice (F) e sasso (S)
# Carta vince su sasso, sasso vince su forbice, forbice vince su carta
# Confronta scelta utente e scelta del computer
# Stampa il punteggio aggiornato e chiede all'utente se vuole giocare nuovamente

import random

# Variabili globali
numero_giocate = 0
punteggio_utente = 0
punteggio_computer = 0


def benvenuto():
    """Chiede all'utente il nome e mostra un messaggio di benvenuto."""
    nome_utente = input("\nCiao, inserisci il tuo nome: ").strip()
    print(f"\nOk, {nome_utente.capitalize()}. Giochiamo a Carta, Forbice e Sasso. Conosci le regole?")
    
    risposta_utente = input("\nRispondi Sì o No: ").lower()
    if risposta_utente not in ("sì", "si", "s", "sy", "yes", "y", "yeah", "yep"):
        print(
            "\nEcco le regole: scegli tra carta, forbice e sasso, poi confrontiamo con la mia scelta."
            "\nCarta vince su sasso, sasso vince su forbice, forbice vince su carta."
        )
    
    return nome_utente


def mossa_pc_random():
    """Genera casualmente la mossa del computer."""
    mosse_possibili = ["Carta", "Forbice", "Sasso"]
    return random.choice(mosse_possibili)


def confronta_pc_scelta_utente(mossa_pc, nome_utente, scelta_utente, punteggio_utente, punteggio_computer, numero_giocate):
    """Confronta la scelta dell'utente e del computer e aggiorna punteggi e numero giocate."""
    
    numero_giocate += 1
    nome_utente = nome_utente.capitalize()  # iniziale maiuscola

    if scelta_utente == "F":
        if mossa_pc == "Forbice":
            print(f"\nPareggio! Entrambi abbiamo scelto Forbice.")
        elif mossa_pc == "Carta":
            punteggio_utente += 1
            print(f"\nHai vinto, {nome_utente}! Io avevo scelto Carta e tu Forbice!")
        else:  # Sasso
            punteggio_computer += 1
            print(f"\nHai perso, {nome_utente}! Io avevo scelto Sasso e tu Forbice!")
    
    elif scelta_utente == "C":
        if mossa_pc == "Carta":
            print(f"\nPareggio! Entrambi abbiamo scelto Carta.")
        elif mossa_pc == "Sasso":
            punteggio_utente += 1
            print(f"\nHai vinto, {nome_utente}! Io avevo scelto Sasso e tu Carta!")
        else:  # Forbice
            punteggio_computer += 1
            print(f"\nHai perso, {nome_utente}! Io avevo scelto Forbice e tu Carta!")
    
    elif scelta_utente == "S":
        if mossa_pc == "Sasso":
            print(f"\nPareggio! Entrambi abbiamo scelto Sasso.")
        elif mossa_pc == "Forbice":
            punteggio_utente += 1
            print(f"\nHai vinto, {nome_utente}! Io avevo scelto Forbice e tu Sasso!")
        else:  # Carta
            punteggio_computer += 1
            print(f"\nHai perso, {nome_utente}! Io avevo scelto Carta e tu Sasso!")

    print(f"\nPunteggio utente: {punteggio_utente} - Punteggio computer: {punteggio_computer}")

    return punteggio_utente, punteggio_computer, numero_giocate



def fai_stampa_finale(nome_utente, punteggio_utente, punteggio_computer):
    """Stampa il risultato finale della partita."""
    if punteggio_utente > punteggio_computer:
        print(f"\nComplimenti {nome_utente}! Hai vinto la partita con {punteggio_utente} punti contro i miei {punteggio_computer}!")
    elif punteggio_utente == punteggio_computer:
        print(f"\nÈ un pareggio, {nome_utente}! Abbiamo entrambi totalizzato {punteggio_utente} punti!")
    else:
        print(f"\nMi dispiace {nome_utente}! Hai perso la partita con {punteggio_utente} punti contro i miei {punteggio_computer}!")


# --- PROGRAMMA PRINCIPALE ---

nome_giocatore = benvenuto()

while numero_giocate < 10:
    scelta_utente = input("\nFai la tua scelta tra C per carta, F per forbice ed S per sasso: ").strip().upper()
    
    # Controllo input valido
    if scelta_utente not in ("C", "F", "S"):
        print("Scelta non valida! Riprova.")
        continue

    mossa_pc = mossa_pc_random()  # mossa del computer per questo turno

    punteggio_utente, punteggio_computer, numero_giocate = confronta_pc_scelta_utente(
        mossa_pc, nome_giocatore, scelta_utente, punteggio_utente, punteggio_computer, numero_giocate
    )

    print(f"\nNumero giocate: {numero_giocate}")

# Stampa risultato finale
fai_stampa_finale(nome_giocatore, punteggio_utente, punteggio_computer)

print("\nGrazie per aver giocato! Alla prossima!")
            
            

    

