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

    os.makedirs(folder_name, exist_ok=True)

    urllib.request.urlretrieve(url, os.path.join(folder_name, file_name))

    with open(os.path.join(folder_name, "run.sh"), "w") as run_file:
        run_file.write(run_script)

    os.chmod(os.path.join(folder_name, "run.sh"), 0o755)

if __name__ == "__main__":
    main()
