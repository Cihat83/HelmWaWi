from User.Model.user import user



def createUser(email, name, password, adresse, tel):

    createdUser = user(email, name, password, adresse, tel)
    createdUser.speichern()

# 1     Geh in den Ordner "User", dann in den Unterordner "Model", öffne die Datei "user.py" und hol dir daraus genau das Ding namens "user".
#       Die Datei enthält z.B. Informationen über Benutzer.
#       from: "Geh zu diesem Ort im Ordnersystem." ; import: "Hol dir genau das, was ich brauche."

# 5    Diese Zeile ist der Start einer Funktion, die dafür sorgt, dass ein neuer Benutzer (User) erstellt wird.

#       mit def Definiere ich eine Funktion;
#       Eine Funktion ist wie ein Rezept oder eine Anleitung, die immer wieder verwendet werden kann, wenn du etwas Bestimmtes tun willst.

#       createUser bedeutet: "Erstelle einen Benutzer".

#       (email, name, password, adresse, tel) das sind die Parameter der Funktion.
#       Sie geben an, welche Informationen die Funktion benötigt, um zu funktionieren.

# 7     Hier erstellst du einen neuen Benutzer. Die Informationen, die du in den Klammern übergibst, werden verwendet,
#       um den neuen Benutzer zu bauen und in der Variablen createdUser gespeichert.


# 8     Mit createdUser.speichern() rufst du die Methode speichern() auf, die zu dem benutzer gehört, den du in createdUser gespeichert hast.
#       in diesem Fall gibt speichern() eine Bestätigung aus, dass der Benutzer gespeichert wurde.



#   Fazit:
#   def createUser(email, name, password, adresse, tel): ist der Start einer Funktion, die alle wichtigen Daten eines neuen Benutzers
#   (E-Mail, Name, Passwort, Adresse, Telefonnummer) nimmt und damit etwas tut.
#   Du kannst die Funktion später immer wieder verwenden, um neue Benutzer zu erstellen, indem du ihr die entsprechenden Daten übergibst.