figures=str(input())
if figures=="square":
     a=float(input())
     area_square=a*a
     print("{0:.3f}".format (area_square))
elif figures=="rectangle":
    side1=float(input())
    side2=float(input())
    area_rectangle=side1*side2
    print("{0:.3f}".format (area_rectangle))
elif figures=="circle":
    r=float(input())
    radious_circle=3.14159*(r*r)
    print("{0:.3f}".format (radious_circle))
elif figures=="triangle":
    side=float(input())
    h=float(input())
    area_triangle=(side*h)/2
    print("{0:.3f}".format (area_triangle))

