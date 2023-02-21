# ansiblefiledel
Creates Ansible workbooks to delete old files from a server based off simple config file.

how to run:
1) put .json files into ./json/
    .json schema is explained in "json structure.pdf"
2) create virtualenviroment
    virtualenv venv
3) go into virtualenv
    source ./venv/bin/activate
4) run script
    python main.py

if no errors you should have your workbooks in ./ansible/


example file:

---
- name: Delete old files in folder
  hosts: localhost
  become: yes
  tasks:
    - name: find files older than specified time
      find:
        paths: /path/to/folder/
        age: 10d
        recurse: yes
        file_type: file
      register: files1
    - name: delete files older than specified time
      file:
        path: "{{ item.path }}"
        state: absent
      with_items: "{{ files1.files }}"

