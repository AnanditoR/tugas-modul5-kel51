from userService import userService



print("Tugas Modul 5 Kelompok 51\n")
email = input("Email: ")
password = input("Password: ")
get_class = userService(email,password)
get_class.login()

