def get_age(dob_year):
    if(dob_year >= 2023):
        return 0

    elif(2022-dob_year >= 18):
        return "over 18"

    else:
        return 2022 - dob_year


if __name__ == '__main__':
    age = get_age(2011)
    print(f"Your age is : {age}")
