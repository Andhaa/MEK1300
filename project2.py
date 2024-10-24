from random import shuffle

#Dictionary over brukere og tilhørende passord. Aldri gjør dette igjen, noensinne, noen gang. 
users = {"MEK1300" : "Python"}

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
# dvs, for questions[0] = choices[0:3] gyldige alternativer og choices[0] er riktig svar. 
# Vi bruker random.shuffle() til å lage en tilfeldig rekkefølge av svaralternativer senere
choices =  ['Oslo','Bergen','Stavanger','Trondheim','Krone','Euro','Pound','Deutsche Mark','Oslo','Stavanger','Bergen',
            'Trondheim','17th May','27th May','17th April','27th April','Red','White','Blue','Yellow','3','1','2','4',
            'NTNU','UiS','UiO','NMBU','196km','96km','296km','396km','South-west','North','South','South-east',
            'Bergen','Oslo','Stavanger','Tromsø']     

#Liste over riktige svar: (kunne også være laget programmatisk ved å ta det 4.elementet i egen liste, se forklaring over)
choices_correct = ['Oslo', 'Krone', 'Oslo', '17th May', 'Red', '3', 'NTNU', '196km', 'South-west', 'Bergen']

#Liste over bokstaver fra A-D. Brukes til å formatere output:
letters=["A","B","C","D"] 

user_answers = [] #Liste over svar

def login_info(user_db, username, password): # Håvard og Tobias
  if username in user_db and password == user_db[username]:
     return True
  print("Invalid username and / or password!")     
  return False

def main(questions, choices):
  '''Tar i mot to lister, questions og choices. For hvert element i questions[] så loopes choices[] fire ganger'''
  global user_answers                                      #Siden user_answers er utenfor scopet til funksjonen og vi skal skrive til den, må vi deklarere denne som global
  start_pos = 0                                            #Teller for å holde styr på hvor vi er i listen
  for i in range(len(questions)):                          #For hvert spørsmål i listen spørsmål
    print("Q%i:"%(i+1) , questions[i])                     #Ser slik ut: "Q8: Where in Norway is Stavanger?"
    teller = 0                                             #Sett variabelen teller til 0, denne brukes til å lage ABCD i print senere
    rand_liste = choices[start_pos:start_pos+4]            #Ta et utdrag(slice) fra listen over svaralternativer pr. spørsmål, lagre dette i en ny liste. 
    shuffle(rand_liste)                                    #Bruk shufflefunksjonen på denne lista før vi printer den som valgalternativ. 
    for t in rand_liste:                                   #For hvert element i den nye lista (Som nå har tilfeldig rekkefølge) 
      print(" "*4,letters[teller],": ", t, sep="")       
      teller = teller+1      
    user_answers.append(rand_liste[user_input()])          #Legg til svar i listen user_answers fra listen rand_list som er fra 0-3. Henvisning til User_input()
    start_pos = start_pos + 4                              #Dette gir oss starten av svaralternativ for neste spørsmål. 
  return

def user_input():
  ''' Funksjonen kjører så lenge svaret ikke er a,b,c eller d. Returnerer int fra 0-3.'''
  svar = input("Answer:")
  while svar.capitalize() not in letters: #Henvisning til listen som inneholder "A,B,C,D"
    print("Please input your response with a character A, B, C or D")
    svar = input("Answer:")
  match svar.capitalize():
    case "A": return 0
    case "B": return 1
    case "C": return 2
    case "D": return 3

def check_lists(liste1, liste2):
    if len(liste1) != len(liste2):
        print("Listene har ulik lengde, noe er feil!")
        return False
    match_count = 0
    mismatch_count = 0
    for i in range(len(liste1)):
        if liste1[i] == liste2[i]:
            match_count+= 1
        else:
            mismatch_count += 1 
            print(f"Feil svar i Oppgave {i+1}: Svaret er {liste1[i]}, ditt svar var {liste2[i]}")       
    print ("Correct answers: ", match_count , "Wrong answers: " , mismatch_count)
    
    return match_count == len(liste1)

##Programmet starter her : 
user = login_info(users, input("Enter your username: "), input("Enter your password: "))
while(user==False): #Så lenge input er feil, så fortsetter vi å spørre etter passord:
   login_info(users, input("Enter your username: "), input("Enter your password: "))

#Hvis loopen over evalurer til sann så kjører vi resten av programmet: 
main(questions,choices)
if check_lists(choices_correct, user_answers)==True:
   print("Congratulations, you had no errors!")