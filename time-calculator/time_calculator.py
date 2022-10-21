#code by Geovane Fernandes
def add_time(start, duration, day = ""):
    # Split the start time into hours, minutes and AM/PM
    start_time = start.split(" ")
    start_hours = int(start_time[0].split(":")[0])
    start_minutes = int(start_time[0].split(":")[1])
    start_period = start_time[1]
    
    # Split the duration into hours and minutes
    duration_hours = int(duration.split(":")[0])
    duration_minutes = int(duration.split(":")[1])
   
    # Calculate the new time
    new_hours = start_hours + duration_hours
    new_minutes = start_minutes + duration_minutes
    days = 0

    if new_minutes >= 60:
        new_hours += 1
        new_minutes -= 60
    
    if start_period == "PM":
        new_hours += 12
        days = new_hours // 24
    else:
        days = new_hours // 24
        
    new_hours = new_hours % 24

    if new_hours >= 12:
        new_period = "PM"
        if new_hours > 12:
            new_hours -= 12
    else:
        new_period = "AM"
        if new_hours == 0:
            new_hours = 12

    #check if day is given
    if day != "":
        dia = day.lower()
        week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        day_index = week.index(dia)
        new_day_index = (day_index + days) % 7
        new_day = week[new_day_index].capitalize()
        if days == 0:
            new_time = f"{new_hours}:{new_minutes:02d} {new_period}, {new_day}"
        elif days == 1:
            new_time = f"{new_hours}:{new_minutes:02d} {new_period}, {new_day} (next day)"
        else:
            new_time = f"{new_hours}:{new_minutes:02d} {new_period}, {new_day} ({days} days later)"
    else:
     
        if days == 0:
            new_time = f"{new_hours}:{new_minutes:02d} {new_period}"
        elif days == 1:
            new_time = f"{new_hours}:{new_minutes:02d} {new_period} (next day)"
        else:
            new_time = f"{new_hours}:{new_minutes:02d} {new_period} ({days} days later)"
    return new_time