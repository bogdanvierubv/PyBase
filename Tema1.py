from copy import replace
from itertools import count
from shlex import join

raw_logs= [ " ERROR | Voltage too LOW | code=E12 ", "info | System started successfully ",
           " WARNING | High temperature detected | code=W07 ", " ERROR | Communication timeout | code=E99 ",
           " info | System shutdown complete " ]

counts_errors= []
counts_warnings= []
counts_infos= []

error_codes = []
warning_codes = []

# 1 task
clean_string1 = raw_logs[0].strip().lower()
# print(clean_string1)
clean_string2 = raw_logs[1].strip().lower()
# print(clean_string2)
clean_string3 = raw_logs[2].strip().lower()
# print(clean_string3)
clean_string4 = raw_logs[3].strip().lower()
# print(clean_string4)
clean_string5 = raw_logs[4].strip().lower()
# print(clean_string5)

# varianta a doua

for i in range(len(raw_logs)):
    # print(raw_logs[i])
    raw_logs[i]=raw_logs[i].strip().lower()
    # print(raw_logs[i])


# 2 task
# print(clean_string1.split("|"))
# print(clean_string2.split("|"))
# print(clean_string3.split("|"))
# print(clean_string4.split("|"))
# print(clean_string5.split("|"))

# varianta a doua
    raw_logs[i]=raw_logs[i].split("|")
    print(raw_logs[i])

# # 3 task
# raw_logs_final=(clean_string1.lower().split("|") + clean_string2.lower().split("|") + clean_string3.lower().split("|")+ clean_string4.lower().split("|") +
#                 clean_string5.lower().split("|"))
# print(raw_logs_final)
#
# list=",".join(raw_logs_final)
# print(list)
#
# if "error" in list:
#     print("error found!")
# if list.startswith("error"):
#     print("error detected!")
#
# if "warning" in list:
#     print("warning found!")
#
# if "info" in list:
#     print("info found!")



#
# varianta a doua
    if raw_logs[i][0].startswith("error"):
        # print("error detected!")
        counts_errors.append(raw_logs[i][0].strip())
        error_code_list = raw_logs[i][2].split("=")[1].upper()
        error_codes.append(error_code_list)

    # if "error" in raw_logs[i][0]:
    #     print("error found!")
    if raw_logs[i][0].startswith("warning"):
        # print("warning detected!")
        counts_warnings.append(raw_logs[i][0].strip())
        warning_code_list = raw_logs[i][2].split("=")[1].upper()
        warning_codes.append(warning_code_list)

    if raw_logs[i][0].startswith("info"):
        # print("info detected!")
        counts_infos.append(raw_logs[i][0].strip())

        # print(counts_errors)
        # print(counts_warnings)
        # print(counts_infos)

# varianta 2
# # 4 task
# print("errors")
# a=list.count("error")
# print(a)
# print("warnings")
# b=list.count("warning")
# print(b)
# print("infos")
# c=list.count("info")
# print(c)
#



summary = f"""
OUTPUT
LOG SUMMARY
-----------

Errors      : {counts_errors.count('error')}
Warnings    : {counts_warnings.count('warning')}
Info        : {counts_infos.count('info')}


Error Codes : {error_codes}
Warning Codes: {warning_codes}
"""
print(summary)