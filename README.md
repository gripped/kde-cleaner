

    kde-cleaner --help  
    usage: kde-cleaner [-h] [--delete] [--list] [--programs]  
      
    Creates a timestamped backup of KDE config files to ~/.local/share/kde-cleaner and optionally deletes the originals.  
      
    options:  
    -h, --help show this help message and exit  
    --delete, -d Deletes the config files after backing up  
    --list, -l Lists the config files covered by the program and then exits  
    --programs, -p Also process a limited set of KDE program configs  
      
    With no options given a backup of of non program KDE config files will be made
