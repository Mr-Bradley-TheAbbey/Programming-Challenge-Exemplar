import os
import random

def initial_menu():
  os.system('clear')
  print("Welcome to the Music Selection System")
  print("")
  print("Please select an option:")
  print("1. Create an account")
  print("2. Login")
  print("3. Exit")

  choice = -1
  
  while choice < 0 or choice > 3:
    choice = int(input("Please select option 1, 2 or 3:"))
    if choice == 1:
      create_account()
      login()
    elif choice == 2:
      login()
    elif choice == 3:
      break

def menu(user):

  os.system('clear')
  print("Welcome to the Music Selection System - {}".format(user[0]))
  
  exit = False
  while exit is False:

    
    print("")
    print("Please select an option:")
    print("1. Change Favourite Artist")
    print("2. Change Favourite Genre")
    print("3. List songs in our Library")
    print("4. View our playlists")
    print("5. Create a new playlist")
    print("6. Autogenerate a new playlist")
    print("7. Print an Artist's List of Songs")
    print("8. Exit")
    
    choice = int(input("Please select option 1-8:"))
    if choice == 1:
      change_artist(user)
    elif choice == 2:
      change_genre(user)
    elif choice == 3:
      view_library()
    elif choice == 4:
      view_playlists()
    elif choice == 5:
      create_playlist()
    elif choice == 6:
      autogenerate()
    elif choice == 7:
      artists_songs()
    elif choice == 8:
      exit = True

def login():

  os.system('clear')
  print("Welcome to the Music Selection System")
  print("")
  print("Please login by entering your Name and Date of Birth")
  print("")

  #collect users from users.txt file
  accountfile = open("users.txt", "r")

  file = accountfile.read()
  accountfile.close()
  file = file.split("\n")
  

  let_in = False

  #Loop until valid user details entered
  while let_in == False:
    name = input("What is your full name?")
    dob = input("What is your Date of Birth?")

    #check each line of file for correct name & dob
    for i in file:
      i = i.split(",")
      if name == i[0] and dob == i[1]:
        let_in = True
        user = i
    os.system('clear')
    print("Invalid user - please try again")   

  os.system('clear')
  print("Valid User")
  menu(user)
  
def create_account():
  #open file, ask for details and write to file
  
  os.system('clear')
  os.system('clear')
  print("Welcome to the Music Selection System")
  print("")
  print("Please answer the following questions to create an account.")
  print("")
  
  accountfile = open("users.txt", "a")
  
  name = input("What is your full name?")
  dob = input("What is your Date of Birth (Format dd/mm/yy)?")
  fav_artist = input("Who is your favourite artist?")
  fav_genre = input("What is your favourite genre?")
  
  account = name + "," + dob + "," + fav_artist + "," + fav_genre + "\n"
  
  accountfile.write(account)
  accountfile.close()
  
  os.system('clear')
  
  print("Your account has been created with the following details:")
  print("Name: {}".format(name))
  print("DoB: {}".format(dob))
  print("Favourite Artist: {}".format(fav_artist))
  print("Favourite Genre: {}".format(fav_genre))

def change_artist(user):

  os.system('clear')

  accountfile = open("users.txt", "r")
  file = accountfile.read()
  accountfile.close()
  file = file.split("\n")

  accountdetails = user[0] + "," + user[1] + "," + user[2] + "," + user[3]
  print(accountdetails)
  file.remove(accountdetails)
  print(file)

  newartist = input("What is your new favourite Artist?")
  accountdetails = user[0] + "," + user[1] + "," + newartist + "," + user[3]
  file.append(accountdetails)

  file2w = ""
  for i in file:
    if i != "":
      file2w += i + "\n"

  accountfile = open("users.txt", "w")
  accountfile.write(file2w)
  accountfile.close()

def change_genre(user):

  os.system('clear')

  accountfile = open("users.txt", "r")
  file = accountfile.read()
  accountfile.close()
  file = file.split("\n")

  accountdetails = user[0] + "," + user[1] + "," + user[2] + "," + user[3]
  print(accountdetails)
  file.remove(accountdetails)


  newgenre = input("What is your new favourite Genre?")
  accountdetails = user[0] + "," + user[1] + "," + user[2] + "," + newgenre
  file.append(accountdetails)

  file2w = ""
  for i in file:
    if i != "":
      file2w += i + "\n"

  accountfile = open("users.txt", "w")
  accountfile.write(file2w)
  accountfile.close()

def view_library():

  os.system('clear')
  print("Music Selection System - View Song List")
  print("")
  
  libraryfile = open("song_list.txt", "r")
  library = libraryfile.read()
  libraryfile.close( )

  library = library.split("\n")
  library.sort()

  for song in library:
    song = song.split(",")
    print("Song name: {}".format(song[0]))
    print("Artist: {}".format(song[1]))
    print("Genre: {}".format(song[2]))
    print("Song length: {}".format(song[3]))
    print("")

