is_male = False
is_tall = True

if is_male and is_tall:
    print("That person is a male and tall")

elif is_male and not(is_tall):
    print("That person is male but not tall")

elif not(is_male) and is_tall:
    print("That person is female and tall")

else:
    print("That person is female and short")
