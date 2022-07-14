# PySync

This project is just a simple python script to keep folders sync.

## Requirements

* [Podman](https://podman.io/) Or [Docker](https://www.docker.com/get-started/).

## Security

Do not build your own image with your private ssh file inside it. The best way of dealing with this is to mount a volume with your .ssh keys.

```bash
podman run --mount type=bind,src=<YOUR .ssh DIR>,dst=/root/.ssh
```

## Quick Start

You can subsititue `podman` to `docker` if you are using docker.

```bash
podman run --mount type=bind,src=<YOUR .ssh DIR>,dst=/root/.ssh quay.io/guipguia/pysync:v0.0.1 <ARGS>
```


## Arguments

| Argument   | Shortcut | Description                                                                                           | Required           |
|------------|----------|-------------------------------------------------------------------------------------------------------|--------------------|
| --src      | -s       | Source folder to sync with destination folder.  (This is where your files are, soruce of truth).      | :heavy_check_mark: |
| --dst      | -d       | Destination folder, this is where the files  that are in src folder are going to.                     | :heavy_check_mark: |
| --remote   | -r       | Enable remote sync mode.                                                                              |         :x:        |
| --key      | -k       | Location to your private ssh-key.  (This key should be in authrozied_keys on the destination server.) |         :x:        |
| --username | -u       | Username for remote connection.                                                                       |         :x:        |
| --host     | -ip      | Ip/Hostname for the remote connection. eg(myserver.example.com)                                       |         :x:        |