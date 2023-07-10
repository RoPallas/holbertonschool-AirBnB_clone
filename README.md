

# AirBnB Clone - The console



![image](https://github.com/RoPallas/holbertonschool-AirBnB_clone/blob/main/assets/console.png)

The console will be a tool to validate the storage engine
## Description
This is the first part of the project that simulates an airbnb application. 
The first piece is to manipulate a powerful storage system.
This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”

## Prerequisited
Python3.4+ has to be installed if you desire to use the console:

    sudo apt-get install python3

## Instalation and run
To access:

    git clone https://github.com/RoPallas/holbertonschool-AirBnB_clone.git; cd holbertonschool-AirBnB_clone

To run:

    ./console.py
## Use
### Available commands

- help ([command])
- create [ClassName]
- show [ClassName] [id]
- all ([ClassName])
- update [ClassName] [id] [attribute] [value]
- destroy [ClassName] [id]
- quit or EOF

### Command explanation
-help:
Show the available commands and their explanations

Ex: $ help create
- create:	
Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.

Ex: $ create BaseModel
- show:	
Prints the string representation of an instance based on the class name and id.

Ex: $ show BaseModel 1234-1234-1234
- all:	
Prints all string representation of all instances based or not on the class name.

Ex: $ all BaseModel
- update:	
Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).

Ex: $ update BaseModel 1234-1234-1234 name Betty
- destroy:
Deletes an instance based on the class name and id (save the change into the JSON file). 

Ex: $ destroy BaseModel 1234-1234-1234.
- quit or EOF:
To exit the program



## Class
### Advailable Class

- BaseModel
- User
- Amenity
- City
- Place
- State
- Review
- FileStorage

## Usage/Examples
### Non nteractive mode

Ex:

    $ echo "help" | ./console.py
    (hbnb) 
    Documented commands (type help <topic>):
    ========================================
    EOF  all  count  create  destroy  help  quit  show  update

    (hbnb) 
    $

### Interactive mode

Ex:

    $ ./console.py
    (hbnb) create User
    1e32232d-5a63-4d92-8092-ac3240b29f46
    (hbnb)
    (hbnb) show User 1e32232d-5a63-4d92-8092-ac3240b29f46
    [User] (1e32232d-5a63-4d92-8092-ac3240b29f46) {'id': '1e32232d-5a63-4d92-8092-a
    c3240b29f46', 'created_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828), 
    'updated_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828)}
    (hbnb) 
    (hbnb) User.show(1e32232d-5a63-4d92-8092-ac3240b29f46)
    [User] (1e32232d-5a63-4d92-8092-ac3240b29f46) {'id': '1e32232d-5a63-4d92-8092-a
    c3240b29f46', 'created_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828), 
    'updated_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828)}
    (hbnb) quit
    $


## Authors

- [@RoPallas](https://github.com/RoPallas)
- [@MrKindness235](https://github.com/MrKindness235)

