commands = open('input/7', 'r').read().splitlines()

class Directory:

    def __init__(self, name, parent):
        self.name = name
        self.children = []
        self.parent = parent

class File:

    def __init__(self, name, size):
        self.name = name
        self.size = size

def build_file_tree(commands):

    root = Directory("/", None)
    cur = root
    for line in commands[1:]:
        p = line.split()
        if p[0] != "$":
            if p[0] == "dir":
                cur.children.append(Directory(p[1], parent=cur))
            #ls output, add files
            else:
                cur.children.append(File(name=p[1], size=int(p[0])))
        #we're changing directories 
        else:
            if p[1] == "cd":
                if p[2] != "..":
                    destination = p[2]
                    #find the subdirectory and move our pointer
                    for child in cur.children:
                        if child.name == destination:
                            cur = child
                #otherwise find the parent and go there
                else:
                    cur = cur.parent

    return root

def get_dir_sizes_under_100(d, total_under_100k):
    sub_dirs, total_size = [], 0

    for child in d.children:
        if isinstance(child, Directory):
            sub_dirs.append(child)
        else:
            total_size += child.size

    for sub_dir in sub_dirs:
        t, total_under_100k = get_dir_sizes_under_100(sub_dir, total_under_100k)
        total_size += t

    if total_size < 100000:
        total_under_100k += total_size

    return total_size, total_under_100k


def part_1():
    root = build_file_tree(commands)
    total_under_100k = 0
    _, t = get_dir_sizes_under_100(root, total_under_100k)
    print(t)

    
def get_dir_size_and_store(d, l):
    sub_dirs, total_size = [], 0

    for child in d.children:
        if isinstance(child, Directory):
            sub_dirs.append(child)
        else:
            total_size += child.size

    for sub_dir in sub_dirs:
        _, t = get_dir_size_and_store(sub_dir, l)
        total_size += t

    l[d] = total_size

    return sub_dirs, total_size


def part_2():
    TOTAL_DISK_SPACE = 70000000
    SPACE_NEEDED = 30000000

    root = build_file_tree(commands)
    l = {}
    get_dir_size_and_store(root, l)

    UNUSED_SPACE = TOTAL_DISK_SPACE - l[root]
    difference = SPACE_NEEDED - UNUSED_SPACE

    print(min([v for (_, v) in l.items() if v >= difference]))
    
#part_1()
part_2()
