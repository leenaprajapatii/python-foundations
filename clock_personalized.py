from datetime import datetime

def brain_clock(birthdate_str, sleep_per_day, eat_per_day, screen_per_day):
    """
    Estimates how much of your life has been spent based on YOUR actual routine:
    - Sleeping
    - Eating
    - Screen time
    Based on your birthdate and personal daily hours.
    """
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    except ValueError:
        print(" Invalid date format. Use YYYY-MM-DD.")
        return

    today = datetime.now()
    days_lived = (today - birthdate).days

    sleep_hours = days_lived * sleep_per_day
    eating_hours = days_lived * eat_per_day
    screen_hours = days_lived * screen_per_day

    def hours_to_days_hrs_mins(hours):
        days = int(hours // 24)
        hrs = int(hours % 24)
        return f"{days} days and {hrs} hours"

    print("\n Personal Life Clock Stats")
    print(f" You've been alive for {days_lived:,} days.")
    print(f" Sleeping: ~{hours_to_days_hrs_mins(sleep_hours)}")
    print(f" Eating: ~{hours_to_days_hrs_mins(eating_hours)}")
    print(f" Screen time: ~{hours_to_days_hrs_mins(screen_hours)}")
    total_used = sleep_hours + eating_hours + screen_hours
    percent_used = (total_used / (days_lived * 24)) * 100

    print(f"\n🌀 You’ve spent approximately {percent_used:.2f}% of your life doing these 3 things!")

if __name__ == "__main__":
    print("Welcome to Brain Clock Know how much of your life you've spent!")

    birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
    
    try:
        sleep_per_day = float(input(" How many hours do you sleep per day? (e.g. 7.5): "))
        eat_per_day = float(input(" How many hours do you spend eating per day? (e.g. 1.5): "))
        screen_per_day = float(input(" How many hours on screen/social media per day? (e.g. 4): "))
    except ValueError:
        print(" Please enter valid numbers for hours.")
    else:
        brain_clock(birthdate_input, sleep_per_day, eat_per_day, screen_per_day)
