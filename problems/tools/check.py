import os

def check_files(directory):
    # List of files in the directory, sorted numerically
    files = sorted([f for f in os.listdir(directory) if f.endswith('.txt')], 
                   key=lambda x: int(os.path.splitext(x)[0]))
    
    previous_content = None  # To store the content of the previous file
    similar_count = 0  # Counter for similar files
    
    for i, file in enumerate(files):
        file_path = os.path.join(directory, file)
        
        # Check if the file is empty
        if os.path.getsize(file_path) == 0:
            print(f"Processing {file}: File is empty.")
            continue
        
        # Read the current file content
        with open(file_path, 'r') as f:
            current_content = f.read()
        
        # Check if the current file content matches the previous one
        if previous_content is not None:
            if current_content == previous_content:
                print(f"Processing {file}: Same content as {files[i-1]}.")
                similar_count += 1
            else:
                print(f"Processing {file}: Content is different from {files[i-1]}.")
        else:
            print(f"Processing {file}: No previous file to compare.")
        
        # Update previous content
        previous_content = current_content
    
    # Final report
    print(f"\nTotal number of files with similar content: {similar_count}")

# Usage
directory = "./raw"
check_files(directory)
