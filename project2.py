"""
Oppgaven går ut på å lage et spørreskjema med flervalgspørsmål.
Den stiller følgende krav: 

Det må være en innloggingsfunksjon for å få tilgang til spørreskjemaet.
Brukernavn skal være "MEK1300" og passord skal være "Python"
Dette skal lagres i et dictionary og sendes til en funksjon kalt login_info().

Ved riktig forsøk får man tilgang til selve spørreskjemaet. 
Hvis ikke skal brukeren så beskjed om feil brukernavn og/eller passord. 
Brukeren får muligheten til å taste brukernavn og passord på nytt frem til  vellykket forsøk.

Deretter starter flervalgstesten på 10 spørsmål som er vedlagt oppgaven. 

Quizzen avsluttes med at man får vite antall riktige og feil svar. 
For hvert feil svar skal programmet vise brukerens svar og det riktige svaret.

Hint: Bruk lister for å lagre spørsmål og svar.
Hint2: Bruk funksjoner for å holde oversikt i koden.

Forslag til oppgavefordeling: 
Slik jeg ser kan oppgaven deles i to. 
En del som handler om innlogging og den andre om selve spørreskjemaet. 

Mitt forslag er at vi deler dette mellom oss:
Håvard og Tobias tar innloggingsbiten, 
Edward og Anders tar spørreskjemet.
Dere står naturligvis fritt til å lage andre funksjoner eksempelvis bryte de opp i mindre funksjoner osv, 
enn det jeg har gjort, pass på at det er innenfor oppgaven. 
Se eksempel på psuedokode i quiz()funksjonen under. 
"""
from random import randrange, shuffle


def login_info(): # Håvard og Tobias
  return 



global choises, questions, letters, user_answers, user_wrong, choises_correct
#Liste over alle spørsmål:
questions = ["What is the capital of Norway?", 
              "What is the currency of Norway?", 
              "What is the largest city in Norway?",
              "When is constitution day (the national day) of Norway?",
              "What color is the background of the Norwegian flag?",
              "How many countries does Norway border?",	 
              "What is the name of the university in Trondheim?",	 
              "How long is the border between Norway and Russia?",	 
              "Where in Norway is Stavanger?",	 
              "From which Norwegian city did the world’s famous composer Edvard Grieg come?"]

# Dette er en ordnet liste over svaralternativer i grupper på 4 for alle spørsmål. Hvert første svaralternativ i hver gruppe er riktig svar.
# dvs, for questions[0] = choises[0:3] gyldige alternativer og choises[0] er riktig svar. 
# Vi kan bruke randint til å lage en tilfeldig rekkefølge av svaralternativer senere
choises =  ['Oslo','Bergen','Stavanger','Trondheim','Krone','Euro','Pound','Deutsche Mark','Oslo','Stavanger','Bergen',
            'Trondheim','17th May','27th May','17th April','27th April','Red','White','Blue','Yellow','3','1','2','4',
            'NTNU','UiS','UiO','NMBU','196km','96km','296km','396km','South-west','North','South','South-east',
            'Bergen','Oslo','Stavanger','Tromsø']     

#Liste over riktige svar
choises_correct = ['Oslo', 'Krone', 'Oslo', '17th May', 'Red', '3', 'NTNU', '196km', 'South-west', 'Bergen']
#Liste over bokstaver fra A-D. Brukes til å formatere output
letters=["A","B","C","D"]
#Liste over hva brukeren har svart.
user_answers = [] 
user_wrong = []

def quiz(): #Edward og Anders
  #Psuedokode: 
  # (for hvert spørsmål)Hent et spørsmål fra listen over spørsmål.
  # Presenter dette og valgalternativ til brukeren.
  # Ta input fra brukeren
  # Lagre inputet i en egen liste
  # når det ikke lengre er flere spørsmål 
  # sjekk hva som er riktig og ikke
  # For hvert spørsmål som er svart FEIL, print dette, sammen med riktig svar. 
  #TODO: (x) formater lister og lag en loop for spørsmål og svaralternativ.
  #TODO: () en funksjon for å lage tilfeldig rekkefølge på svaralternativene for hvert spørsmål? 
  #TODO: () funksjon som tar input fra brukeren, sjekker at dette er en bokstav i listen over tilatte bokstaver 
  #         og returnerer en int basert på hvilket spørsmål som er stilt og hvilket svaralternativ. Eks, svaralternativ D på spørsmål 4 skal gi choises[15]
  #TODO: Hør med faglærer om vi får bruke andre metoder fra randombilioteket enn randint. 
 
  #Hovedloop for å gjennom alle spørsmål og svaralternativer:
  #TODO: Lag en funksjon for å gjøre slik at svaralternativene kommer i en tilfeldig rekkefølge?  
  start_pos = 0
  for i in range(len(questions)):
    print("Q%i:"%(i+1) , questions[i])              #Ser slik ut: "Q8: Where in Norway is Stavanger?"
    teller = 0                                      #For å kunne loope gjennom listen av bokstaver laget jeg en ny teller her, denne vil gå fra 0-3, i loopen under
    for t in range(start_pos, start_pos+4):         #Her looper vi gjennom listen av svaralternativer. vi starter på 0 og slutter på 0+4
      print(" "*4,letters[teller],": ", choises[t], sep="") 
      teller = teller+1
    user_answers.append(user_input()) 
    start_pos = start_pos + 4                       #Gjør klar for neste iterasjon av svaralternativer ved å forskyve variablen med 4  
  return

def random_liste(questions, choises):
  start_pos = 0
  for i in range(len(questions)):
    print("Q%i:"%(i+1) , questions[i])              #Ser slik ut: "Q8: Where in Norway is Stavanger?"
    teller = 0
    rand_liste = choises[start_pos:start_pos+4]     #Ta et utdrag fra listen over svaralternativer pr. spørsmål, lagre dette i en ny liste
    shuffle(rand_liste)                             #Bruk shufflefunksjonen for å snu og endre på denne lista før vi printer den. 
    for t in rand_liste:         
      print(" "*4,letters[teller],": ", t, sep="") 
      teller = teller+1
    start_pos = start_pos + 4  
  return

def user_input():
  ''' Funksjonen kjører så lenge svaret ikke er A, B, C eller D. Returnerer valgt bokstav'''
  svar = input("Answer:")
  while svar.capitalize() not in ["A", "B", "C", "D"]:
    print("Please input your response with a character A, B, C or D")
    svar = input("Answer:")
  return svar.capitalize()

def oppsummering(svar, choises): #gammel funksjon, ikke noe vits i å kjøre denne enda
  teller = 0
  for e in svar: #for hvert element i listen svar
    if e != choises[teller]:
      user_wrong.append(e)
    teller = teller + 5 
  

  return
  
