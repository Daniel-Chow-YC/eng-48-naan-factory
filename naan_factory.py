# Basis of a test
# you'll be testing functions or methods, these need to be called or initialised
# having controlled inputs for known outputs
    # and testing for these

# Make test for make_dough
# To make dough it will take in 'water' and 'flour' to make dough.
print(make_dough('water', 'flour') == 'dough')

# Make test for bake_dough
#Then with the dough we should be able to put it into the oven, and get out a Naan.
print(bake_dough('dough') == 'Naan')