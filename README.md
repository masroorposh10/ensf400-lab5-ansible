### Assignment - 2: A fully dockerized environment to play with ansible.

- Name: Masroor Posh
- UCID: 30156171

## Usage:

# Run this for the initial startup:
- `docker compose up -d`
- `export ANSIBLE_CONFIG=$(pwd)/ansible.cfg`
- `ansible all:localhost --list-hosts`
- `ansible all:localhost -m ping`

# Run this to execute:
- `ansible-playbook hello.yml`
# To test:
- `service nginx status`
- `ls -l /etc/nginx/sites-enabled/`
- `curl http://0.0.0.0`

# To test the python api:
- `python load_inventory.py`
- `python run_playbook.py`