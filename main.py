# Author: Jason Chase
# Date: 2/1/23
# this script will grab all the JSON files from ./json/ and put an ansible script into ./ansible/

from Lib.ansibledel import *
import shutil
import os
if __name__ == '__main__':
    # load jsonloc
    templates = os.listdir('./json/')
    if len(templates) == 0:
        print("No templates to work on.")
        quit(-1)
    # create ./ansible file
    try:
        if os.path.exists("./ansible"):
            shutil.rmtree("./ansible")

        os.mkdir("./ansible")
    except:
        print("failed to create ansilbe folder. Please check read/write permissions")
        quit(-1)

    try:

        # create the templates
        for i in range(len(templates)):

            # open file
            loc = "./json/" + templates[i]
            f = open(loc)
            ftext = f.read()
            f.close()

            # create ansible file
            ansi = createansibledel(ftext)
            name = templates[i]
            name = name[:-5]
            loc = "./ansible/" + name + ".yaml"
            f = open(loc, 'w')
            f.write(ansi)
            f.close()


    except:
        print("Failed to create ansible playbooks")
        quit(-1)
    #print(createansibledel(ftext))