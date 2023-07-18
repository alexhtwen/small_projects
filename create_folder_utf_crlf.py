import os

def create_folder_from_text(folder_names_file: str, path: str) -> None:
    # Read the text file with UTF-8 encoding and handle CR LF line endings
    with open(folder_names_file, 'r', encoding='utf-8', newline='\r\n') as file:
        lines = file.read().strip()
        for line in lines:
            line = line.strip('\n')
            # Create a folder using the text content
            folder_name = line.replace(' ', '_')  # Replace spaces with underscores
            os.makedirs(f'{path}{folder_name}')

            print(f"{path}{folder_name}' created successfully.")
            return None

# Usage example
folder_names_file = 'folder_name_utf.txt'
path = './'
create_folder_from_text(folder_names_file, path)
