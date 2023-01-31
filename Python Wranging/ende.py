import sys
import base64
from cryptography.fernet import Fernet

usage_msg = "Usage: " + sys.argv[0] + " (-e/-d) [file]"
help_msg = usage_msg + "\n" + \
           "  To decrypt a file named 'pole.txt', do: " + \
           "'$ python " + sys.argv[0] + " -d pole.txt'\n" + "<password>" \
           "  To encrypt a file named 'pole.txt', do: "  \
           "'$ python " + sys.argv[0] + " -e pole.txt'\n" + "<password>"

# Handle error invalid arguments from users.

if len(sys.argv) < 2 or len(sys.argv) > 4:
    print("Invalid arguments. Please try python ende.py -h to see further instruction. Please try again.")
    sys.exit(1)

# Encode to base64
if sys.argv[1] == "-e":
    if len(sys.argv) < 4:
        sim_sala_bim = input("Please enter the password:")
    else:
        sim_sala_bim = sys.argv[3]

    ssb_b64 = base64.b64encode(sim_sala_bim.encode())
    c = Fernet(ssb_b64)

    with open(sys.argv[2], "rb") as f:
        data = f.read()
        data_c = c.encrypt(data)
        sys.stdout.write(data_c.decode())

# Decode from base64
elif sys.argv[1] == "-d":
    if len(sys.argv) < 4:
        sim_sala_bim = input("Please enter the password:")
    else:
        sim_sala_bim = sys.argv[3]

    ssb_b64 = base64.b64encode(sim_sala_bim.encode())
    c = Fernet(ssb_b64)

    with open(sys.argv[2], "r") as f:
        data = f.read()
        data_c = c.decrypt(data.encode())
        sys.stdout.buffer.write(data_c)

# Print out help message
elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print(help_msg)
    sys.exit(1)


else:
    print("Invalid arguments. Please try python ende.py -h to see further instruction. Please try again.")
