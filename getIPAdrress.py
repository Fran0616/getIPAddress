import socket

displayMessage = "The ip address is: "

print ("This program will display the IP address of a hostname\n")
print ("Input the hostname including it's the top level domain.\n Example: google.com\n")
hostname = input("Enter website: ") 
print(displayMessage + socket.gethostbyname(hostname))
