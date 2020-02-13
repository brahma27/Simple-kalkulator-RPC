from xmlrpc.server import SimpleXMLRPCServer


with SimpleXMLRPCServer(("192.168.1.5", 8008))as server:
    server.register_introspection_functions()

    print('mulai menghubungkan port 8008...')

    def tambah(x,y):
        return x+y
    server.register_function(tambah, "tambah")

    def kurang(x,y):
        return x-y
    server.register_function(kurang, "kurang")

    def kali(x,y):
        return x*y
    server.register_function(kali, "kali")

    def bagi(x,y):
        return x//y
    server.register_function(bagi, "bagi")

    def pangkat(x,y):
        return x**y
    server.register_function(pangkat, "pangkat")
    def mod(x,y):
        return x%y
    server.register_function(mod, "mod")


    server.serve_forever()