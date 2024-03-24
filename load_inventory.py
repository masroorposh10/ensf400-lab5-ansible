import ansible_runner

result = ansible_runner.interface.run_command("ansible", [
    "all:localhost", "-i",
    "hosts.yml", "-m", "setup", "-a",
    "filter=ansible_default_ipv4"
])

ansible_runner.interface.run_command("ansible", [
    "all:localhost", "--list-hosts"
])
# Ping hosts
ansible_runner.interface.run_command("ansible", [
    "-i", "./hosts.yml",
    "--private-key", "./secrets/id_rsa",
    "all:localhost",
    "-m", "ping"
])
