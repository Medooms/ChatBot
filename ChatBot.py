import json

# Charger la base de connaissances
with open("faq.json", "r", encoding="utf-8") as f:
    base = json.load(f)

def choisir_theme():
    print("\nThèmes disponibles :")
    for theme in base["themes"]:
        print("-", theme.capitalize())
    choix = input("\nChoisissez un thème : ").lower()
    if choix in base["themes"]:
        return choix
    else:
        print("Thème non reconnu, réessayez.")
        return choisir_theme()

def poser_question(theme):
    questions = base["themes"][theme]["questions"]
    print(f"\nQuestions possibles pour {theme.capitalize()} :")
    for q in questions:
        print("-", q.capitalize())
    choix = input("\nQuelle information souhaitez-vous ? ").lower()
    if choix in questions:
        return questions[choix]
    else:
        return "Désolé, je n’ai pas cette information."

# Boucle d’interaction
print("Chatbot étudiant (tape 'quit' pour sortir)")
while True:
    utilisateur = input("\nVous : ")
    if utilisateur.lower() == "quit":
        print("Chatbot : Au revoir !")
        break
    theme = choisir_theme()
    reponse = poser_question(theme)
    print("\nChatbot :", reponse)