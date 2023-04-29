def add_time(start_time, duration, start_day=None):
    # Parse the start time
    start_time_parts = start_time.split()
    start_time_hour, start_time_minute = map(int, start_time_parts[0].split(':'))
    start_time_ampm = start_time_parts[1]

    # Parse the duration
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Convert the start time to 24-hour clock format
    if start_time_ampm == 'PM' and start_time_hour != 12:
        start_time_hour += 12
    elif start_time_ampm == 'AM' and start_time_hour == 12:
        start_time_hour = 0

    # Add the duration
    end_time_hour = start_time_hour + duration_hours
    end_time_minute = start_time_minute + duration_minutes
    if end_time_minute >= 60:
        end_time_hour += 1
        end_time_minute -= 60

    days_elapsed = 0
    while end_time_hour >= 24:
        end_time_hour -= 24
        days_elapsed += 1

    if end_time_hour >= 12:
        end_time_ampm = 'PM'
        if end_time_hour > 12:
            end_time_hour -= 12
    else:
        end_time_ampm = 'AM'
        if end_time_hour == 0:
            end_time_hour = 12

    # Format the end time as a string
    end_time = '{:d}:{:02d} {}'.format(end_time_hour, end_time_minute, end_time_ampm)

    # Calculate the final day of the week
    if start_day is not None:
        start_day = start_day.lower()
        weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        start_day_index = weekdays.index(start_day)
        end_day_index = (start_day_index + days_elapsed) % 7
        end_day = weekdays[end_day_index]
        end_time += ', ' + end_day.capitalize()

    # Add the number of days elapsed to the output
    if days_elapsed == 1:
        end_time += ' (next day)'
    elif days_elapsed > 1:
        end_time += ' ({} days later)'.format(days_elapsed)

    return end_time