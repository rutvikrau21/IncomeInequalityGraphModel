import matplotlib.pyplot as plt
import os.path
import pandas as pd
import sys

import MST as mst
import efficiency as eff
import robustness as rbs


def main():
   #Gets User input
    initial, totalnodes, inc = get_user_input()

    #Creates Plots according to user inputs
    numPlots = int(((totalnodes - initial)/inc)) + 1
    fig, axs = plt.subplots(numPlots, sharex=True)
    fig.suptitle('Efficiency vs Edges at nodes')
    i = 0

    #Loops user inputs so creates n starting points with nodes,
    for num1 in range(initial, totalnodes + 1, inc):
            g = mst.Graph(num1)
            g.newMST()

            Data = {'Edges': list(range(int((num1 * (num1 - 1))/2 - (num1 - 1)))),
                    'Efficiency': [],
                    'Network Connectivity': [],
                    'Robustness': []
                    }
            add_Network_Data(g, Data)

            df = pd.DataFrame(Data, columns=['Edges', 'Efficiency', 'Network Connectivity',
                                             'Robustness'])
            name = 'Nodes=' + str(num1)

            create_Graph(numPlots, axs, i, df, name)

            create_dataframe_folder(df, name)

            i+=1
    #Shows final plot
    if len(sys.argv) > 1:
        plt.show()

def get_user_input():
    while True:
        try:
            initial = int((input("Starting point \n")))
            totalnodes = int((input("Type number of nodes \n")))
            inc = int((input("Increment size \n")))
            if (inc <= 0 or int(((totalnodes - initial)/inc)) < 0 or
                    initial < 3 or totalnodes < initial):
                raise ValueError
            break

        except ValueError:
            print("Make sure your inputs are valid"
                  "Starting should be >3 and no negatives\n")
            if(input("Exit? y to exit\n")[0] == 'y'):
                exit()

    return initial, totalnodes, inc

def add_Network_Data(g, Data):
    while True:
        try:
            g.newConnection()
            Data['Efficiency'].append(eff.getEfficiency(g))
            Data['Network Connectivity'].append(rbs.getNetworkConnectivity(g))
            Data['Robustness'].append(rbs.getCriticalRemovalFraction(g))
        except IndexError:
            print("Network fully connected")
            break

def create_Graph(numPlots, axs, i, df, name):
    if len(sys.argv) == 1:
        pass

    else:
        # Dictionary for the dataframe measure
        measure = {
            'E': 'Efficiency',
            'R': 'Robustness',
            'N': 'Network Connectivity'
        }
        try:
            if numPlots == 1:
                axs.plot(df['Edges'], df[measure[sys.argv[1]]])
                axs.set_title(name)
            else:
                axs[i].plot(df['Edges'], df[measure[sys.argv[1]]])
                axs[i].set_title(name)

        except KeyError:
            print("Invalid Input, input N, R, or E or nothing for just data")
            exit()

def create_dataframe_folder(df, name):
    save_path = os.path.expanduser('~/Desktop/')
    newpath = os.path.join(save_path, 'dataframes/')

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    save_path = os.path.expanduser('~/Desktop/dataframes/')
    completeName = os.path.join(save_path, name + ".csv")

    df.to_csv(completeName, index=False, header=True)


if __name__ == "__main__":
    main()