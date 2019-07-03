inFile = open("state_contacts_change_ins_mut0.txt", 'r')

# create the global, stored array
factors = []

# read the new B factors from file
for line in inFile.readlines(): factors.append( float(line) )

# clear out the old B Factors
cmd.alter("ins_mut0", "b=0.0")

# update the B Factors with new properties
cmd.alter("ins_mut0 and name CA", "b=factors.pop(0)")

# color the protein based on the new B Factors of the alpha carbons
cmd.spectrum("b", "rainbow", "ins_mut0", 0.25, 2)

##################

inFile = open("state_contacts_change_ins_mut1.txt", 'r')

# create the global, stored array
factors = []

# read the new B factors from file
for line in inFile.readlines(): factors.append( float(line) )

# clear out the old B Factors
cmd.alter("ins_mut1", "b=0.0")

# update the B Factors with new properties
cmd.alter("ins_mut1 and name CA", "b=factors.pop(0)")

# color the protein based on the new B Factors of the alpha carbons
cmd.spectrum("b", "rainbow", "ins_mut1", 0.25, 2)

####################

inFile = open("state_contacts_change_ins_mut2.txt", 'r')

# create the global, stored array
factors = []

# read the new B factors from file
for line in inFile.readlines(): factors.append( float(line) )

# clear out the old B Factors
cmd.alter("ins_mut2", "b=0.0")

# update the B Factors with new properties
cmd.alter("ins_mut2 and name CA", "b=factors.pop(0)")

# color the protein based on the new B Factors of the alpha carbons
cmd.spectrum("b", "rainbow", "ins_mut2", 0.25, 2)

####################

inFile = open("state_contacts_change_ins_mut3.txt", 'r')

# create the global, stored array
factors = []

# read the new B factors from file
for line in inFile.readlines(): factors.append( float(line) )

# clear out the old B Factors
cmd.alter("ins_mut3", "b=0.0")

# update the B Factors with new properties
cmd.alter("ins_mut3 and name CA", "b=factors.pop(0)")

# color the protein based on the new B Factors of the alpha carbons
cmd.spectrum("b", "rainbow", "ins_mut3", 0.25, 2)
