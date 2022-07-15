import argparse, time, os
from subprocess import Popen, PIPE

def get_env(name: str):
    return os.getenv(name, default=None)


def get_required_env(var: str):
    variable = get_env(var)
    if variable == None:
        raise Exception('Couldn\'t find %s env.' % var)

def set_local_command():
    global command

    src = get_required_env('SYNC_SOURCE_DIR')
    dst = get_required_env('SYNC_DESTINATION_DIR')

    command = ['rsync', '-a', src, dst]

def set_remote_command():
    global command

    src = get_required_env('SYNC_SOURCE_DIR')
    dst = get_required_env('SYNC_DESTINATION_DIR')
    username = get_required_env('SYNC_USERNAME')
    host = get_required_env('SYNC_HOST')

    command = ['rsync', '-a', src, '%s@%s:%s' % (username, host, dst)]

def run():
    while True:
        process = Popen(command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        if stderr != b'':
            raise Exception(stderr)
        time.sleep(30)

def main():
    # start_folder_observer()
    src = get_required_env('SYNC_SOURCE_DIR')
    dst = get_required_env('SYNC_DESTINATION_DIR')
    print('Start to sync local %s with %s...' % (src, dst))
    run()
    


if __name__ == '__main__':
    remote = get_env('SYNC_REMOTE')
    
    if remote:
        print('remote...')
        set_remote_command()
    else:
        print('not remote')
        set_local_command()
    
    main()