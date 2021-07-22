import wget
import os


def ask():
    menu = int(
        input('1. Download file\n2. Delete file (by size)\n99. EXIT\n\nYour choose: '))
    if menu == 1:
        url = input('URL (with protocol): ')
        max_number = int(input('Max number 1-999: '))
        file_extension = input('File extension (.pdf, .html): ')
        file_name = input('File name: ')
        file_location = input('File location (full path): ')
        download_file(url, max_number, file_extension,
                      file_name, file_location)
    elif menu == 2:
        directory = input('Directory: ')
        file_size = int(input('File size (bytes): '))
        delete_file(directory, file_size)
    elif menu == 99:
        print('program exited')
        exit


def download_file(url, max_number, file_extension, file_name, file_location):
    os.mkdir(file_location)
    for i in range(1, max_number + 1):
        site = url + str(i)
        wget.download(
            site, file_location + file_name + '-' + str(i) + file_extension)

    print('\n\nDownloaded ' + str(i))


def delete_file(directory, file_size):
    for i in os.scandir(directory):
        if os.path.getsize(directory + i.name) > file_size:
            os.remove(directory + i.name)
            print('Deleted file more than ' +
                  str(file_size) + ' bytes: ' + i.name)


ask()
