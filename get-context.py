import os
import argparse

def combine_files_to_context(directory_path, output_filename="context.txt"):
    try:
        # Create or overwrite the context.txt file
        with open(output_filename, 'w', encoding='utf-8') as context_file:
            # Iterate over each file in the given directory
            for filename in os.listdir(directory_path):
                file_path = os.path.join(directory_path, filename)

                # Only process files (skip directories)
                if os.path.isfile(file_path):
                    print(f"Processing file: {filename}")
                    
                    # Open each file and append its contents to the context.txt
                    with open(file_path, 'r', encoding='utf-8') as file:
                        context_file.write(f"\n\n----- {filename} -----\n")  # Optional file separator for context
                        context_file.write(file.read())
            
        print(f"Context successfully written to {output_filename}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Combine contents of all files in a directory into a single context file.")
    
    # Argument for directory path (default is the current directory)
    parser.add_argument('directory', nargs='?', default='.', help="Path to the directory containing the files (default is the current directory).")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Combine the files into the context file
    combine_files_to_context(args.directory)

if __name__ == "__main__":
    main()

