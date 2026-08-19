'''
    Author: Aaramva Acharya
    Program: Lab-3: Playlist Program
    Description: This program allows the user to create either a music playlist or a movie playlist.
                 It stores the user's own list, asks a friend for their list, removes duplicate items,
                 sorts both playlists alphabetically, combines them into a master playlist, and finally
                 shuffles the master playlist to produce a randomized final playlist.
'''


import random
import time as t

#####----------MUSIC PLAYLIST----------#####

def shuffleList(final_master):
    #Suffling the final music playlist
    random.shuffle(final_master)
    print('\n')
    t.sleep(2)
    print('-----SHUFFLED MASTER PLAYLIST-----')
    for index in final_master:
        print(index)


def master_list(my_songs, unique_friend_songs):
    # Creates the final playlist combining both sorted lists
    final_master = my_songs + unique_friend_songs

    t.sleep(2)
    print('\n-----COMBINED MUSIC PLAYLIST-----')
    for count in final_master:
        print(count)
    
    t.sleep(2)
    print('\n-----SORTED MUSIC PLAYLIST-----')
    final_master.sort()
    for num3 in final_master:
        print(num3)

    shuffleList(final_master)


def sortList(my_songs, unique_friend_songs):
    #Sorts both playlists separately
    print('-----SORTING PLAYLIST ALPHABETICALLY-----' + '\n')
    t.sleep(1)
    print('Sorting my playlist.....')
    t.sleep(2)
    my_songs.sort()
    for num1 in my_songs:
        print(num1)
    print('\n')
    print('Sorting your playlist.....')
    t.sleep(2)
    unique_friend_songs.sort()
    for num2 in unique_friend_songs:
        print(num2)

    master_list(my_songs, unique_friend_songs)


def check_list(my_songs, friend_songs):
    unique_friend_songs = [] #This list will store only the friend's songs that are not duplicates

    # Checks friend's each song
    for song in friend_songs:
        # If the song is not already in my list, adds to the list
        if song not in my_songs:
            unique_friend_songs.append(song)
        else:
            # Let the user know a duplicate was found
            t.sleep(1)
            print(f'\nDuplicate removed: {song}')

    t.sleep(2)
    print('\nMy music playlist after checking for repeats:')
    for count1 in my_songs:
        print(count1)

    t.sleep(1)
    print('\nYour music playlist after checking for repeats:')
    for count2 in unique_friend_songs:
        print(count2)
    print('\n')

    sortList(my_songs, unique_friend_songs) #Calling function to sort the list alphabetically


