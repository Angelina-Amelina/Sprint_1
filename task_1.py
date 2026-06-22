count_time = 0
string_of_time = '1h 45m,360s,25m,30m 120s,2h 60s'

lst = string_of_time.split(',')

for i in lst:
    lst_time = i.split()

    for n in lst_time:
        if 'h' in n:
            hours = n.replace('h','')
            count_time += int(hours) * 60
        elif 'm' in n:
            minutes = n.replace('m','')
            count_time += int(minutes)
        elif 's' in n:
            seconds = n.replace('s','')
            count_time += int(seconds) // 60

print(count_time)
