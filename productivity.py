


def Add_Action():
    Action_List = []
    Action = 'Start'
    while Action != "0" and Action != '':
         Action_List.append(Action)
         Action = input('Задача: ')
    print(Action_List)



def cmd_help():
    print('Commands')
    print('-- help' , '-- action_restart', '-- action_add', sep="\n")


def action_add(act):
    print(act, '-')

cmd = ' '
while cmd != '': #Временная коммандная строка
    cmd = input(': ')
    if cmd == 'help':
        cmd_help()
    elif cmd == 'action_restart':
        Add_Action()
    elif cmd == 'action_add':
        arg = input('Аргумент: ')
        action_add(arg)


