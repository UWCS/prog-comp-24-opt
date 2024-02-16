#!/bin/bash
#
#SBATCH --job-name=optimise-cpu # Job name for tracking
#SBATCH --partition=cpu-batch  # Partition you wish to use (see above for list)
#SBATCH --cpus-per-task=1      # Number of CPU threads used by your job, set this upto 40 as required.
#SBATCH --mem-per-cpu=1500     # RAM in MB needed per core (i.e. 1500MB * 40 threads = 60GB RAM)
#SBATCH --time=2:00:00      # Job time limit set to 2 hours
#SBATCH --output=joboutput_%j.out # Standard out from your job

# Everything in this file can be modified, except the output location, printing
# the arguments being used to run it, and the time command to run the job

echo "Running with arguments: grid size=$GRID_SIZE, num agents=$NUM_AGENTS"
time python3 optimise.py $GRID_SIZE $NUM_AGENTS
