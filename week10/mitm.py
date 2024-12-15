from pwn import *

config_alice = open("config_alice", "r")
config_bob = open("config_bob", "r")

hostAlice = config_bob.readline()[:-1]
portAlice = int(config_bob.readline())

hostBob = config_alice.readline()[:-1]
portBob = int(config_alice.readline())

config_alice.close()
config_bob.close()

rAlice = remote(hostAlice, portAlice)
lAlice = listen(portBob)
lAlice.wait_for_connection()

lBob = listen(portAlice)
lBob.wait_for_connection()
rBob = remote(hostBob, portBob)

g = 2
p = 7853799659

gy = int.from_bytes(lBob.recvline()[:-1], "little")
print("Received GY from Bob:", gy)

c = random.randint(1, p)
gc = pow(g, c, p)

print("Sending GC to Alice:", gc)
rAlice.sendline(gc.to_bytes(8, "little"))

gx = int.from_bytes(lAlice.recvline()[:-1], "little")
print("Received GX from Alice:", gx)

d = random.randint(1, p)
gd = pow(g, d, p)

print("Sending GD to Bob:", gd)
rBob.sendline(gd.to_bytes(8, "little"))

print("Shared secret with Alice:", pow(gx, c, p))
print("Shared secret with Bob:", pow(gy, d, p))

lAlice.close()
rAlice.close()
