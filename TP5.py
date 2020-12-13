# // feature 1 //

# test

def test_f1():
  assert Feature1("bob") == "Hello, Bob"
  assert Feature1("Bob") == "Hello, Bob"

# fonction

def Feature1(nom):

  if not nom[0].isupper():
    nom = nom[0:1].capitalize() + nom[1:]
    return("Hello, "+ nom)

  else:
    return("Hello, "+ nom)

# // feature 2 //

# test

def test_f2():

  assert Feature2(' ') == "Hello, my friend"

# fonction

def Feature2(nom):

  if nom.isspace():
    return("Hello, my friend")

# // feature 3 //

# test

def test_f3():

  assert Feature3("JERRY") == "HELLO, JERRY"

# fonction

def Feature3(nom):

  if nom.isupper():
    return("HELLO, "+ nom)

# // feature 4 //

# test

def test_f4x5():

  assert Feature4x5("Amy,bob") == "Hello, Amy Bob "

# fonction

def Feature4x5(nom):

  liste_noms = list()
  i = 0

  while i < len(nom):

    liste_noms += [""]
    while i < len(nom) and nom[i] != ',':

      liste_noms[len(liste_noms)-1] += nom[i]
      i += 1

    i += 1

  message = "Hello, "

  for noms in liste_noms:

    if not noms[0].isupper():
      noms = noms[0:1].capitalize() + noms[1:]

    message += noms +' '

  return message

# // feature 6 //

# test

def test_f6():
  assert Feature6("Amy, BOB, Jerry") == "Hello, Amy Jerry. AND BOB"

# fonction

def Feature6(nom):

  liste_noms = list()
  i = 0

  while i < len(nom):

    liste_noms += [""]
    while i < len(nom) and nom[i] != ',':

      liste_noms[len(liste_noms)-1] += nom[i]
      i += 1

    i += 1

  Message = "Hello, "

  for noms in liste_noms:

    if not noms.isupper():

      Message += noms

  Message +=". AND"

  for noms in liste_noms:

    if noms.isupper():

      Message += noms

  return Message


# // TEST DES FEATURES //

def test_all_features():
  test_f1()
  print("la fonctionnalité 1 fonctionne comme prévu !")

  test_f2()
  print("la fonctionnalité 2 fonctionne comme prévu !")

  test_f3()
  print("la fonctionnalité 3 fonctionne comme prévu !")

  test_f4x5()
  print("les fonctionnalité 4 et 5 fonctionne comme prévu !")

  test_f6()
  print("la fonctionnalité 6 fonctionnent comme prévu !")

test_all_features()
