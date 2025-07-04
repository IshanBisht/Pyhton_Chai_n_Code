import hello
#from hello import chai    #importing a method from one file to another

from importlib import reload
reload(hello)

print(hello.c3)

#chai("ginger tea")

#from importlib import reload      #if you make any changes in the hello file and try to access any method from the initial file you 
#reload(hello)                       have to reload the file using this.

#print(hello.c1)