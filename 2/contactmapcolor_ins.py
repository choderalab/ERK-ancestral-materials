inFile = open("state_contacts_change_ins0.txt", 'r')

# create the global, stored array
factors = []

# read the new B factors from file
for line in inFile.readlines(): factors.append( float(line) )

# clear out the old B Factors
cmd.alter("ins0", "b=0.0")

# update the B Factors with new properties
cmd.alter("ins0 and name CA", "b=factors.pop(0)")

# color the protein based on the new B Factors of the alpha carbons
cmd.spectrum("b", "rainbow", "ins0", 0.25, 2)

##################

inFile = open("state_contacts_change_ins1.txt", 'r')

# create the global, stored array
factors = []

# read the new B factors from file
for line in inFile.readlines(): factors.append( float(line) )

# clear out the old B Factors
cmd.alter("ins1", "b=0.0")

# update the B Factors with new properties
cmd.alter("ins1 and name CA", "b=factors.pop(0)")

# color the protein based on the new B Factors of the alpha carbons
cmd.spectrum("b", "rainbow", "ins1", 0.25, 2)

####################

inFile = open("state_contacts_change_ins2.txt", 'r')

# create the global, stored array
factors = []

# read the new B factors from file
for line in inFile.readlines(): factors.append( float(line) )

# clear out the old B Factors
cmd.alter("ins2", "b=0.0")

# update the B Factors with new properties
cmd.alter("ins2 and name CA", "b=factors.pop(0)")

# color the protein based on the new B Factors of the alpha carbons
cmd.spectrum("b", "rainbow", "ins2", 0.25, 2)

####################

inFile = open("state_contacts_change_ins3.txt", 'r')

# create the global, stored array
factors = []

# read the new B factors from file
for line in inFile.readlines(): factors.append( float(line) )

# clear out the old B Factors
cmd.alter("ins3", "b=0.0")

# update the B Factors with new properties
cmd.alter("ins3 and name CA", "b=factors.pop(0)")

# color the protein based on the new B Factors of the alpha carbons
cmd.spectrum("b", "rainbow", "ins3", 0.25, 2)
