# Author: Jason Chase
# Date: 2/20/23
# version: 1.2
import json

# will take json string and return yaml string for ansible deletion
def createansibledel(jsontext):
    # grab the table
    ansibletext = "" # holds the text to be returned
    try:
        # load jsonfile
        jsonfile = json.loads(jsontext)

    except:
        print("failed to parse json file")
        quit(-1)


    try:
        # gets server name
        # must be the server name of inventory file
        servername = jsonfile['server']

        vars = []
        varnum = len(jsonfile['tasks'])
        for i in range(varnum):

            path = jsonfile['tasks'][i]['path']
            age = jsonfile['tasks'][i]['age']
            var = [path, age]
            vars.append(var)

    except:
        print("Failed to create anisble file. ")
        print("Please make sure below follows documentation standards.")
        print(jsontext)
        quit(-1)

    #print(vars)

    ansibletext += "---\n"
    ansibletext += "- name: Delete old files on server " + servername + "\n"
    ansibletext += "  hosts: " + servername + "\n"
    ansibletext += "  become: yes\n"
    ansibletext += "  tasks:\n"
    for i in range(varnum):

        ansibletext += "    - name: Find " + servername + " files in " + vars[i][0] + "\n"
        ansibletext += "      find:\n"
        ansibletext += "        paths: " + vars[i][0] + "\n"
        ansibletext += "        age: " + vars[i][1] + "\n"
        ansibletext += "        recurse: yes\n"
        ansibletext += "        file_type: file\n"
        ansibletext += "      register: files" + str(i) + "\n"
        ansibletext += "    - name: Delete " + servername + " files in " + vars[i][0] + "\n"
        ansibletext += "      file:\n"
        ansibletext += "        path: \"{{ item.path }}\"\n"
        ansibletext += "        state: absent\n"
        ansibletext += "      with_items: \"{{ files" + str(i) + ".files }}\"\n"

    return ansibletext
