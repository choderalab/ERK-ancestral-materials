#!/bin/bash
#BSUB -J erk1_wt
#BSUB -q gpuqueue
#BSUB -n 1
#BSUB -R span[ptile=1]
#BSUB -R rusage[mem=10]
#BSUB -gpu num=1
#BSUB -W 48:00
#BSUB -o /home/rafal.wiewiora/job_outputs/%J.stdout
#BSUB -eo /home/rafal.wiewiora/job_outputs/%J.stderr

cd $LS_SUBCWD
python prep_equilibrate_phospho.py ERK1_WT.pdb
