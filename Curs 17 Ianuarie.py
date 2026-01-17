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


raw_logs = [
" ERROR | Voltage too LOW | code=E12 ",
" info | System started successfully ",
" WARNING | High temperature detected | code=W07 ",
" ERROR | Communication timeout | code=E99 ",
" info | System shutdown complete "
]

# print(raw_logs)

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

for i in range(len(raw_logs)):
    # raw_logs[i] -> ['error ', ' voltage too low ', ' code=e12']
    # raw_logs[i][0] -> `error`
    # raw_logs[i][0][0] -> `e`
    print(raw_logs[i])

    # print(raw_logs[i][0].startswith("error"))

    if raw_logs[i][0].startswith("error"):
        print("this is an error log")

    if raw_logs[i][0].startswith("info"):
        print("this is an info log")

    if raw_logs[i][0].startswith("warning"):
        print("this is an warning log")

