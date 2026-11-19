
contact_book = {}

test_inputs = [
    'add\nName: Priya\nPhone: 555-0142',   # saves Priya
    'search Priya',                         # prints Priya: 555-0142
    'search priya',                         # not found for now, works after .lower()
    'search',                               # message, no crash
    'add',                                  # message, no crash
    'add Priya 555',                        # message, wrong format
    'delete Bob',                           # message, not found
    'delete',                               # message, no crash
    'foo',                                  # valid command message
    '',                                     # empty message
    'list',                                 # prints Priya
    'delete Priya',                         # deleted
    'list',                                 # prints nothing
]
while True:
    print('\n\n')
    line = input('> ')
    response =line.split()
    if not response:
         print( 'You didnt add anything! try again')
         continue
    #print(response)
    #example response for add: will be add name: dde phone: 34343
    if response[0] == 'add':
            if len(response) !=5:
                print("Enter valid input")
                continue
            else:
                name  = response[2].lower()
                phone = response[4]
                contact_book[name] = phone
                print("Name updated with", name)
                print(contact_book)
            
        
        

    elif response[0] == 'search':

        if len(response) <2:
             print("enter a valid search term")
             continue

        name = response[1].lower()
        if name in contact_book.keys():
            phone = contact_book[name]
            print(f'{name}: {phone}')
        else:
            print("name not found")
        
    elif response[0] == 'list':
        for k, v in contact_book.items():
            print(f'{k} : {v}')


    elif response[0] == 'delete':

            if len(response)< 2:
                 print("enter a valid term to delete")
                 continue
            
            name =response[1].lower()
            if name in contact_book.keys():
                del contact_book[name]
                print("deleted contact", name)

            else:
                 print("hey the name is not found")



    elif response[0] == 'quit':
        break
    else: 
         print("pls enter a valid command")



