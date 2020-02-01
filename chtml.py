

def changecontent(old_file, new_file, old_str1, new_str1, old_str2, new_str2):
    content = open(old_file)
    with open(new_file, 'w') as f:
        for line in content:
            f.write(line.replace(old_str1, new_str1).replace(old_str2, new_str2))

    content.close


changecontent('announcements.html','t2.html', "Date_content", "New_Date", None, None)