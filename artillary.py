repeat = True
while repeat == True:
    m = int(input("Distance: "))
    if m > 1600 or m<100:
        print("Out of range.")
    else:
        r = (m-4224.25)/-4.21781
        print(round(r,1))