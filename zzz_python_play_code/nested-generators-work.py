def gen():
    yield 1
    yield 2

for i in gen():
    for j in gen():
        
        print( 'i:', i, ', j:', j )

# prints:

# i: 1 , j: 1
# i: 1 , j: 2
# i: 2 , j: 1
# i: 2 , j: 2

# as desired

# nested generators work!
