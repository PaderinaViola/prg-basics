employees = ["SMITH Lucy","JONES Janet","LEE Jerry",
               "JACKSON Peter","JOHNSON Rick",
               "LEWIS Terry","CLARKE Robin"]
emp_J = list(filter(lambda e: e[0]=="J", employees))
for x in emp_J:
    print(x)