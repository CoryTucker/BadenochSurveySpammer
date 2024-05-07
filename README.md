# BadenochSurveySpammer
A simple python project to (hopefully) spam this survey: https://www.smartsurvey.co.uk/s/55NP2K/

# Current status
All the backend stuff is in a 'functional' state - in that the code can fill in all the questions and send survey responses out. 
In #issues i've outlined some things that need finishing before it's fully fuctional though. The main things are getting chatGPT intergration working, and me adding some structure to allow it to run in the background instead of a 1-and-done debug test thingy.

# Running - 
this is the first draft of these instructions. If anyone wants to help improve them, please do.
I'm assuming that you have git and python installed already.

Clone the git repository
```
git clone https://github.com/CoryTucker/BadenochSurveySpammer
```
From the installation directory, run
```
pipenv update
```
Then, to run the project:
```
python main.py
```
As of currently, i'd give this about a 1 in 20 chance of working as i haven't done much testing, so feel free to open issues and / or pull requests to get things up and running.

# More detailed running instructions (for windows)
These are the steps I needed to go through to get this working on my windows boot drive:
I've probably simplified them too much but it's better than them being confusing.

Download and install git from: [https://git-scm.com/downloads](https://git-scm.com/download/win)
Download and install python from : [https://www.python.org/downloads/](https://www.python.org/downloads/release/python-3122/)
(specifically, python 3.12.2 - this is important)

Make sure to tick the box titled 'Add python.exe to PATH' (this makes it so you can run python from the command prompt)

Open up the newly installed application 'Git Bash', which gives a linux-like console

Run the commands:
```
cd Documents/
git clone https://github.com/CoryTucker/BadenochSurveySpammer
cd BadenochSurveySpammer/
```
This clones the git repository into your Documents/ Folder


This part roughly follows this tutorial : [https://www.pythontutorial.net/python-basics/install-pipenv-windows/](https://pipenv.pypa.io/en/latest/installation.html)
Next, open up a regular windows command prompt, and install pipenv with:
```
pip install pipenv
```

Next, we need to add an environment variable to the PATH so pipenv can run.
First, run
```
python -m site --user-site
```
and copy the output.

For me it looked like this:
```
C:\Users\corye\AppData\Local\......\site-packages
```

Remove 'site-packages' from the end and add 'Scripts' instead


Open settings and search for 'environment variable'.
Click on 'Envionment variables' under the 'Advanced' tab
In 'User variables for $username', click on 'Path' and 'Edit'
In the new window, click 'New' and paste in the output of the command we got before.

Close and reopen the command prompt so the path changes are registered



Next, install the required python packages using pip
Run the commands:
```
cd Documents\BadenochSurveySpammer
pipenv sync
```
And finally, run the program with:
```
pipenv run python main.py
```

Running the project from a fresh instance of command prompt can be done with
```
cd Documents/BadenochSurveySpammer
pipenv run python main.py
```

