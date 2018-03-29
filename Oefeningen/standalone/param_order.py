def display_info(a, b, *args,  instructor="Colt", **kwargs):
    print(f"a: {a}\nb: {b}\n*args: {args}\ninstructor: {instructor}\n**kwargs: {kwargs}")


display_info(1, 2, 3, last_name="Steele", job="Instructor")

#a: 1
#b: 2
#*args: (3,)
#instructor: Colt
#**kwargs: {last_name:"Steele", job:"Instructor"}
