# Tema
# lista1 = [1, 3, 4, 100, 300]
# index     0  1  2   3    4

# exemplul 1.Clean each log line

# var1=" EU sunt  SLIM SHADY un sir de caratere    e   cu cateva spatii  "
# var2 = var1.strip()
# var2 = var2.lower()
# # sau var2 = var1.strip().lower()
# print(var1)
# print(var2)

# lista1 = []
# print(lista1)
# lista1.append(30)
# lista1.append(100)
# lista1.append(350)
# lista1.append(30)
# print(lista1)
#
# print(lista1.count(30))


raw_logs = [
" ERROR | Voltage too LOW | code=E12 ",
" info | System started successfully ",
" WARNING | High temperature detected | code=W07 ",
" ERROR | Communication timeout | code=E99 ",
" info | System shutdown complete "
]

# for elem in raw_logs:
#     print(elem)
# print(raw_logs)

error_codes_list = []
warning_codes_list = []

# 1-creem indezi pentru lista noastra
for i in range(len(raw_logs)):
    # for i -> creaza variabila i
    # len(raw_logs) -> 5
    # range (len(raw_logs)) -> range(5) -> [0, 1,2 ,3 ,4]
    # i  -> index
    # print(i)
    raw_logs[i] = raw_logs[i].strip().lower()
    # print(raw_logs[i])

# 2.Split log fields
    raw_logs[i] = raw_logs[i].split("|")
    # print(raw_logs[i])

# 3.Identify log level

print("Starting Indentification:")

log_type_counts = []

for i in range(len(raw_logs)):
    # raw_logs[i] -> ['error ', ' voltage too low ', ' code=e12']
    # raw_logs[i][0] -> `error`
    # raw_logs[i][0][0] -> `e`
    # print(raw_logs[i])

    # print(raw_logs[i][0].startswith("error"))

    if raw_logs[i][0].startswith("error"):
        # print("this is an error log")
        log_type_counts.append(raw_logs[i][0].strip())
        extracted_error_code = raw_logs[i][2].split("=")[1].upper()
        error_codes_list.append(extracted_error_code)

    if raw_logs[i][0].startswith("info"):
        # print("this is an info log")
        log_type_counts.append(raw_logs[i][0].strip())

    if raw_logs[i][0].startswith("warning"):
        # print("this is an warning log")
        log_type_counts.append(raw_logs[i][0].strip())
        extracted_warning_code = raw_logs[i][2].split("=")[1].upper()
        warning_codes_list.append(extracted_warning_code)

        # procesam eroarea din logul cu erori:
        print(raw_logs[i][2])
        # raw_logs[i][2] -> ` code=e12`
        # raw_logs[i][2].split("=") -> [`code`, `e12`]











        print(log_type_counts)

error_count = log_type_counts.count("error")
warning_count = log_type_counts.count("warning")
info_count = log_type_counts.count("info")

output_string = f"""
OUTPUT
LOG SUMMARY
-----------

Errors      : {error_count}
Warnings    : {warning_count}
Info        : {info_count}


Error Codes : {error_codes_list}
Warning Codes: {warning_codes_list}
"""
print(output_string)

# print("-----F-Strings-----")

# string2 = "Horatiu"
# var3 = f"[{string2} are mere]"
# print(var3)



# print("PUTPUT")
# print("LOG SUMMARY")
# print("----------")
# print("Errors  :")
# print(log_type_counts.count("error"))
# print("Warnings  :")
# print(log_type_counts.count("warning"))
# print("Info  :")
# print(log_type_counts.count("info"))