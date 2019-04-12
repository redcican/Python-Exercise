# Check the type of a math sequences
# Arithmetic, Geometric or No pattern
# But without negative numbers

def mathSequences(arr):
    arith = set()
    geo = set()
    
    for i in range(1, len(arr)):
        number1 = arr[i] - arr[i-1];
        arith.add(number1);
        number2 = arr[i] / arr[i-1];
        geo.add(number2);

    if len(arith) == 1:
        return "Arithmetic"
    elif len(geo) == 1:
        return "Geometric"
    else:
        return -1
# "Arithmetic"
print(mathSequences([-10,-20,-30,-40]))
# "Geometric"
print(mathSequences([2,4,8,16]))
# -1
print(mathSequences([2,5,6,87,8]))


