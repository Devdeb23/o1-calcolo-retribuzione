# ---
# Esercizio 01: Calcolo Retribuzione Lorda
# Obiettivo: Implementare il modello Input-Elaborazione-Output.
#

# --- 1. FASE DI INPUT ---
# Chiediamo all'utente le ore lavorate.
# input() legge sempre il testo (stringa).
# float() converte il testo in un numero con decimali
ore_lavorate = float(input("Inserisci le ore lavorate: "))

# Chiediamo all'utente la paga oraria.
paga_oraria = float(input("Inserisci la paga oraria (€): "))

# --- 2. FASE DI ELABORAZIONE ---
# Calcoliamo la retribuzione lorda usando l'operatore matematico *.
# Il risultato viene salvato in una nuova variabile.
retribuzione_lorda = ore_lavorate * paga_oraria

# --- 3. FASE DI OUTPUT ---
# Mostriamo il risultato all'utente.
# Usiamo una "f-string" per inserire facilmente le variabili nel testo.
# Formatta il numero per avere sempre due cifre decimali (come i centesimi)
print("--- Riepilogo Paga ---")
print(f"La tua retribuzione lorda è: € {retribuzione_lorda:.2f}")