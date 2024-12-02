from collections import Counter

def main() :
    input = open('input.txt', 'r')

    left_pairs, right_pairs = get_pairs_from_input(input)

    distance = get_distance_from_pairs(left_pairs, right_pairs)
    similarity = get_similarity_score(left_pairs, right_pairs)

    print(f"answer for part 1: {distance}")
    print(f"answer for part 2: {similarity}")

def get_pairs_from_input(input):
    left_side = []
    right_side = []

    for line in input:
        ids = line.split()
        left_side.append(int(ids[0]))
        right_side.append(int(ids[1]))

    left_side.sort()
    right_side.sort()

    return left_side, right_side

# Gets the answer for part 1
def get_distance_from_pairs(left, right):
    distance = 0

    for id_1, id_2 in zip(left, right):
        distance += abs(id_1-id_2)

    return distance

# Gets the answer for part 2
def get_similarity_score(left, right):
    similarity = 0
    counter = Counter(right)

    for id in left:

        if id in counter:
            similarity += id * counter[id]

    return similarity

if __name__ == "__main__":
    main()
