import os
import glob
import time

def sortFiles():
    where = os.getcwd()
    where = where.replace('\\' , '/')
    where = where + "/"

    os.mkdir('Audio')
    os.mkdir('Videos')
    os.mkdir('Documents')
    os.mkdir('Pictures')



    files = glob.glob('*')

    print("Sorting files...")

    for i in range(len(files)):
        x = files[i]
        bar = ['-','-','-','-','-','-','-','-','-']
        
        if x[-4:] == ".txt" or x[-4:] == ".rtf" or x[-3:] == ".py" or x[-4:] == ".doc" or x[-5:] == ".docx" or x[-4:] == ".odt" or x[-4:] == ".pdf" or x[-4:] == ".tex" or x[-4:] == ".wpd" or x[-4:] == ".ods" or x[-5:] == ".xlsm" or x[-4:] == ".xls" or x[-5:] == ".xlsx":
            file = x
            if file == os.path.basename(__file__):
                continue
            else:
                os.replace(where+file, where+"Documents/"+file)

        if x[-4:] == ".mp4" or x[-4:] == ".3g2" or x[-4:] == ".3gp" or x[-4:] == ".avi" or x[-4:] == ".flv" or x[-5:] == ".h264" or x[-4:] == ".m4v" or x[-4:] == ".mkv" or x[-4:] == ".mov" or x[-4:] == ".mpg" or x[-5:] == ".mpeg" or x[-3:] == ".rm" or x[-4:] == ".swf" or x[-4:] == ".vob" or x[-4:] == ".wmv":
            file = x
            os.replace(where+file, where+"Videos/"+file)

        if x[-4:] == ".wav" or x[-4:] == ".mp3" or x[-4:] == ".aif" or x[-4:] == ".cda" or x[-4:] == ".mid" or x[-5:] == ".midi" or x[-4:] == ".mpa" or x[-4:] == ".ogg" or x[-4:] == ".wma" or x[-4:] == ".wpl":
            file = x
            os.replace(where+file, where+"Audio/"+file)

        if x[-4:] == ".jpg" or x[-5:] == ".jpeg" or x[-4:] == ".bmp" or x[-4:] == ".png" or x[-3:] == ".ai" or x[-4:] == ".gif" or x[-4:] == ".ico" or x[-3:] == ".ps" or x[-4:] == ".psd" or x[-4:] == ".svg" or x[-4:] == ".tif" or x[-5:] == ".tiff" or x[-4:] == ".raw" or x[-4:] == ".arw":
            file = x
            os.replace(where+file, where+"Pictures/"+file)


    for i in range(len(bar)):
        print(bar[i], end=" ")
        time.sleep(0.2)
    print("Files Sorted.")
    time.sleep(2)

while True:
    sort = input("Entering 's' will sort all files in this directory into the respective folders: \nAudio \nVideos \nDocuments \nPictures \nsub-directories will not be affected \nEnter 'e' to exit. \n(s/e): ")

    if sort == "s":
        sortFiles()
        break
    elif sort == "e":
        break
    else:
        print("Invalid input\n\n")






