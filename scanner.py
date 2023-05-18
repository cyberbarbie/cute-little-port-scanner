import sys, socket, os                                                                                  
from datetime import datetime as dt                                                                     
                                                                                                        
os.system("figlet Cute Little Port Scanner | lolcat")                                                   
                                                                                                        
# define target                                                                                         
if len(sys.argv) == 2:                                                                                  
    target = socket.gethostbyname(sys.argv[1]) # translate hostname to IPv4                             
else:                                                                                                   
    print("Invalid amount of arguments")                                                                
    print("Syntax: python3 scanner.py <ip>")                                                            
# Add a pretty banner                                                                                   
print("-" *50)                                                                                          
print("Scanning target: "+ target)                                                                      
print("Time started: "+ str(dt.now()))                                                                  
print("-" * 50)

try:                                                                                                    
    for port in range(0,443):                                                                           
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                           
        socket.setdefaulttimeout(1) #wait for 1s for a response then move on                            
        result = s.connect_ex((target,port)) #tuple to connect on target and port                       
        if result == 0:                                                                                 
            print(f"Port {port} is open")                                                               
        s.close()                                                                                       
                                                                                                        
except KeyboardInterrupt:                                                                               
    print("\nExiting Program")                                                                          
    sys.exit() #graceful exit                                                                           
                                                                                                        
except socket.gaierror: # when hostname cant resolve                                                    
    print("Hostname could not be resolved.")                                                            
    sys.exit()                                                                                          
                                                                                                        
except socket.error:                                                                                    
    print("Couldn't connect to the server")                                                             
    sys.exit() 
