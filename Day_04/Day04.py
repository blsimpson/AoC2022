def get_input(file_name):
    with open(file_name, 'r') as f:
        data = f.read().split("\n")
    return data
    
def part_one(data):
    count = 0
    for line in data:
        i1, i2 = line.split(',')
        i1_start, i1_end = [int(x) for x in i1.split("-")]
        i2_start, i2_end = [int(x) for x in i2.split("-")]
        if (i2_start <= i1_start and i1_end <= i2_end) or (i1_start <= i2_start and i2_end <= i1_end):
            count += 1
    return(count)

def part_two(data):
    count = 0
    for line in data:
        i1, i2 = line.split(',')
        i1_start, i1_end = [int(x) for x in i1.split("-")]
        i2_start, i2_end = [int(x) for x in i2.split("-")]
        if (i1_start <= i2_end and i2_start <= i1_end):
            count += 1
    return(count)

def main():
    file_name = ".\day_04\input.txt"
    data = get_input(file_name)
    print(f"The answer to part one is {part_one(data)}")
    print(f"The answer to part one is {part_two(data)}")

if __name__ == "__main__":
    main()