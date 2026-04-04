is_raining = True
have_umbrella = False
is_weekend = True

if is_raining and not have_umbrella:
    print("Stay home")
elif is_weekend and (not is_raining or have_umbrella):
    print("Go out")
elif not is_weekend:
    print("Go to work")