# PHP Simple Initializer (phi)

Looking for a speedy start for your future PHP projects? Is AI _not quite enough_ when it comes to speeding things up? Would you like to use the same type of admin panel in every project? Do you have favorite or frequently-used files or structures you want to add to your projects immediately, so you don’t have to worry about them later?

Enter the PHP Simple Initializer, one of the most practical tools for this task. With PHP Simple Initializer, you can jump-start your project using a pre-existing structure or even fully-functional parts of an application you don’t want to recreate repeatedly. With this tool, you can stop worrying about repetitive code and focus on the more important aspects of your work.

---

## Why Does This Exist?

As a freelance software developer who takes software production seriously, I value being able to deliver my projects efficiently. The first "project initializer" I made was for Selenium web automation projects in Python. While it didn’t significantly boost my overall development speed, it allowed me to start projects right away. However, after migrating to C# for web automation, the Selenium initializer became obsolete. Nonetheless, it inspired me to create this application.

Additionally, I drew inspiration from IDEs like Dev-C++ and Visual Studio, which allow developers to start projects using templates. I developed this program as a far simpler yet equally effective alternative for PHP.

---

## Who Is This For?

This program is ideal for:

- Freelancers who want a head start in their projects (like me).
- Developers who don’t want to rewrite their trusted modules repeatedly.

If you have reliable, time-tested modules that you frequently use, simply add them to the `project-skeletons` or `addons` folder, specify their folder names as arguments, and you’re good to go.

---

## How To Use It

Follow these steps to use the PHP Simple Initializer:

1. You need to have Python installed on your system. A basic understanding of Python is also helpful if you want to customize the program.
2. After making the necessary edits, run `compile.bat` to compile the application using PyInstaller (install with `pip install pyinstaller` if needed).
3. Ensure the application is included in your system's PATH variable.
4. Add your frequently-used modules and project templates to either the `project-skeletons` or `addons` folder. Create a new folder inside these directories to store your code. If it’s in the `project-skeletons` folder, you may need to specify an argument to copy the folder.
5. Navigate to your working directory in File Explorer, type `cmd` in the address bar to open the Command Prompt.
6. Run `phi` with the necessary arguments. For example:
   ```bash
   phi --admin --addon login
7. Voilà! PHP Simple Initializer will handle the repetitive setup work for you.

---


## How Effective Is It?

The effectiveness of this tool depends on your use case and the amount of code you prepare for it. The more modules and templates you add, the better it becomes! It can even outperform some of the most advanced AI models when it comes to repetitive project setups.

Ultimately, this application is a small but **highly efficient** tool. Even if you need to prepare your own templates and addons initially, PHP Simple Initializer can save you time and reduce deadline stress.

## Can This Application Improve?

Absolutely! I have several ideas for enhancing this application. As its developer, I use it every time I start a new project and estimate that it saves me **over a day’s worth of work**. I firmly believe this tool has the potential to make development faster both at the start and throughout. I plan to periodically update this repository with minor fixes and new features.

If you have an idea for a better project initializer, feel free to fork this repository and create your own! The more initializers we have, the fewer developers will worry about deadlines.