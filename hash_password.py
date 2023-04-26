import hashlib

pw = input("Enter your UVM NetID PASSWORD: ")
h = hashlib.new("md4", pw.encode("utf-16le")).hexdigest()

print("Copy/paste the following into the wpa_supplicant.conf file: \n")
print("password=hash:" + h + "\n")
