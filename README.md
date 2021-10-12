### Vagrant
```
For creating an isoloated development server
On CMD ->
        1. vagrant init ubuntu/bionic64 (type of server)
        2. vagrant up (Run a new VM)
        3. vagrant ssh (Connecting to VM)
```

### Virtual Environment
```
For creating a Local Environment(not System wide) specific to this Project
On CMD ->
        1. cd /vagrant 
        2. python -m venv ~/env (creating env file to vagrant 
                                home directory, so, that if we
                                delete thi vagrant file, we can 
                                start with a new V.environment)
        3. source ~/env/bin/activate
```