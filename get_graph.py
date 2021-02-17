import matplotlib.pyplot as plt
import os.path
import pandas as pd

import MST as mst
import efficiency as eff



def main():
    while True:
        try:
            initial = int((input("Starting point \n")))
            totalnodes = int((input("Type number of nodes \n")))
            inc = int((input("Type number of nodes \n")))
            if (inc <= 0 or int(((totalnodes - initial)/inc)) < 0):
                raise ValueError
            break
        except ValueError:
            print("Make sure your inputs are valid")

    fig, axs = plt.subplots(int(((totalnodes - initial)/inc) + 1), sharex=True)
    fig.suptitle('Efficiency vs Edges at nodes')
    i = 0

    for num1 in range(initial, totalnodes + 1, inc):
        g = mst.Graph(num1)
        g.newMST()

        Data = {'Edges': list(range(int((num1 * (num1 - 1))/2 - (num1 - 1)))),
                'Efficiency': []
                }

        while True:
            try:
                g.newConnection()
                Data['Efficiency'].append(eff.getEfficiency(g))
            except IndexError:
                print("Network fully connected")
                break

        df = pd.DataFrame(Data, columns=['Edges', 'Efficiency'])
        name = 'Nodes=' + str(num1)

        if int(((totalnodes - initial)/inc)) == 0:
            axs.plot(df['Edges'], df['Efficiency'])
            axs.set_title(name)
        else:
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