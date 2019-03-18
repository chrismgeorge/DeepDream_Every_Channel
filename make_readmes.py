import os

directory_path = "./white_box_layers/"

for folder in os.listdir(directory_path):
    if ('pre' in folder):
        new_path = directory_path + folder + '/'
        i = 0
        new_read_me = new_path + "README.md"
        text = ""
        for file in os.listdir(new_path):
            if (".jpg" in file):
                name = folder + '_channel_' + '{num:0{width}}'.format(num=i, width=5) + '.jpg'
                text += '<p align="center">  <img src="'+name+'?"> </p>'
                text += '<p align="center">'+ name +'</p>'
                text += "\n\n***\n\n"
                i += 1

        file = open(new_read_me, "w")
        file.write(text)
