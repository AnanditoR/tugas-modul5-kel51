class userService(object):

    def __init__(self, email, password):
       self.email = email
       self.password = password
       self.data = {
            "ditokelompok51@gmail.com" : { 
                "email"     : "ditokelompok51@gmail.com",
                "password"  : "12345", 
                "role"      : "superadmin",
            },
            "azzamkelompok51@gmail.com" : {
                "email"     : "azzamkelompok51@gmail.com",
                "password"  : "12345",
                "role"      : "user",
            }
       }
       self.history = {
           "ditokelompok51@gmail.com" : {
                "peminjaman_buku"     : {'Fisika Dasar', 'Dasar Komputer dan Pemrograman'},
                "tanggal_pinjam"   : "25 April 2020"
           },
           "azzamkelompok51@gmail.com" : {
                "peminjaman_buku"     : {'Kalkulus', 'Dasar Komputer dan Pemrograman', 'Konsep Jaringan Komputer'},
                "tanggal_pinjam"   : "25 April 2020",
           }
       }
    def login(self):
        get_history = self.history
        get_data = self.checkCredentials()
        if get_data:
            print("\nWelcome ",get_data['role'])
            print("Logged in as user email: ",get_data['email'])
            print("\n",get_data['email'], "Meminjam buku :")
        else:
            print("\nInvalid Login!\n")

    def checkCredentials(self):
        for value in self.data:
            if value == self.email:
                get_data_user = self.data[value]
                if self.password == get_data_user['password']:
                    return get_data_user
                else:
                    return False


