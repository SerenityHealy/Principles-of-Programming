room_numbers = {
    "CSC101": 3004,
    "CSC102": 4501,
    "CSC103": 6755,
    "NET110": 1244,
    "COM241": 1411
}

instructor_names = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}
print("Welcome, enter your course number to get the room number, time and instructor for your course.")
course_number = input("Please enter your course number:")

if course_number in room_numbers:
    room = room_numbers[course_number]
    instructor = instructor_names[course_number]
    meeting_time = meeting_times[course_number]

    print(f"Course Number: {course_number}")
    print(f"Room Number: {room}")
    print(f"Instructor: {instructor}")
    print(f"Meeting Time: {meeting_time}")
else:
    print("Course number not found.")

