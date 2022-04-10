import sys
import src.greeter as greeter
# import subprocess

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        print(greeter.get_greeting(args[0]))

    # subprocess.call(f"cp -TR {args[1]}/SnortInstall/snort/etc /etc/snort", shell=True)
    # subprocess.call(f"cp -TR {args[1]}/SnortInstall/snort/rules /etc/snort/rules", shell=True)
    # subprocess.call("snort -D -A fast -l /tmp -c /etc/snort/snort.conf", shell=True)
    
if __name__ == "__main__":
    main()