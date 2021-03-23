

def bubble_sort(list_demo):
    n = len(list_demo)
    for j in range(n-1):
        count = 0
        for i in range(n-1-j):
            if list_demo[i] > list_demo[i+1]:
                list_demo[i],list_demo[i+1] = list_demo[i+1],list_demo[i]
                count += 1
        if count == 0:
            return


if __name__ == "__main__":
    li = [1,7,9,5,3]
    print(li)
    bubble_sort(li)
    print(li)
