import os
import random

# generate a random number

file = "output.txt"
directory = "C:\\Users\\kakoumet\\OneDrive - Microsoft Office 365\\Documents\\BotCommits\\"

def commit(file, new_text):
    # remove content of file
    f = open(file, "w")
    f.close()
    os.system(f"cd {directory} "
              f"&& echo {new_text} > output.txt "
              f"&& git add {file} "
              f"&& git commit -m \"commit of {new_text}\" "
              f"&& git push origin master")


if __name__ == '__main__':
    nb_commits = random.randint(0,25)
    print(f"nb_commits : {nb_commits}")
    for i in range(nb_commits):
        newText = str(random.randint(1,100000))
        nb_number = random.randint(1, 1000)
        newText = nb_number * newText
        commit(file, newText)