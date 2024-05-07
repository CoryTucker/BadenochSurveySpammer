# BadenochSurveySpammer
A simple python project to (hopefully) spam this survey: https://www.smartsurvey.co.uk/s/55NP2K/

# Current status
All the backend stuff is in a 'functional' state - in that the code can fill in all the questions and send survey responses out. 
In #issues i've outlined some things that need finishing before it's fully fuctional though. The main things are getting chatGPT intergration working, and me adding some structure to allow it to run in the background instead of a 1-and-done debug test thingy.

# Running - this is the first draft of these instructions. If anyone wants to help improve them, please do.
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
