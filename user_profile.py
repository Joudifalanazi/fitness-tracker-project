def create_user_profile(name, age, weight, height, weekly_goal_minutes, weekly_goal_calories):
    """
    Creates a user profile using a dictionary.
    """
    profile = {
        "name": name,
        "age": age,
        "weight": weight,
        "height": height,
        "weekly_goal_minutes": weekly_goal_minutes,
        "weekly_goal_calories": weekly_goal_calories
    }
    return profile


def calculate_bmi(weight, height):
    """
    Calculates BMI using weight in kg and height in cm.
    Formula: BMI = weight / height_in_meters^2
    """
    height_in_meters = height / 100

    if height_in_meters == 0:
        return 0

    bmi = weight / (height_in_meters ** 2)
    return bmi


def display_user_profile(profile):
    """
    Displays user profile details.
    """
    print("-----------------------------")
    print(f"Name: {profile['name']}")
    print(f"Age: {profile['age']}")
    print(f"Weight: {profile['weight']} kg")
    print(f"Height: {profile['height']} cm")
    print(f"Weekly Goal: {profile['weekly_goal_minutes']} minutes")
    print(f"Weekly Calorie Goal: {profile['weekly_goal_calories']} calories")
    print("-----------------------------")
