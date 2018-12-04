total = 0

with open('day1_input.txt') as infile:
    

        for line in infile:
            try:
                num = int(line)
                total += num
                #print(num)
            except ValueError:
                print(
                    "'{}' is not a number".format(line.rstrip())
                )

print(total)