# Basis of a test
# you'll be testing functions or methods, these need to be called or initialised
# having controlled inputs for known outputs
    # and testing for these

def make_dough(arg1, arg2):
    if arg1 != 'water' and arg2 != 'water':
        return 'not dough'
    elif arg1 != 'flour' and arg2 != 'flour':
        return 'not dough'
    elif 'water' in [arg1, arg2] and 'flour' in [arg1, arg2]:
        return 'dough'

def bake_dough(arg1):
    if arg1 == 'dough':
        return 'Naan'
    else:
        return 'not Naan'



# # Make test for make_dough
# print("testing make_dough with 'water' and 'flour'. Expected ---> 'dough'")
# print(make_dough('water', 'flour') == 'dough')
# print("when calling make_dough('water', 'flour') got:", make_dough('water', 'flour'))
#
# # when I pass in cement and water, or anything else... I should get: 'not dough'
# print(make_dough('cement', 'water') == 'not dough')
# print("when calling make_dough('water', 'cement') got:", make_dough('water', 'cement'))

# Make test for bake_dough
# print("testing bake_dough with 'dough'. Expected ---> 'Naan'")
# print(bake_dough('dough') == 'Naan')
# print("when calling bake_dough('dough'), got:", bake_dough('dough'))

# When baked_dough is passed something other than dough it should output 'not Naan'

# Make test for not dough
print("Testing make_dough with 'water' and 'cement'. Expect --> 'not dough' ")
print(make_dough('water', 'cement') == 'not dough')
print("when calling make_dough('water', 'cement') got:", make_dough('water', 'cemet'))

# Make test for not Naan
print("testing bake_dough with 'chicken'. Expected ---> 'not Naan'")
print(bake_dough('chicken') == 'not Naan')
print("when calling bake_dough('chicken'), got:", bake_dough('chicken'))