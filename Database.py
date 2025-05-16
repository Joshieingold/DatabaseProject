def Run():
    print("Please write the database you would like to connect to.")
    db = ConnectPath(input())
    if db is False:
        print("Aborting Connection")
        return

    while True:
        print("Awaiting next command")
        command = input().strip()

        if command == "quit":
            print("Closing Connection")
            break
        elif command.startswith("create collection"):
            collection_name = command.replace("create collection", "").strip()
            CreateCollection(db, collection_name)
        elif command == "list collections":
            ListConnections(db)
        else:
            print("Unknown command")


def ConnectPath(database_string):
    try:
        open(database_string, "a").close()  # Ensure file exists
        print(f'Successfully connected to {database_string}')
        return database_string
    except Exception as e:
        print("Connection Failed:", e)
        return False


def CreateCollection(db_path, collection_name):
    with open(db_path, "a") as f:
        f.write(collection_name + "\n")
    print(f'Collection "{collection_name}" Created')


def ListConnections(db_path):
    with open(db_path, "r") as f:
        collections = f.read().splitlines()
        if not collections:
            print("No collections found.")
        else:
            print("Collections:")
            for i in collections:
                print("-", i)


Run()
