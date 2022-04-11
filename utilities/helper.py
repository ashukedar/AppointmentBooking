from datetime import datetime

def setDateTime(inputText):
    while True:
        try:
            date_time_str = input(inputText)+":00.000000" #2018-06-29 08:15:27.243860
            return datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
        except:
            print("Invalid input. Expected input: YYYY-MM-DD HH:MM")

def setTime(inputText):
    while True:
        try:
            time_str = input(inputText) #2018-06-29 08:15:27.243860
            arr = time_str.split(':')
            if len(time_str) != 5 or time_str[2] != ":" or int(arr[0]) > 24 or int(arr[0]) < 0 or int(arr[1]) > 24 or int(arr[1]) < 0:
                raise Exception()
            return "CAST('" + time_str + ":00' AS TIME )"
        except:
            print("Invalid input. Expected input: HH:MM")
