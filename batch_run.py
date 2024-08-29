import os
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--base_dir')
parser.add_argument('--output_dir')
args = parser.parse_args()



base_dir = args.base_dir
output_dir = args.output_dir

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through all subdictionary in the base dictionary
for subdir in os.listdir(base_dir):

    # Get path
    subdir_path = os.path.join(base_dir, subdir)

    # Ensure it's a directory
    if not os.path.isdir(subdir_path):
        print(f"Skipping {subdir_path}, as it is not a directory.")
        continue

    w2v_path = os.path.join(subdir_path, "word2vec.txt")
    ws_child_path = os.path.join(subdir_path, "wsChildren.txt")
    catcode_path = os.path.join(subdir_path, "wscatCode.txt")

    # Check if all input files exist
    if not all(os.path.exists(path) for path in [w2v_path, ws_child_path, catcode_path]):
        print(f"Skipping {subdir_path}, missing one or more required input files.")
        continue

    # Output path
    output_path = os.path.join(output_dir, subdict)
    train_nball_path = os.path.join(output_path, "nball.txt")
    log_path = os.path.join(output_path, 'log.txt')

    # Construct the command
    command = [
        'python', 'nball.py',
        '--train_nball', train_nball_path,
        '--w2v', w2v_path,
        '--ws_child', ws_child_path,
        '--ws_catcode', catcode_path,
        '--log', log_path
    ]

    # Run the command using subprocess
    print(f"Running command for {subdir}: {' '.join(command)}")
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"Successfully processed {subdir}.")
    except subprocess.CalledProcessError as e:
        print(f"Error running command for {subdir}: {e.stderr}")

print("Batch processing complete.")
