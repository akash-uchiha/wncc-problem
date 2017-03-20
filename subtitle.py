

#create list of all lines
lines=file.readlines()

#remove \n items from list lines
newlines=[]
for line in lines:
    if line!='\n':
        newlines.append(line)
        
clock=time.clock()       
counter=1

print "<start>"
for x in range(0,len(newlines)) :
    
    if  newlines[x]==str(counter)+'\n':
        tim=newlines[x+1]
        times=tim.split(' --> ')
        time1=times[0].split(':')
        time2=times[1].split(':')
        t1=caltime(time1)
        t2=caltime(time2)
        delay=t2-t1
        
        while(t1>time.clock()):
            continue
        i=x+2    
        while newlines[i]!=str(counter+1)+'\n':    
            print newlines[i]
            i=i+1
        time.sleep(delay)
        os.system('cls')
        counter=counter+1
        
    
# end of code
