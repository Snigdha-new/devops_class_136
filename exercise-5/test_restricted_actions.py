import docker

client = docker.from_env()

print("Starting container with AppArmor profile...")
container = client.containers.run(
    "flask-apparmor",
    ports={'5000/tcp': 5000},
    security_opt=["apparmor=my-apparmor-profile"],
    detach=True
)

print(f"Container started: {container.short_id}\n")

print("1. Testing restricted file read (/etc/passwd via Python)...")
exit_code, output = container.exec_run("python -c \"open('/etc/passwd').read()\"")
print(f"   Exit Code: {exit_code}")
print(f"   Output: {output.decode().strip()}\n")

print("2. Testing restricted binary execution (/bin/bash)...")
exit_code, output = container.exec_run("/bin/bash")
print(f"   Exit Code: {exit_code}")
print(f"   Output: {output.decode().strip()}\n")

print("Stopping container...")
container.stop()
container.remove()
