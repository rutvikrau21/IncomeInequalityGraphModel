import MST as mst

def main():
    while True:
        try:
            num1 = int((input("Type number of nodes \n")))
            break
        except ValueError:  # catch the *specific* exception
            print("Enter numbers only")

    g = mst.Graph(num1)
    g.newMST()



    print("Matrix")
    print(g.graph)
    print("\n")


    print("Distances")

    while True:
        try:
            g.newConnection()
            print(mst.getEfficiency(g))
        except IndexError:
            print("Network fully connected")
            break

if __name__ == "__main__":
    main()