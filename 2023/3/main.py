# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.

def bordered(list):
    map=[]
    blank=''
    for x in range(len(list[0])):
        blank=blank+'.'
    map.append(blank)
    for line in list:
        map.append(line)
    map.append(blank)
    for x in range(len(map)):
        map[x]='.'+map[x]+'.'
    return(map)

def check(map,y):
    coord=[-1,0,1]
    for x in range(1,len(map[y])):
        partno=''
        surround=''
        if map[y][x].isdigit() and not map[y][x-1].isdigit():
            i=x
            ended=False
            while not ended:
                partno=partno+map[y][i]
                tempgearlist=[]
                for w in coord:
                    for z in coord:
                        if map[y+w][i+z].isdigit()==False:
                            surround=surround+(map[y+w][i+z])
                        if map[y+w][i+z]=='*':

                            gearname=str(map[y+w])+'x'+str(map[i+z])
                            #create or add to temp list of gears connected to this number
                            if gearname in tempgearlist:
                                pass
                            else:
                                tempgearlist.append(gearname)


                if not map[y][i+1].isdigit():
                    ended=True
                i=i+1
            print('adding'+partno)
            partnos.append(partno)
            print('adding'+surround)
            surrounds.append(surround)
            #add partno to all gears in temp list





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #filename='test'
    filename='input'
    with open(filename) as file:
        list = [line.rstrip() for line in file]
    #print(list)
    gears={}
    map=bordered(list)
    #print(map)
    x=1
    y=1
    partnosum=0
    partnos=[]
    surrounds=[]
    while y<len(map)-1:
        print(map[y])
        check(map,y)
        y=y+1
    print(partnos)
    print(surrounds)
    for x in range (len(partnos)):
        add=False
        for y in range (len(surrounds[x])):
            if (surrounds[x][y]=='.')==False:
                add=True
        if add:
            partnosum=partnosum+int(partnos[x])
    print(partnosum)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
