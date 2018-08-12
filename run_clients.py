from subprocess import Popen, CREATE_NEW_CONSOLE

for i in range(10):
    Popen('python client.py localhost 6666 r', creationflags=CREATE_NEW_CONSOLE)

# input('Enter to exit from Python script...')