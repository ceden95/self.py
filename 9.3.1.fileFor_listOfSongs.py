#the program uses the data of file made from a list of songs details in the following structure:
#song name;artist\band name;song length.
#the function my_mp3_playlist in the program returns a tuple of the next items:
#(name of the longest song, number of songs in the file, the most played artist)

def main():
    file_path = "C:\python course\9.3.1\9.3.1.listOfSongs.txt"
    playlist_tuple = my_mp3_playlist(file_path)
    print(playlist_tuple)


def my_mp3_playlist(file_path):
    """the function creates a tuple of 3 item from a date in file_path.
    :param file_path: file path to a file of playlist.
    :file_path type: str
    :return: (first_in_tuple, second_in_tuple, third_in_tuple).
    :rtype: tuple"""
    opened_file_path = open(file_path, "r")
    readed_file_path = opened_file_path.read()
    opened_file_path.close()
    
    #the longest song
    first_in_tuple = find_the_longest_song(readed_file_path)
    #number of songs in the file
    second_in_tuple = len(song_details_in_list(readed_file_path))
    #the most played artist
    third_in_tuple = find_most_played_artist(readed_file_path)
    ourTuple = (first_in_tuple, second_in_tuple, third_in_tuple)
    return ourTuple

def song_details_in_list(readed_file_path):
    splited_lines_file = readed_file_path.split("\n")
    song_details = [] 
    for item in splited_lines_file:
        splited_item = item.split(";")
        song_details.append(splited_item)
    return song_details

    
def find_the_longest_song(readed_file_path):
    song_details = song_details_in_list(readed_file_path)
    listOfSongsStr = []
    for item in song_details:
        listOfSongsStr.append(item[2])
        listOfSongsFloat = []
    for item in listOfSongsStr:
        a = item.replace(":", ".")
        strToFloat = float(a) 
        listOfSongsFloat.append(strToFloat)
    listOfSongsFloat.sort()
    longestSong = str(listOfSongsFloat[-1]).replace(".", ":")
    for item in song_details:
        if longestSong in item:
            longest_song = item[0]
    return longest_song


def find_most_played_artist(readed_file_path):     
    song_details = song_details_in_list(readed_file_path)
    listOfArtist = []
    for item in song_details:
        listOfArtist.append(item[1])
    times_played_dict = {}
    for item in listOfArtist:
        if item in times_played_dict.keys(): 
            times_played_dict[item] = int(times_played_dict[item]) + 1
        else: 
            times_played_dict[item] = 1
    maxValue = max(times_played_dict.values())
    ourArtist = ""
    for key in times_played_dict.keys():
        if(times_played_dict[key] == maxValue):
           ourArtist = key
           break 
    return ourArtist
    
main()
