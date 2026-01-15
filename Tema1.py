from copy import replace

raw_logs= [ " ERROR | Voltage too LOW | code=E12 ", "info | System started successfully ",
           " WARNING | High temperature detected | code=W07 ", " ERROR | Communication timeout | code=E99 ",
           " info | System shutdown complete " ]

clean_string1 = raw_logs[0].strip()
print(clean_string1.lower())
clean_string2 = raw_logs[1].strip()
print(clean_string2.lower())
clean_string3 = raw_logs[2].strip()
print(clean_string3.lower())
clean_string4 = raw_logs[3].strip()
print(clean_string4.lower())
clean_string5 = raw_logs[4].strip()
print(clean_string5.lower())