def view_playlists():
  os.system('clear')
  print("Music Selection System - View Playlists")
  print("")

  file = open("playlists.txt", "r")
  playlistsfile = file.read()
  file.close()
  playlists = playlistsfile.split("\n")

  for playlist in playlists:
    if playlist != "":
      playlist = playlist.split(",")
      print("Playlist Title: {}".format(playlist[0]))
      print("Playlist Genre: {}".format(playlist[1]))
      total_length = playlist[2]
      minutes = int(total_length) // 60
      seconds = int(total_length) % 60
      print("Playlist Length: {}:{}".format(minutes, seconds))
      print("")
    
def create_playlist():
  os.system('clear')
  print("Music Selection System - Playlist Creation")
  print("")

  libraryfile = open("song_list.txt", "r")
  library = libraryfile.read()
  libraryfile.close( )

  library = library.split("\n")

  playlist_name = input("What shall we call the playlist?")

  playlist_detail = ""
  playlist_length = 0
  song_choice = "a"

  while song_choice != "Exit":
    song_choice = input("Enter a Song to add to Playlist (Enter Exit to leave):")

    for song in library:
      song_detail = song.split(",")
      if song_choice == song_detail[0]:
        playlist_detail += song + "\n"
        song_length = song_detail[3]
        actual_song_length = int(song_length[0]) * 60 + int(song_length[2::])
        playlist_length += actual_song_length
        print("{} has been added to {} playlist".format(song_choice, playlist_name))
      

  filename = playlist_name + ".txt"
  artistfile = open(filename, "w") 
  artistfile.write(playlist_detail)
  artistfile.close()

  playlist_list_detail = playlist_name + "," + "Self_Selected"+ "," + str(playlist_length) +"\n"
  playlist_file = open("playlists.txt", "a")
  playlist_file.write(playlist_list_detail)
  playlist_file.close()
    
def autogenerate():
  os.system('clear')
  print("Music Selection System - Playlist Autogeneration")
  print("")
  maxlength = int(input("What is the max. length of you playlist (in minutes)?"))
  playlist_name = input("What shall we call the playlist?")
  print("")
  print("Select an genre:")
  print("1. Pop")
  print("2. Rock")
  print("3. Indie")

  selection = -1
  while selection < 0 or selection > 3:
    selection = int(input("Select 1, 2 or 3:"))
    if selection == 1:
      genre_selected = "Pop"
    elif selection == 2:
      genre_selected = "Rock"
    elif selection ==3:
      genre_selected = "Indie"


  libraryfile = open("song_list.txt", "r")
  library = libraryfile.read()
  libraryfile.close( )

  library = library.split("\n")

  possible_songs = []

  for song in library:
    songdetail = song.split(",")
    if songdetail[2] == genre_selected:
      possible_songs.append(songdetail)

  playlist_songs = []

  length = 0
  
  while length < maxlength * 60:
    random_song = random.choice(possible_songs)
    song_length = random_song[3]
    actual_song_length = int(song_length[0]) * 60 + int(song_length[2::])
    if length + actual_song_length > maxlength * 60:
      break
    else:
      length += actual_song_length
      playlist_songs.append(random_song)

  playlist_detail = ""
  for song in playlist_songs:
    playlist_detail += song[0] + "," + song[1] + "," + song[2] + "," + song[3] + "\n"

  playlist_file_name = playlist_name + ".txt"
  playlist_file = open(playlist_file_name, "w")
  playlist_file.write(playlist_detail)
  playlist_file.close()

  playlist_list_detail = playlist_name + "," + genre_selected + "," + str(length) +"\n"
  playlist_file = open("playlists.txt", "a")
  playlist_file.write(playlist_list_detail)
  playlist_file.close()

def artists_songs():
  os.system('clear')
  print("Music Selection System - View Artist's Songs")
  print("")

  libraryfile = open("song_list.txt", "r")
  library = libraryfile.read()
  libraryfile.close( )

  library = library.split("\n")

  choice_of_artist = input("Which Artist's Songs do you wish to look at?")
  print("")

  artists_list = ""
  
  for song in library:
    song_detail = song.split(",")
    if song_detail[1] == choice_of_artist:
      print("Song name: {}".format(song_detail[0]))
      print("Artist: {}".format(song_detail[1]))
      print("Genre: {}".format(song_detail[2]))
      print("Song length: {}".format(song_detail[3]))
      print("")
      artists_list += "Song name: {}\n".format(song_detail[0])
      artists_list += "Artist: {}\n".format(song_detail[1])
      artists_list +="Genre: {}\n".format(song_detail[2])
      artists_list += "Song length: {}\n".format(song_detail[3])
      artists_list += "\n"

  filename = choice_of_artist + ".txt"
  artistfile = open(filename, "w") 
  artistfile.write(artists_list)
  artistfile.close()
  
initial_menu()
