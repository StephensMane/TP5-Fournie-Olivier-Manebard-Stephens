def message(nom):
    if nom == None:
        print("Hello, my friend")
    elif any(ch.isupper() for ch in nom):
        print("HELLO," +nom.upper())
    else:
        print("Hello, " +nom.capitalize())


nom=input("Tapez votre nom :")
message(nom)