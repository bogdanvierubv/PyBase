from copy import replace
from itertools import count

raw_logs= [ " ERROR | Voltage too LOW | code=E12 ", "info | System started successfully ",
           " WARNING | High temperature detected | code=W07 ", " ERROR | Communication timeout | code=E99 ",
           " info | System shutdown complete " ]
# 1 task
clean_string1 = raw_logs[0].strip()
# print(clean_string1.lower())
clean_string2 = raw_logs[1].strip()
# print(clean_string2.lower())
clean_string3 = raw_logs[2].strip()
# print(clean_string3.lower())
clean_string4 = raw_logs[3].strip()
# print(clean_string4.lower())
clean_string5 = raw_logs[4].strip()
# print(clean_string5.lower())

# 2 task
# print(clean_string1.lower().split("|"))
# print(clean_string2.lower().split("|"))
# print(clean_string3.lower().split("|"))
# print(clean_string4.lower().split("|"))
# print(clean_string5.lower().split("|"))

# 3 task
raw_logs_final=(clean_string1.lower().split("|") + clean_string2.lower().split("|") + clean_string3.lower().split("|")+ clean_string4.lower().split("|") +
                clean_string5.lower().split("|"))
print(raw_logs_final)

list="".join(raw_logs_final)
print(list)

if "error" in list:
    print("error found!")
if list.startswith("error"):
    print("error detected!")

if "warning" in list:
    print("warning found!")

if "info" in list:
    print("info found!")

# 4 task
print("errors")
a=list.count("error")
print(a)
print("warnings")
b=list.count("warning")
print(b)
print("infos")
c=list.count("info")
print(c)

# 5 task



