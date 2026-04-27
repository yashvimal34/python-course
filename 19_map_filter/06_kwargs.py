def marks(**kwargs):
    # kwargs is the dictionary with all the key value pairs which were to marks.
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

marks(Rahul=78, Yash=90, Krishna=45, Utkarsh=89)