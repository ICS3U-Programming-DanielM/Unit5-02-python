# !/user/bin/env.python3
# Created By: Daniel Momoh
# Date: Nov. 22, 2022
# This program asks the user for the base and
# and height, then determines the area of a triangle.
# this function calculates the area of a triangle


def calc_area(base_as_a_float, height_as_a_float):
    area = (base_as_a_float * height_as_a_float) / 2
    print("You entered {} as the base".format(base_as_a_float))
    print("You entered {} as the height".format(height_as_a_float))
    print("The area of the triangle is {:.2f}cm^2".format(area))


# checks for invalid input
def main():
    # displays the opening message
    print("Today we will calculate the area of a triangle!")
    print("")
    # gets base and height from the user
    base_as_a_string = input("Enter the base (cm): ")
    height_as_a_string = input("Enter the height (cm): ")
    print("")

    try:
        # converts input values to floats
        base_as_a_float_user = float(base_as_a_string)
        height_as_a_float_user = float(height_as_a_string)

        # makes sure input is greater than 0
        if base_as_a_float_user > 0 and height_as_a_float_user > 0:
            # calls function calculate the area
            calc_area(base_as_a_float_user, height_as_a_float_user)
        else:
            print("The base and height must be greater than 0.")
    except Exception:
        print("Only numbers can be accepted!")


if __name__ == "__main__":
    main()
