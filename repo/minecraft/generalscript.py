import os
import sys
import urllib.request

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <url> <folder_name>")
        return

    url = sys.argv[1]
    folder_name = sys.argv[2]
    file_name = url.split("/")[-1]
    run_script = f"java -jar {file_name} --nogui"

    multiclient_folder = "multiclient"
    os.makedirs(multiclient_folder, exist_ok=True)

    client_folder = os.path.join(multiclient_folder, folder_name)
    os.makedirs(client_folder, exist_ok=True)

    urllib.request.urlretrieve(url, os.path.join(client_folder, file_name))

    with open(os.path.join(client_folder, "run.sh"), "w") as run_file:
        run_file.write(run_script)

    os.chmod(os.path.join(client_folder, "run.sh"), 0o755)

    with open(os.path.join(client_folder, "eula.txt"), "w") as eula_file:
        eula_file.write("eula=true")
    print('SUCCESS')

if __name__ == "__main__":
    main()
