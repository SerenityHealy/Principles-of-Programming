current_time = int(input())

wait_time = int(input())

alarm_time = (current_time + wait_time) % 24

print(f"The alarm will go off at: {alarm_time}")
