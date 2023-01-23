from borders import frame

menu_list = [
    "\t\t\t\tTask Overview",
    "123456789@123456789@123456789@123456789@123456789@",
    "123456789@123456789@123456789@123456789@123456789@123456789@",
    "AAA",
    "123456789@123456789@123456789@123456789@123456789@123456789@123456789@123456789@123456789@123456789@",
    "BBB",
    "Total number of users ··············· :      9",
    "Tasks overdue ······················· :    100.00%",
    "Date assignement:\t0123456789",
    ]

frame(menu_list, colour="pink", spacing=1)

print(frame.__doc__)