def friend_musicList(my_music_list):
    print('\n')
    t.sleep(2)
    print("-----YOUR MUSIC PLAYLIST-----")
    t.sleep(1)
    # Asks how many songs the friend wants to enter
    try:
        count = int(input("How many songs do you want on your playlist? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    frnd_music_list = [0] * count
    print('Please enter your music list:')

    for index in range(len(frnd_music_list)):
        frnd_music_list[index] = input(f'Enter song #{index+1}: ')

    print('\nYour playlist contains:')
    for item in frnd_music_list:
        print(item)

    check_list(my_music_list, frnd_music_list) #Calling function to check for duplicate songs in friend's list


def make_musicList():
    #Creates the music list of 5
    my_music_list = [0] * 5
    print('\n')
    t.sleep(2)
    print('-----MY MUSIC PLAYLIST-----')
    my_music_list = ['South on Ya by Luke Combs', 'Safari Song by Greta Van Fleet', 'Fly Like an Eagle by Steve Miller Band', 'Driving to Hawaii by Summer Salt', 'Life in the Fast Lane by Eagles']
    #Prints the user's music list
    print('These are the songs in my music playlist: ' + '\n')
    for index in range(len(my_music_list)):
        print(my_music_list[index])

    friend_musicList(my_music_list) #Calling function for friend's playlist 


#####----------MOVIE PLAYLIST----------#####


def shuffle_movie_list(final_master):
    #Suffling the final movie playlist
    random.shuffle(final_master)
    print('\n')
    t.sleep(2)
    print('-----SHUFFLED MASTER PLAYLIST-----')
    for index in final_master:
        print(index)


def master_movie_list(my_movies, unique_friend_movies):
    # Creates the final playlist combining both sorted lists
    final_master = my_movies + unique_friend_movies

    t.sleep(2)
    print('\n-----COMBINED MOVIE PLAYLIST-----')
    for count in final_master:
        print(count)
    
    t.sleep(2)
    print('\n-----SORTED MOVIE PLAYLIST-----')
    final_master.sort()
    for num3 in final_master:
        print(num3)

    shuffle_movie_list(final_master)


def sort_movie_list(my_movies, unique_friend_movies):
    #Sorts both playlists separately
    print('-----SORTING PLAYLIST ALPHABETICALLY-----' + '\n')
    t.sleep(1)
    print('Sorting my playlist.....')
    t.sleep(2)
    my_movies.sort()
    for num1 in my_movies:
        print(num1)
    print('\n')
    print('Sorting your playlist.....')
    t.sleep(2)
    unique_friend_movies.sort()
    for num2 in unique_friend_movies:
        print(num2)

    master_movie_list(my_movies, unique_friend_movies)


def check_movie_list(my_movies, friend_movies):
    unique_friend_movies = [] #This list will store only the friend's movies that are not duplicates

    # Checks friend's each song
    for movie in friend_movies:
        # If the song is not already in my list, adds to the list
        if movie not in my_movies:
            unique_friend_movies.append(movie)
        else:
            # Let the user know a duplicate was found
            t.sleep(1)
            print(f'\nDuplicate removed: {movie}')

    t.sleep(2)
    print('\nMy movie playlist after checking for repeats:')
    for count1 in my_movies:
        print(count1)

    t.sleep(1)
    print('\nYour movie playlist after checking for repeats:')
    for count2 in unique_friend_movies:
        print(count2)
    print('\n')

    sort_movie_list(my_movies, unique_friend_movies) #Calling function to sort the list alphabetically


def friend_movieList(my_movie_list):
    print('\n')
    t.sleep(2)
    print("-----YOUR MOVIE PLAYLIST-----")
    t.sleep(1)
    # Asks how many movies the friend wants to enter
    try:
        count = int(input("How many movies do you want on your playlist? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    frnd_movie_list = [0] * count
    print('Please enter your movie list:')

    for index in range(len(frnd_movie_list)):
        frnd_movie_list[index] = input(f'Enter movie #{index+1}: ')

    print('\nYour movie list contains:')
    for item in frnd_movie_list:
        print(item)

    check_movie_list(my_movie_list, frnd_movie_list) #Calling function to check for duplicate movies in friend's list



def make_movieList():
    #Creates the movie list of 5
    my_movie_list = [0] * 5
    print('\n')
    t.sleep(2)
    print('-----MY MOVIE PLAYLIST-----')
    my_movie_list = ['Inception (2010)', 'The Dark Knight (2008)', 'Interstellar (2014)', 'La La Land (2016)', 'The Shawshank Redemption (1994)']
    #Prints the user's movie list
    print('These are the movies in my playlist: ' + '\n')
    for index in range(len(my_movie_list)):
        print(my_movie_list[index])

    friend_movieList(my_movie_list) #Calling function for friend's playlist 


def show_menu():
    #Displaying the menu to the user
    print("Hello! Let's make a playlist.")
    t.sleep(1)
    print('A. Music')
    print('B. Movie')
    print('C. Exit')

    #Taking user's input for the type of playlist
    choice = input('What kind of playlist do you want to make? ')
    if (choice == 'A'): 
        make_musicList() #Goes on to make the music playlist
    elif (choice == 'B'):
        make_movieList() #Goes on to make the movie playlist
    elif (choice == 'C'): #Exits the program
        print('Thank you for using the program.')
        print('Have a great day!')
        exit()
    else:
        print('Please enter a valid choice from the menu.') #Input validation
        show_menu()


def main():
    show_menu() #Calling the show_menu function


main() #Calling the main function