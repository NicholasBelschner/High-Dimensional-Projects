import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_lammps_dump(filename):
    data = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        parsing_atoms = False
        for line in lines:
            if line.startswith('ITEM: ATOMS'):
                parsing_atoms = True
                continue
            if line.startswith('ITEM:'):
                parsing_atoms = False
            if parsing_atoms:
                data.append(line.strip().split())
    if data:
        return pd.DataFrame(data, columns=['id', 'type', 'x', 'y', 'z', 'vx', 'vy', 'vz'], dtype=float)
    else:
        return pd.DataFrame()  # Return an empty DataFrame if no atom data is found

# Load simulation data
data = read_lammps_dump('lammps_output.dump')

if data.empty:
    print("The DataFrame is empty. Please check the input file.")
else:
    # Calculate the mean square displacement (MSD)
    def calculate_msd(data):
        n_atoms = data['id'].nunique()
        timesteps = len(data) // n_atoms
        initial_positions = data[['x', 'y', 'z']].iloc[:n_atoms].values
        msd = []

        for t in range(timesteps):
            current_positions = data[['x', 'y', 'z']].iloc[t*n_atoms:(t+1)*n_atoms].values
            displacements = current_positions - initial_positions
            squared_displacements = (displacements ** 2).sum(axis=1)
            msd.append(squared_displacements.mean())
        
        return msd

    msd = calculate_msd(data)

    # Plot MSD
    plt.figure(figsize=(10, 6))
    plt.plot(msd)
    plt.xlabel('Time Step')
    plt.ylabel('Mean Square Displacement')
    plt.title('Mean Square Displacement of Nanoparticles')
    plt.grid(True)
    plt.savefig('msd_plot.png')
    plt.show()