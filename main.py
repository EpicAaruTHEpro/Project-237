for i in range(1000):    
    with open("file" + str(i) + ".txt", "w+") as f:
        f.write("good morning")