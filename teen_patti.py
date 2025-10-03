def findPokerHand(cards):
    ranks=[]
    suits=[]
    possibleRanks=[]
    for card in cards:
        if len(card)==2:
            rank=card[0]
            suit=card[1]
        else:
            rank=card[0:2]
            suit=card[2]
        if rank=="A":
                rank=14
        elif rank=="K":
                rank=13
        elif rank=="Q":
                rank=12
        elif rank=="J":
                rank=11
        ranks.append(int(rank))
        suits.append(suit)
    #print(ranks)
    #print(suits)
    sortedRanks = sorted(ranks)    # sorted in ascending order e.g: [9,10,11,12,13,14]
    ranks = sortedRanks
    #print(ranks)
    #print(sortedRanks)

    if find_flush(suits):
        if find_doubly(ranks):         # rank 5
            possibleRanks.append(5)
            print("Doubly")
        else :
            possibleRanks.append(3)    # rank 3
            print("Color")
    elif not find_flush(suits):
        if find_trail(ranks):          # rank 6
            possibleRanks.append(6)
            print("Trail")
        elif find_straight(ranks):
            possibleRanks.append(4)     # rank 4
            print("Run")
        elif find_juut(ranks):
            possibleRanks.append(2)      # rank 2
            print("Juut")
        else:
            possibleRanks.append(1)      # rank 1
            print("High Card")
    return possibleRanks

def find_flush(colors):
    if colors.count(colors[0])== 3:
        return True
    else:
         return False

def find_doubly(numbers):
    if find_straight(numbers):
        return True
    else:
        return False 

def find_straight(numbers):
    # print(numbers)
    if is_difference_one(numbers):
        return True
    else:
        return False

def find_juut(numbers):
    unique_numbers = list(set(numbers))   # finding unique numbers
    counts=[]
    for un in unique_numbers:
        counts.append(numbers.count(int(un)))
    if 2 in counts:
        return True
    else:
        return False

def is_difference_one(n):
    if n[2]-n[1]==1 and n[1]-n[0]==1:
        return True
    else:
        return False

def find_trail(numbers):
    unique_number = list(set(numbers))
    unique_number = unique_number[0]
    if numbers.count(int(unique_number)) == 3:
        return True
    else:
        False

if __name__ == "__main__":
    findPokerHand(["AH","AC","AD"])     # Trail
    findPokerHand(["AH","QH","KH"])     # Doubly
    findPokerHand(["10S","9C","8H"])    # Run
    findPokerHand(["5H","10H","KH"])    # Color
    findPokerHand(["JH","6D","JH"])     # Juut
    findPokerHand(["2H","7D","9C"])     # High Card