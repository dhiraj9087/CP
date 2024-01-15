# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    #print(student_marks[query_name])
    #q=[student_marks[query_name]]
    c=0
    q=list(student_marks[query_name])
    out=sum(q)/len(q)
    print("%.2f"%out)

