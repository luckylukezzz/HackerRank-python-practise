#https://www.hackerrank.com/challenges/default-arguments/problem?isFullScreen=true


def print_from_stream(n,stream=EvenStream()):
    stream.__init__()
    for _ in range(n):
        print(stream.get_next())

