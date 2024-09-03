def node(inputs: list):
    output = 0
    x: tuple
    for x in inputs:
        output += x[0] * x[1]
    output = output/len(inputs)
    return(output)

# layer 1 (a)
#input
a0 = 1
a1 = -1

#layer 2 (b)
b0 = node([(a0,1),(a1,-1)])

print(b0)