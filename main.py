import MST as mst
import matplotlib.pyplot as plt
import pandas as pd

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

    Data = {'Edges': list(range(int((num1 * (num1 - 1))/2 - (num1 - 1)))),
            'Efficiency': []
            }

    while True:
        try:
            g.newConnection()
            Data['Efficiency'].append(mst.getEfficiency(g))
        except IndexError:
            print("Network fully connected")
            break

    df = pd.DataFrame(Data, columns=['Edges', 'Efficiency'])

    plt.plot(df['Edges'], df['Efficiency'])
    plt.title('Efficiency vs Edges')
    plt.xlabel('Edges added')
    plt.ylabel('Efficiency')
    plt.show()

if __name__ == "__main__":
    main()
