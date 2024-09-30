c = get_config()

c.NotebookApp.token = ''

# Set a password (replace with your hashed password)
c.NotebookApp.password = 'argon2:$argon2id$v=19$m=10240,t=10,p=8$4NYZPGH/GQp2X/CrNC4QEQ$lA62KWzevsr+mlhqmDGn894M3llJUq3MoHR+Yui6fSo'