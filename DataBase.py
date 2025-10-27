import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="10.200.14.25",
    user="TheGoat",
    password="SixSeven",
    database="musikk"
)
mycursor = mydb.cursor()

# - Commands -
def EditArt():
    old_name = input("Enter the artist name to edit: ").lower()

    mycursor.execute("SELECT id FROM Artister WHERE name = %s", (old_name,))
    artist = mycursor.fetchone()

    if artist is None:
        print("Artist", {old_name}, "not found.")
        return

    new_name = input("Enter the new name for the artist: ").lower()
    mycursor.execute("UPDATE Artister SET name = %s WHERE id = %s", (new_name, artist[0]))
    mydb.commit()

    print("Artist", {old_name}, "has been renamed to", {new_name})


def RemoveArt():
    ListArt()
    Remove_Artist = input("Remove Artist: ").lower()

    # Check if artist exists
    mycursor.execute("SELECT id FROM Artister WHERE name = %s", (Remove_Artist,))
    artist = mycursor.fetchone()

    if artist is None:
        print("Artist", {Remove_Artist}, "not found.")
    else:
        artist_id = artist[0]

        mycursor.execute("DELETE FROM Sanger WHERE Artist = %s", (artist_id,))
        mycursor.execute("DELETE FROM Artister WHERE id = %s", (artist_id,))

        mydb.commit()

        print("Artist", {Remove_Artist}, "and their songs have been removed.")


def RemoveSong():
    ListSong()
    Remove_Song = input("Remove Song: ").lower()

    mycursor.execute("SELECT id FROM Sanger WHERE Sang = %s", (Remove_Song,))
    song = mycursor.fetchone()

    if song is None:
        print("Song", {Remove_Song}, "not found.")
    else:
        mycursor.execute("DELETE FROM Sanger WHERE id = %s", (song[0],))
        mydb.commit()
        print("Song", {Remove_Song}, "has been removed.")


def ListArt():
    mycursor.execute("SELECT * FROM Artister;")
    result = mycursor.fetchall()
    for x in result:
        print(x)


def ListSong():
    mycursor.execute("SELECT * FROM Sanger;")
    result = mycursor.fetchall()
    for x in result:
        print(x)


def AddArt():
    artist_name = input("Add an Artist: ").lower()

    mycursor.execute("SELECT id FROM Artister WHERE name = %s", (artist_name,))
    artist = mycursor.fetchone()

    if artist is None:
        mycursor.execute("INSERT INTO Artister (name) VALUES (%s)", (artist_name,))
        mydb.commit()
        print("Added new artist:", {artist_name})
    else:
        print("Artist", {artist_name}, "already exists.")


def AddSong():
    song_name = input("Add a Song: ").lower()
    artist_name = input("Who's the Artist: ").lower()

    mycursor.execute("SELECT id FROM Artister WHERE name = %s", (artist_name,))
    artist = mycursor.fetchone()
    if artist is None:
        mycursor.execute("INSERT INTO Artister (name) VALUES (%s)", (artist_name,))
        mydb.commit()
        artist_id = mycursor.lastrowid
        print("Added new artist:", {artist_name})
    else:
        artist_id = artist[0]

    mycursor.execute("INSERT INTO Sanger (Sang, Artist) VALUES (%s, %s)", (song_name, artist_id))
    mydb.commit()
    print("Added song", {song_name}, "by", {artist_name})

def RemoveAll():
    confirm = input("Are you sure you want to delete ALL artists and their songs? (yes/no): ").strip().lower()
    if confirm == "yes":
        mycursor.execute("DROP TABLE IF EXISTS Sanger;")
        mycursor.execute("DROP TABLE IF EXISTS Artister;")

        mycursor.execute("""
        CREATE TABLE IF NOT EXISTS Artister (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
        """)

        mycursor.execute("""
        CREATE TABLE IF NOT EXISTS Sanger (
            id INT AUTO_INCREMENT PRIMARY KEY,
            Sang VARCHAR(255) NOT NULL,
            Artist INT,
            FOREIGN KEY (Artist) REFERENCES Artister(id) ON DELETE CASCADE
        );
        """)

        mydb.commit()
        print("All artists and their songs have been deleted and tables recreated.")
    else:
        print("Cancelled.")

def meny():
    print("+------------------+-----------------+")
    print("|  Add Artist (1)  |   Add Song (2)  |")
    print("+------------------+-----------------+")
    print("| Remove Artist(3) | Remove Song(4)  |")
    print("+------------------+-----------------+")
    print("|  Edit Artist(5)  | Under Constrac- |")
    print("+------------------+-----------------+----------+")
    print("| List Artists (6) |  List Songs(7)  |  Quit(Q) |")
    print("+------------------+-----------------+----------+")


# --- MAIN LOOP ---
while True:
    meny()
    Command = input("Velg kommando: ").strip()

    match Command:
        case "1":
            AddArt()
        case "2":
            AddSong()
        case "3":
            RemoveArt()
        case "4":
            RemoveSong()
        case "5":
            EditArt()
        case "6":
            ListArt()
        case "7":
            ListSong()
        case "DELETE":
            RemoveAll()
        case "q":
            print("Avslutter programmet...")
            break
        case _:
            print("Ugyldig kommando, prøv igjen.")


