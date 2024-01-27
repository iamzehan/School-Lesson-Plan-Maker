import subprocess

def run(script_path):
    try:
        # Run the Bash script using subprocess
        subprocess.run(["streamlit", "run", script_path])
    except subprocess.CalledProcessError as e:
        print(f"Error running the Bash script: {e}")

if __name__ == "__main__":
    run("app/Home.py")