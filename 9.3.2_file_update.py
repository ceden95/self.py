#the program gets a file_path to a file of song details with the following structure:
#song name;artist\band name;song length.
#the function my_mp4_playlist in the program changes the name of the song in the 3rd line in file_path to new_song.

def main():
    file_path = "C:\python course\9.3.2\9.3.2.txt"
    new_song = "halo"
    my_mp4_playlist(file_path, new_song)

def my_mp4_playlist(file_path, new_song):
    """the function edit the file with the name of the song in the 3rd line
    :param file_path: file path to songs details.
    :file_path type: string.
    :param new_song: the word to replace the song name in the 3rd line.
    :new_song type: string."""
    opened_file_path = open(file_path, "r")
    readed_file_path = opened_file_path.read()
    opened_file_path.close()
    new_list_for_file = update_new_song_list(readed_file_path, new_song)
    print(new_list_for_file)
    create_new_file(file_path, new_list_for_file)



def update_new_song_list(readed_file_path, new_song):
    """the function replace the name of the song in the 3rd line to new_song
    and return is as a string.
    :param readed_file_path: the content of 'file_path' file.
    :readed_file_path type: string.
    :param new_song: string of the new song to replace.
    :return: the content of the file with the updated new_song.
    :rtype: srt."""
    splited_lines_file = readed_file_path.split("\n")
    song_details = [] 
    for item in splited_lines_file:
        splited_item = item.split(";")
        song_details.append(splited_item)

    song_details[3][0] = new_song
    return song_details 


def create_new_file(file_path, new_list_for_file):
    """the function updates the file_path to the 'new_list_for_file'(string of
    song detailes with the new updated song).
    :param file_path: the file path to the file neeads to be updated.
    :file_path type: string.
    :param new_list_for_file: string with the content of file_path with the new updated song.
    :new_list_for_file type: string."""
    opened_file_for_update = open(file_path, "w")
    new_list = []
    for item in new_list_for_file:
        str_of_song_details = ";".join(item)
        new_list.append(str_of_song_details)
    print(new_list)
    the_new_list = "\n".join(new_list)
    print(the_new_list)

    opened_file_for_update.write(the_new_list)
    opened_file_for_update.close()


main()



