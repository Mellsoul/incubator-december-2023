# YOUR SOLUTION
def check_eligibility_for_covid_vaccine(birth_year):
    current_year = 2024  # You can update this to the current year
    age = current_year - birth_year

    # Checking if the person is above 80 years old
    if int(age) <= 80:
        raise ValueError("Person is not eligible for COVID vaccine.")

    print("Person is eligible for COVID vaccine.")

# Example usage
try:
    birth_year = int(input("Enter the birth year: "))
    check_eligibility_for_covid_vaccine(birth_year)
except ValueError as e:
    print(f"Error: {e}")
