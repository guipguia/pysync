import argparse, time, os
from subprocess import Popen, PIPE

def test_args():
    if args.remote:
        set_remote_command()
    else:
        set_local_command()

def set_local_command():
    global command
    command = ['rsync', '-a', args.src, args.dst]

def set_remote_command():
    global command
    command = ['rsync', '-a', args.src, '%s@%s:%s' % (args.username, args.host, args.dst)]


def run():
    while True:
        process = Popen(command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        if stderr != b'':
            raise Exception(stderr)
        time.sleep(30)

def main():
    # start_folder_observer()
    print('Start to sync local %s with %s...' % (args.src, args.dst))
    run()
    


if __name__ == '__main__':
    global args

    parser = argparse.ArgumentParser(description='PySync arguments.')
    parser.add_argument('--src', '-s', help='Source folder to sync with destination folder. (This is where your files are, soruce of truth).', required=True)
    parser.add_argument('--dst', '-d', help='Destination folder, this is where the files that are in src folder are going to.', required=True)
    parser.add_argument('--remote', '-r', action=argparse.BooleanOptionalAction, help='Enable remote sync mode.', required=False)
    parser.add_argument('--key', '-k', help='Location to your private ssh-key. (This key should be in authrozied_keys on the destination server.)', required=False)
    parser.add_argument('--username', '-u', help='Username for remote connection.')
    parser.add_argument('--host', '--ip', '-c', help='Ip/Hostname for the remote connection. eg(myserver.example.com)')

    args = parser.parse_args()
    
    test_args()
    main()