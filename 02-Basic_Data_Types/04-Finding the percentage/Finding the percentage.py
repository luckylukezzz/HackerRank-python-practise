#https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    
    student_marks = {}
    for _ in range(int(input())):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = input()
    
    x=(sum(student_marks[query_name])/3)
    print(("%.2f"%(x)))
