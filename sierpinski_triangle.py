import turtle 


pen = turtle.Turtle()

def draw_triangle(length):
  pen.setheading(180)
  for i in range(3):
    pen.rt(120)
    pen.fd(length)


def sierpinski_tri_recursive(n,length):
  if n == 1:
    draw_triangle(length) # base case

  else:
    sierpinski_tri_recursive(n-1,length)      # draw triangle ONE
    pen.rt(120)                # angle towards peak
    pen.fd(length * 2 ** (n - 2))             # move towards peak
    sierpinski_tri_recursive(n-1,length)      # draw triangle TWO
    pen.lt(120)                # angle towards right base of ONE
    pen.fd(length * 2 ** (n - 2))             # move towards right base of ONE
    sierpinski_tri_recursive(n-1,length)      # draw triangle THREE
    pen.fd(length * 2 **(n - 2))             # move to start
