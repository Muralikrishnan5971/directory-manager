import shutil

# source = "/Users/muralikrishnan/Downloads/dummy.txt"
# dest = "/Users/muralikrishnan/Downloads/dummy/"
# shutil.move(source, dest)

dummy = {
    "fruit":['apple', 'orange','pear'],
    "animal":['dog', 'tiger', 'fox'],
    "movie":['matrix', 'oldboy', 'readyplayerone']
}

def find_tiger(thing):
    for item in list(dummy.keys()):
        for x in dummy[item]:
            if x == thing:
                # print(x)
                return item 
          

thing = "orange"
item = find_tiger(thing)
print(item, thing)