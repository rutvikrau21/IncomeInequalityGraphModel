import MST as mst
import matplotlib.pyplot as plt
import pandas as pd
import os.path


def main():
    while True:
        try:
            num = int((input("Type number of nodes \n")))
            break
        except ValueError:  # catch the *specific* exception
            print("Enter numbers only")

    fig, axs = plt.subplots(int(num/5), sharex=True)
    fig.suptitle('Efficiency vs Edges at nodes')
    i = 0

    for num1 in range(5, num + 1, 5):
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
        name = 'Nodes=' + str(num1)


        axs[i].plot(df['Edges'], df['Efficiency'])
        axs[i].set_title(name)

        save_path = os.path.expanduser('~/Desktop/')
        newpath = os.path.join(save_path, 'dataframes/')
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        save_path = os.path.expanduser('~/Desktop/dataframes/')
        completeName = os.path.join(save_path, name+".csv")

        df.to_csv(completeName, index = False, header=True)
        i+=1
    plt.show()

if __name__ == "__main__":
    main()