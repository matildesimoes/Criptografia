from pwn import *

config_alice = open("config_alice", "r")
config_bob = open("config_bob", "r")

hostAlice = config_bob.readline()[:-1]
portAlice = int(config_bob.readline())

hostBob = config_alice.readline()[:-1]
portBob = int(config_alice.readline())

config_alice.close()
config_bob.close()

hostMitM = "localhost"


rAlice = remote(hostAlice, portAlice)
lAlice = listen(5077)
lAlice.wait_for_connection()

#lBob = listen(5078)
#lBob.wait_for_connection()
#rBob = remote(hostBob, portBob)

lAlice.close()
rAlice.close()
