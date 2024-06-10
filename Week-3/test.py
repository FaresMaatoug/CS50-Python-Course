list = {
    }

def main():
    i = 1
    while True:
        try:
            item = input("Item: ")
            filter(item, i)
            i += 1
        except KeyError:
            print("NOP")
        except EOFError:
            print("")
            break
    print(order(list))
    #print(list)


def filter(n, m):
    i = 1
    n = n.upper()
    if n not in list:
        list.update({i:n})
    else:
        i += 1
        list.update({i:n})

def order(a):
    length = len(a)
    return dict(sorted(a.items()))
    #for _ in range(length):


main()

