"""
INSTALLATION

Install and Run Python in Mac OS X

Go to Download Python page on the official site and click Download Python 3.6.0 (You may see different version name).
When the download is complete, open the package and follow the instructions.
You will see "The installation was successful" message when Python is successfully installed.
It's recommended to download a good text editor before you get started. If you are a beginner,
I suggest you to download Sublime Text. It's free.
The installation process is straight forward. Run the Sublime Text Disk Image file you downloaded and follow the instructions.
Open Sublime Text and go to File > New File (Shortcut: Cmd+N). Then, save (Cmd+S or File > Save) the file with .py
extension like: hello.py or first-program.py
Write the code and save it again. For starters, you can copy the code below:
print("Hello, World!")
This simple program outputs "Hello, World!"
Go to Tool > Build (Shortcut: Cmd + B). You will see the output at the bottom of Sublime Text.Congratulations,
you've successfully run your first Python program.


Install and Run Python in Linux (Ubuntu)

Install the following dependencies:
$ sudo apt-get install build-essential checkinstall
$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
Go to Download Python page on the official site and click Download Python 3.6.0 (You may see different version name).
In the terminal, go to the directory where the file is downloaded and run the command:
$ tar -xvf Python-3.6.0.tgz
This will extract your zipped file. Note: The filename will be different if you've downloaded a different version.
Use the appropriate filename.
Go to the extracted directory.
$ cd Python-3.6.0
Issue the following commands to compile Python source code on your Operating system.
$ ./configure
$ make
$ make install
We recommend you to install Sublime Text if you are a newbie. To install Sublime Text in Ubuntu (on 14.04).
Issue following commands.
$ sudo add-apt-repository -y ppa:webupd8team/sublime-text-2
$ sudo apt-get update
$ sudo apt-get install sublime-text
Open Sublime text. To create a new file, go to File > New File (Shortcut: Ctrl+N).
Save the file with .py file extension like: hello.py or first-program.py
Write the code and save it (Ctrl+S or File > Save) . For starters, you can copy the code below:
print("Hello, World!")
This simple program outputs "Hello, World!"
Go to Tool > Build (Shortcut: Ctrl+B). You will see the output at the bottom of Sublime Text. Congratulations,
you've successfully run your first Python program.


Install and Run Python in Windows

Go to Download Python page on the official site and click Download Python 3.6.0 (You may see different version name).
When the download is completed, double-click the file and follow the instructions to install it.
When Python is installed, a program called IDLE is also installed along with it. It provides graphical user interface
to work with Python.
Open IDLE, copy the following code below and press enter.
print("Hello, World!")
To create a file in IDLE, go to File > New Window (Shortcut: Ctrl+N).
Write Python code (you can copy the code below for now) and save (Shortcut: Ctrl+S) with .py file extension
like: hello.py or your-first-program.py
print("Hello, World!")
Go to Run > Run module (Shortcut: F5) and you can see the output. Congratulations, you've successfully run your
first Python program.

"""

"""
INSTALLATION

Download the latest version of Python.
Run the installer file and follow the steps to install Python
During the install process, check Add Python to environment variables. 
This will add Python to environment variables and you are able to run Python from any part of the computer.
Also, you can choose the path where Python is installed.
Once you finish the installation process, you can run Python.

1. Run Python in Immediate mode

Once Python is installed, typing python in the command line will invoke the interpreter in immediate mode. 
We can directly type in Python code and press enter to get the output.
Try typing in 1 + 1 and press enter. We get 2 as the output. This prompt can be used as a calculator. 
To exit this mode type quit() and press enter.


2. Run Python in the Integrated Development Environment (IDE)

1. We can use any text editing software to write a Python script file.
2. We just need to save it with the .py extension. But using an IDE can make our life a lot easier. 
    IDE is a piece of software that provides useful features like code hinting, syntax highlighting and checking, 
    file explorers etc. to the programmer for application development.
3. By the way, when you install Python, an IDE named IDLE is also installed. You can use it to run Python on your computer. 
    It's a decent IDE for beginners.
4. When you open IDLE, an interactive Python Shell is opened.
5. Now you can create a new file and save it with .py extension. For example, hello.py
6. Write Python code in the file, save it. To run the file go to Run > Run Module or simply click F5.

"""