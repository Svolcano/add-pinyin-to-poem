with open("multi.txt", 'w') as wh:
    for i in range(1, 10):
        j = 1
        while j <= i:
            wh.write("  %s * %s = %s\t" % (i, j, i*j))
            j += 1
        wh.write("\n")
            