import subprocess as sp

def check():
    cmd = 'cat /proc/mdstat'
    res = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = res.communicate()
    output = output.decode('ascii')
    error = error.decode('ascii')

    if output:
        md_state = output.split('\n')
        md1_state = md_state[2]
        md0_state = md_state[6]
        if 'UU' in md1_state and 'UU' in md0_state:
            print(0)
        elif '_' in md1_state or '_' in md0_state:
            print(30)        
        elif 'F' in md1_state or 'F' in md0_state:
            print('40')
     
    if error:
        print('ERROR:', error)



if __name__  == '__main__':
    
    check()
