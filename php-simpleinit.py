import shutil
import os
import sys
import argparse

#dictionary for libraries. keys are simpler names for easy writing, and values are full names for installing
library_map = {
    "phpmailer": "phpmailer/phpmailer",
    "qr-code": "endroid/qr-code",
    "google-apiclient": "google/apiclient"
    #can be expanded depending on the libraries you use
}

print("PHP Simpleinit v3")

def main():
    try:
        #parser as the program is a CLI tool that takes arguments
        parser = argparse.ArgumentParser(description="PHP Simple Initializer")
        #you can make your own arguments depending on your style of programming
        #example arguments
        # parser.add_argument("--admin", action="store_true", help="Create the default project with admin panel")
        # parser.add_argument("--production", action="store_true", help="Create a production-grade template for fast development")
        #can take subarguments (eg --addon login about contact)
        parser.add_argument("--addon", nargs='+', type=str, help="Specify an addon to include in the project")
        args = parser.parse_args()
        
        #for the application to operate in the directory it was called (through CMD/Terminal)
        if getattr(sys, 'frozen', False):
            executable_dir = os.path.dirname(sys.executable)
        else:
            executable_dir = os.path.dirname(os.path.abspath(__file__))
        
        #if-elif-else structure for each argument like --admin and --production, depending on the argument and your template layout
        if args.admin:
            template_dir = os.path.join(executable_dir, 'project-skeletons/default-with-admin')
            print("Creating a default project with admin panel...")
        elif args.production:
            template_dir = os.path.join(executable_dir, 'project-skeletons/production')
            print("Creating a production template project...")
        else:
            template_dir = os.path.join(executable_dir, 'project-skeletons/default')
            print("Creating a default project...")
        
        #copying the chosen template to the current directory
        current_dir = os.getcwd()
        for item in os.listdir(template_dir):
            src = os.path.join(template_dir, item)
            dst = os.path.join(current_dir, item)
            if os.path.isdir(src):
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)
        
        #calls the function that installs the libraries via Composer
        install_libraries()
        #if --addon argument is used
        if args.addon:
            addons_dir = os.path.join(executable_dir, 'addons') #directory for addons (needs to be in the same directory as the program itself)
            for addon in args.addon: #for each addon
                addon_path = os.path.join(addons_dir, addon)
                if not os.path.exists(addon_path):
                    print(f"Can't find addon '{addon}' bulunamadı. Please check the 'addons' folder.")
                    continue
                for item in os.listdir(addon_path): #copies each addon folder to the project's directory
                    src = os.path.join(addon_path, item)
                    dst = os.path.join(current_dir, item)
                    if os.path.isdir(src):
                        shutil.copytree(src, dst, dirs_exist_ok=True)
                    else:
                        shutil.copy2(src, dst)  
                
                print(f"'{addon}' has been successfully added to the project!")
                
        print("Project is successfully created! Have a good development :)")
    except Exception as e:
        print(f"Error: {e}")

def install_libraries():
    try:
        library_file = 'libs.txt' #there needs to be a libs.txt in the directory of the project beforehand, containing keys of library_map
        if os.path.exists(library_file):
            with open(library_file, 'r') as file:
                libraries = file.readlines()
            
            composer_command = "composer require" #needs Composer in the system to work
            for library in libraries:
                library = library.strip().lower()
                if library in library_map:
                    full_name = library_map[library]
                    composer_command += f" {full_name}"
            os.system(composer_command)
            print("Successfully installed the libraries!")
        else:
            print(f"Create a {library_file} file if you want to install libraries to your project.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main() #starts the application