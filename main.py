import os

#should rename this class
#This class creates the files/directories which will be used to store links

def create_project_dir(directory):
    if not os.path.exists(directory):
        print("creating directory" + directory)
        os.makedirs(directory)


def create_data_files(project_name, url):
    queue = project_name + '/queue.txt'
    visited = project_name + '/visited.txt'
    if not os.path.isfile(queue):
        write_file(queue, url)
    if not os.path.isfile(visited):
        write_file(visited, '')


def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


def append(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


def delete(path):
    with open(path, 'w'):
        pass


def fileToSet(fileName):
    results = set()
    with open(fileName, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
        return results


def setToFile(links, file):
    delete(file)
    for link in sorted(links):
        append(file, link)
