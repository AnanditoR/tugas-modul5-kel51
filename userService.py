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
        get_history = self.checkhistory()
        get_data = self.checkCredentials()
        if get_data:
            print("\nWelcome ",get_data['role'])
            print("Logged in as user email: ",get_data['email'], "\n")
            print(get_data ['email'],"Meminjam buku :", get_history['peminjaman_buku'],"\nPada tanggal", get_history['tanggal_pinjam'])
        else:
            print("\nInvalid Login!\n")

    def checkCredentials(self):
        for a in self.data:
            if a == self.email:
                get_data_user = self.data[a]
                if self.password == get_data_user['password']:
                    return get_data_user
                else:
                    return False

    def checkhistory(self):
        for b in self.history:
            if b == self.email:
                get_history_buku = {}

                get_history_buku.update(tanggal_pinjam = self.history[b]['tanggal_pinjam'])

                str_buku = '\n'
                
                for c in self.history[b]['peminjaman_buku']:
                    str_buku += c + "\n"
                
                get_history_buku.update(peminjaman_buku = str_buku)
                
                return get_history_buku