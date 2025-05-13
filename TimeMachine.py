from datetime import datetime, timedelta  

def time_machine(birthdate_str):  
    """
    Calculate interesting facts about someone's life:
    1. What day of the week their birthday will fall on in 2099
    2. How many seconds they've been alive
    3. The exact date when they will be 1 billion seconds old
    """
    try:
        # Convert birthdate from string to datetime
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")  
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    today = datetime.now()

    # 1. Birthday in 2099
    future_birthday = birthdate.replace(year=2099)
    weekday_2099 = future_birthday.strftime("%A")

    # 2. Seconds alive
    seconds_alive = int((today - birthdate).total_seconds())

    # 3. 1 Billion Seconds Day
    billion_seconds_day = birthdate + timedelta(seconds=1_000_000_000)

    print(f"🎂 In 2099, your birthday is a {weekday_2099}.")  
    print(f"⏳ You've been alive for {seconds_alive:,} seconds.")  
    print(f"🚀 1 BILLION seconds old on: {billion_seconds_day.strftime('%Y-%m-%d (%A)')}")  


if __name__ == "__main__":
    birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
    time_machine(birthdate_input) 
