def command(statement:list, values:list=[] ):
    options = dict()
        
    if statement[0] == "insert":
        values.insert(int(statement[1]), int(statement[2]))
    elif statement[0] == "remove":
        values.remove(int(statement[1]))
    elif statement[0] == "append":
        values.append(int(statement[1]))
    elif statement[0] == "sort":
        values = sorted(values)
    elif statement[0] == "reverse":
        values.reverse()    
    elif statement[0] == "print":
        print(values)
    elif statement[0] == "pop":
        values.pop()
    else:
        raise("unknown option")
    
    return values
    


if __name__ == '__main__':
    
    N = int(input())
    values = []
    for i in range(N):
        statement = input().split(" ")
        values = command(statement, values)