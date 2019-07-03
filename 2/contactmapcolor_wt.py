inFile = open("state_contacts_change_wt0.txt", 'r')

# create the global, stored array
factors = []

# read the new B factors from file
for line in inFile.readlines(): factors.append( float(line) )

# clear out the old B Factors
cmd.alter("wt0", "b=0.0")

# update the B Factors with new properties
cmd.alter("wt0 and name CA", "b=factors.pop(0)")

# color the protein based on the new B Factors of the alpha carbons
cmd.spectrum("b", "rainbow", "wt0", 0.25, 2)

##################

inFile = open("state_contacts_change_wt1.txt", 'r')

# create the global, stored array
factors = []

# read the new B factors from file
for line in inFile.readlines(): factors.append( float(line) )

# clear out the old B Factors
cmd.alter("wt1", "b=0.0")

# update the B Factors with new properties
cmd.alter("wt1 and name CA", "b=factors.pop(0)")

# color the protein based on the new B Factors of the alpha carbons
cmd.spectrum("b", "rainbow", "wt1", 0.25, 2)

####################

inFile = open("state_contacts_change_wt2.txt", 'r')

# create the global, stored array
factors = []

# read the new B factors from file
for line in inFile.readlines(): factors.append( float(line) )

# clear out the old B Factors
cmd.alter("wt2", "b=0.0")

# update the B Factors with new properties
cmd.alter("wt2 and name CA", "b=factors.pop(0)")

# color the protein based on the new B Factors of the alpha carbons
cmd.spectrum("b", "rainbow", "wt2", 0.25, 2)
