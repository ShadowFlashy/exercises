# Write your code here
def format_time(hours, minutes, seconds):
    return f"{str(hours).rjust(2, '0')}:{str(minutes).rjust(2, '0')}:{str(seconds).rjust(2, '0')}" 