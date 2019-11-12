def remove_duplicates(inp, rem):
    for i in range(len(rem) - 1):
        print(i, rem)
        while rem[i] == rem[i+1]:
            print(rem[i], rem[i+1])
            rem = rem[i+1:]
            print(rem)


if __name__ == '__main__':
    arr = 'aazxxzy'
    remove_duplicates("a", arr)