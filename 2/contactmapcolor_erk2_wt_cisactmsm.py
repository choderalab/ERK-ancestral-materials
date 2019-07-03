inFile = open("joint_statespace_samples/wt_diff_contmap.txt", 'r')

# create the global, stored array
factors = []

# read the new B factors from file
for line in inFile.readlines(): factors.append( float(line) )

# clear out the old B Factors
cmd.alter("erk2_wt_start", "b=0.0")

# update the B Factors with new properties
cmd.alter("erk2_wt_start and n. CA", "b=factors.pop(0)")

# color the protein based on the new B Factors of the alpha carbons
cmd.spectrum("b", "rainbow", "erk2_wt_start and n. CA", 0.5, 2)
