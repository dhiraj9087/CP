# import math
# import sys
# input=sys.stdin.readline
# def main():
#     n=int(input())
#     a=list(map(int,input().split()))
#     for i in range(n-2):
#         if a[i] < 0:
#             print("NO")
#             return
#         ele=a[i]
#         a[i]-=ele
#         a[i+1]-=(2*ele)
#         a[i+2]-=(ele)
#     if a[-1]!=0 or a[-2]!=0:
#         print("NO")
#         return
#     print("YES")
# for _ in range(int(input())):
#    main()
import turtle

# Function to draw a heart shape
def draw_heart():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(5)
    t.penup()
    t.color('red')
    t.goto(0, -200)
    t.begin_fill()
    t.left(140)
    t.forward(224)
    for _ in range(200):
        t.right(1)
        t.forward(2)
    t.left(120)
    for _ in range(200):
        t.right(1)
        t.forward(2)
    t.forward(224)
    t.end_fill()
    t.penup()

# Function to write "Sorry" message
def write_sorry():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(5)
    t.color('black')
    t.penup()
    t.goto(0, 0)
    t.write("Sorry", align="center", font=("Arial", 24, "normal"))

# Main function
def main():
    turtle.setup(width=600, height=600)
    draw_heart()
    write_sorry()
    turtle.done()

if __name__ == "__main__":
    main()
