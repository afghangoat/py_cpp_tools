import os

def replace_directory_for_string(directory, find,replace_str,ishtml):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if ishtml==False or (file_path.endswith(".html") or file_path.endswith(".php")):
                try:
                    found=False
                    content=""
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if find in content:
                            content = content.replace(find, replace_str)
                            print(f"Replacing in: {file_path}")
                            found=True
                    with open(file_path, "w", encoding='utf-8') as f:
                        f.write(content)
                except (UnicodeDecodeError, PermissionError) as e:
                    print(f"Skipped (cannot read): {file_path} ({e})")

if __name__ == "__main__":
    input_dir = input("Enter the directory to scan: ")
    search_str = input("Enter the string to search for: ")
    repl_str = input("Enter the string replace the string before: ")
    html_only = input("HTML only? (y/n):")
    bool_html=True
    if html_only=="n":
        bool_html=False

    if not os.path.isdir(input_dir):
        print("Invalid directory.")
    else:
        replace_directory_for_string(input_dir, search_str,repl_str,bool_html)

#https://afghangoat.hu/guidel.html