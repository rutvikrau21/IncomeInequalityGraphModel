import matplotlib.pyplot as plt
import os.path
import pandas as pd
import sys

import MST as mst
import efficiency as eff
import robustness as rbs


def main():
   #Gets User input
    initial, groups = get_user_input() #, totalnodes, inc

    #Creates Plots according to user inputs
    numPlots = 1#int(((totalnodes - initial)/inc)) + 1
    fig, axs = plt.subplots(numPlots, sharex=True)
    fig.suptitle('Efficiency vs Edges at nodes')
    i = 0

    #Loops user inputs so creates n starting points with nodes,
    for num1 in range(initial, initial+1, 1): #totalnodes + 1, inc):
            g = mst.Graph(num1)
            g.newMST()
            edges = int((num1 * (num1 - 1))/2 - (num1 - 1))+1
            interval = int(float(edges)*float(groups/100))

            Data = {'Edges': list(range(1, edges, interval)),
                    'Efficiency': [],
                    'Efficiency Alt': [],
                    # 'Network Connectivity': [],
                    # 'Robustness': [],
                    # 'Edge Robustness': []
                    }
            add_Network_Data(g, Data, interval)
            df = pd.DataFrame(Data, columns=['Edges', 'Efficiency',
                                             'Efficiency Alt',
                                             # 'Network Connectivity', 'Robustness',
                                             # 'Edge Robustness'
                                             ])
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
            # totalnodes = int((input("Type number of nodes \n")))
            # inc = int((input("Increment size \n")))
            groups = int((input("percentage of group added as a whole number \n")))
            # if (inc <= 0 or int(((totalnodes - initial)/inc)) < 0 or
            #         initial < 3 or totalnodes < initial or groups < 0):
            #     raise ValueError
            break

        except ValueError:
            print("Make sure your inputs are valid"
                  "Starting should be >3 and no negatives\n")
            if(input("Exit? y to exit\n")[0] == 'y'):
                exit()

    return initial, groups #totalnodes, inc

def add_Network_Data(g, Data, interval):
    while True:
        try:
            g.dist()
            Data['Efficiency'].append(eff.getEfficiency(g))
            Data['Efficiency Alt'].append(eff.getEfficiency2(g))
            # Data['Network Connectivity'].append(rbs.getNetworkConnectivity(g))
            # Data['Robustness'].append(rbs.getCriticalRemovalFraction(g))
            # Data['Edge Robustness'].append(rbs.getEdgeRobustness(g))
            g.newConnection(interval, 1)
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
            'E2': 'Efficiency Alt',
            'R': 'Robustness',
            'N': 'Network Connectivity',
            'ER': 'Edge Robustness'
        }
        try:
            if numPlots == 1:
                axs.plot(df['Edges'], df[measure[sys.argv[1]]])
                axs.set_title(name)
            else:
                axs[i].plot(df['Edges'], df[measure[sys.argv[1]]])
                axs[i].set_title(name)

        except KeyError:
            print("Invalid Input, input N, R, E2, or E or nothing for just data")
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