#!/bin/bash

# Job Name and Files
#SBATCH -J 1600

# Job core configuration
#SBATCH -N 1
#SBATCH --exclusive

# Wall time in format Day-hour:minutes:seconds
#SBATCH --time=0-05:00:00

## Partition:short/normal and hardware constraint
#SBATCH --partition=thin

module load 2020
module load OpenBLAS/0.3.9-GCC-9.3.0
module load ScaLAPACK/2.1.0-gompi-2020a

/home/yuehao/freefem/bin/ff-mpirun -np 128 ns_3d.edp -v 0 
