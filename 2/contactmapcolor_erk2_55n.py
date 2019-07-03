inFile = open("tyr183_contact_diff_erk2_55n.txt", 'r')

# create the global, stored array
factors = []

# read the new B factors from file
for line in inFile.readlines(): factors.append( float(line) )

# clear out the old B Factors
cmd.alter("erk2_55n_start", "b=0.0")

# update the B Factors with new properties
cmd.alter("erk2_55n_start and n. CA", "b=factors.pop(0)")

# color the protein based on the new B Factors of the alpha carbons
cmd.spectrum("b", "rainbow", "erk2_55n_start and n. CA", -0.25, 0.25)
