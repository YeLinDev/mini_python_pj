clients = []

new_client = ""
while new_client != "quit":
    new_client = input("What is the name of the client?")
    clients.append(new_client)

for client in clients:
    print(client)
