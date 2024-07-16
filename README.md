# django_insurance

STEPS BEFORE JOINING THE PROJECT 
### Step 1. FORK THE PROJECT FIRST BY HITTING THE FORK BUTTON ON THE REPOSITORY HOMEPAGE. 
# https://github.com/strikeouts27/django_insurance

### GITHUB DOC LINK: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo

### Step 2 GIT CLONE THE PROJECT: 
### GITHUB GIT CLONE DOC LINK: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

### Step 3 Create your settings file by copying the sample_dev.py file. After that rename the folder local_settings.py

### STEP 4 CREATE VIRTUAL ENVIORNMENT (USING GITBASH AS YOUR TERMINAL TYPE PREFERRED)  PYTHON DOCUMENTATION LINK: https://docs.python.org/3/library/venv.html

### NOTE IF ACTIVATE COMMAND NOT WORKING CHECK YOUR VENV FOLDER FOR WHAT FOLDERS EXISIT. YOU MAY NEED TO RUN source venv/Scripts/activate because windows does not load the same folders as macintosh and therefore the command to activate it may not line up with what needs to be done. 

### STEP 5 USE THIS REQUIREMENTS COMMAND TO ALL REQUIRMENTS FOR PROJECT. 
# pip install -r requirements.txt

### STEP 6 UPDATE SETTINGS FILE BY CHANGING THE SECRET KEY VALUE TO WHATEVER YOU WANT
Appropriate settings will vary between developers and environment. The settings files are an appropriate way to make those changes.

In django_insurance/config/settings, you'll find a `sample_dev.py` file. Copy it and name the copy `local_settings.py`. (You can name it whatever, but if you pick a personal name, please add it to .gitignore to protect any API keys that might be stored there.) Change the SECRET_KEY value while you're in there. Your local settings file is not particularly vulnerable, but as a matter of best practice, it's worth taking a second to make a secure key. You can do this from a Python interpreter with:

In your virtual enviornment folder you should see scripts folder. go into the activate file add this following line right under neath the export virtual_env line. By doing this when you run activate it will point to your django settings folder. 

export DJANGO_SETTINGS_MODULE=django_insurance.config.settings.local_settings

```
# on Windows, a path can contain colons and backslashes and has to be converted:
if [ "${OSTYPE:-}" = "cygwin" ] || [ "${OSTYPE:-}" = "msys" ] ; then
    # transform D:\path\to\venv to /d/path/to/venv on MSYS
    # and to /cygdrive/d/path/to/venv on Cygwin
    export VIRTUAL_ENV=$(cygpath "C:\Users\Andrew\Desktop\django_projects\django_insurance\venv")
    # we need to use activate file as we have NOT edited activate.bat or activate ps1
    # this next line is the one you should add 
    export DJANGO_SETTINGS_MODULE=django_insurance.config.settings.local_settings
else
    # use the path as-is
    export VIRTUAL_ENV="C:\Users\Andrew\Desktop\django_projects\django_insurance\venv"
fi
```
# Note you cannot have spaces after variable.

### STEP 7 MAKE AND UPDATE GIT IGNORE FILE and input these lines so git will not upload them into the repository. 

__pycache__
env/
django_insurance/config/settings/local_settings.py
venv

### STEP 8 SEE GITHUB ISSUES IN THE REPOSITORY AND LET ME KNOW WHAT YOU WOULD LIKE TO WORK ON. 

THE POINT OF CREATING THIS SETTINGS AND CONFIG FOLDER IS INDEPENDENCE FOR EVERY DEV TO HAVE THEIR OWN SETTINGS.PY AND SET UP THEIR PREFRENCES. 

base.py -> the standard settings that all of the devs can share.

local_settings.py -> how we have our own custom settings. it imports all of base settings.

sample_dev.py is what you share with a developer who has joined the project. they make a copy of this folder and mdake changes as necessary.

people can use gitbash, powershell, cmd, zsh whatever using this technique.

####

local settings folder

sample_dev.py -> make a copy of this folder and rename the folder local_settings.py

```
import secrets
print(secrets.token_urlsafe(80))
```

If you look at `manage.py`, you'll notice that the Django settings file can be controlled by an environment variable. How you manage that is up to you, but I personally find it convenient to add it to the venv activate.bat script. You can do this with `set DJANGO_SETTINGS_MODULE=django_insurance.config.settings.local_settings`. Note that any changes you make to `activate.bat` won't be reflected until you re-run the script. To do this, run `deactivate`, then `env\Scripts\activate.bat`

