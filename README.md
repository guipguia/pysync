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


## Variables

| Env Var              | Description                                                                                      | Loca/Remote |
|----------------------|--------------------------------------------------------------------------------------------------|-------------|
| SYNC_SOURCE_DIR      | Source folder to sync with destination folder.  (This is where your files are, soruce of truth). | Both        |
| SYNC_DESTINATION_DIR | Destination folder, this is where the files  that are in src folder are going to.                | Both        |
| SYNC_REMOTE          | Enable remote sync mode.                                                                         | Remote      |
| SYNC_USERNAME        | Username for remote connection.                                                                  | Remote      |
| SYNC_HOST            | Ip/Hostname for the remote connection. eg(myserver.example.com)                                  | Remote      |