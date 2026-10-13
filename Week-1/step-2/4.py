#Define a variable that stores your school email address. Extract your student number from this email address.

email = "1153361@hr.nl"
student_number = email.split("@")[0].replace("student", "")
print(student_number)