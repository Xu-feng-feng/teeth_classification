import os

def process_txt_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Define the interval for adding [-,-,-]
    interval = 120

    # Create a new list to store modified lines
    modified_lines = []

    # Add [-,-,-] at the beginning of the file
    modified_lines.append("-,-,-")

    # Iterate through the original lines
    for i, line in enumerate(lines):
        modified_lines.append(line.strip())

        # Check if it's time to add [-,-,-]
        if (i + 1) % interval == 0:
            modified_lines.append("-,-,-")

    # Write the modified lines back to the file
    with open(file_path, 'w') as f:
        f.write('\n'.join(modified_lines))

def batch_process_txt_files(root_folder):
    for folder_path, _, file_names in os.walk(root_folder):
        print("Current folder:", folder_path)

        # Filter out only the txt files
        txt_files = [file for file in file_names if file.endswith('.txt')]
        print("txt_files:", txt_files)

        if not txt_files:
            print("No txt files found in this folder.")
            continue

        # Process each txt file in the current folder
        for txt_file in txt_files:
            file_path = os.path.join(folder_path, txt_file)
            print("Processing:", file_path)
            process_txt_file(file_path)

    print("Batch processing complete!")

if __name__ == '__main__':
    # Replace 'your_root_folder_path' with the actual root folder path containing the txt files
    root_folder = r'C:\\dataset\\imu_demo\\trainv3\\data\\2023_7_20'
    batch_process_txt_files(root_folder)
