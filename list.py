if __name__ == '__main__':
    N = int(input())  # Read the number of commands
    lst = []  # Initialize the list

    for _ in range(N):
        command = input().split()  # Read each command and split it into parts
        action = command[0]  # The action to be taken

        if action == 'insert':
            index = int(command[1])
            element = int(command[2])
            lst.insert(index, element)
        elif action == 'print':
            print(lst)
        elif action == 'remove':
            element = int(command[1])
            lst.remove(element)
        elif action == 'append':
            element = int(command[1])
            lst.append(element)
        elif action == 'sort':
            lst.sort()
        elif action == 'pop':
            lst.pop()
        elif action == 'reverse':
            lst.reverse()
