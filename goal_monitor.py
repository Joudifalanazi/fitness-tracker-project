from datetime import datetime
def check_weekly_goal(workout_count, goal):
    """
    Checks if the weekly workout goal was achieved.
    """

    if workout_count >= goal:
        return "Goal achieved!"

    return "Goal not reached yet."
def calculate_streak(workouts):
    """
    Calculates consecutive workout days.
    """

    if len(workouts) == 0:
        return 0

    dates = []

    for workout in workouts:

        workout_date = datetime.strptime(
            workout["date"],
            "%Y-%m-%d"
        ).date()

        dates.append(workout_date)

    dates.sort()

    streak = 1

    for i in range(1, len(dates)):

        difference = (
            dates[i] - dates[i - 1]
        ).days

        if difference == 1:
            streak += 1

    return streak

def generate_achievement(total_workouts):
    """
    Generates achievement messages.
    """

    if total_workouts >= 50:
        return "Fitness Master!"

    elif total_workouts >= 20:
        return "Great Progress!"

    elif total_workouts >= 10:
        return "Nice Consistency!"

    return "Keep Going!"

def motivation_message(streak):
    """
    Generates motivational messages based on streak.
    """

    if streak >= 7:
        return "Amazing dedication!"

    elif streak >= 3:
        return "You're building consistency!"

    return "Keep pushing!"

if __name__ == "__main__":

    workouts = [

        {"date": "2026-05-01"},

        {"date": "2026-05-11"},

        {"date": "2026-05-12"}
    ]

    print(check_weekly_goal(25, 20))

    streak = calculate_streak(workouts)

    print(f"Workout Streak: {streak} days")

    print(generate_achievement(25))

    print(motivation_message(streak))