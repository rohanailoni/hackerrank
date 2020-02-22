a=input()

if a[8:10]=="PM" and a[0:2]!="12":
    b=a.replace(a[0:2],str(int(a[0:2])+12))
    c=b.strip("PM")
    print(c)
if a[8:10]=="AM" and a[0:2]!="12":
    b=a.strip("AM")
    print(b)
if a[8:10]=="PM" and a[0:2]=="12":
    b=a.strip("PM")
    print(b)
if a[8:10]=="AM" and a[0:2]=="12":
    b=a.replace(a[0:2],"00")
    c=b.strip("AM")
    print(c)
