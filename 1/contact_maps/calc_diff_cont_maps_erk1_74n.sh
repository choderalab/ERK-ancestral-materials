#!/bin/bash
#BSUB -J erk1_74n
#BSUB -n 10
#BSUB -R span[ptile=10]
#BSUB -R rusage[mem=20]
#BSUB -W 48:00
#BSUB -o /home/rafal.wiewiora/job_outputs/%J.stdout
#BSUB -eo /home/rafal.wiewiora/job_outputs/%J.stderr

cd $LS_SUBCWD
python calc_diff_cont_maps_erk1_74n.py
