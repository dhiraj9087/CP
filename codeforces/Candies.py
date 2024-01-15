# for i in range((int(input()))):
#     n=int(input())
    # def construct_sequence(n):
    #     seq = []
    #     while n > 1:
    #         if n % 2 == 1:
    #             seq.append('1')
    #             n //= 2
    #         else:
    #             seq.append('2')
    #             n -= 1
    #     seq.append('1')
    #     return ''.join(seq[::-1])
    # if n == 1:
    #     print('1')
    # elif n % 2 == 0:
    #     print('-1')
    # else:
    #     print(construct_sequence(n))
def get_sequence(x, n, spells_used):
    if x == n:
        return spells_used
    elif spells_used >= 40:
        return "impossible"
    else:
        sequence1 = get_sequence(2*x-1, n, spells_used+1)
        sequence2 = get_sequence(2*x+1, n, spells_used+1)
        if sequence1 != "impossible":
            return "1" + sequence1
        elif sequence2 != "impossible":
            return "2" + sequence2
        else:
            return "impossible"

n = 10
sequence = get_sequence(1, n, 0)
print(sequence)

    