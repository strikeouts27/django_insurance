# django_insurance
 Data from Postgres



## Create your settings file

Appropriate settings will vary between developers and environment. The settings files are an appropriate way to make those changes.

In django_insurance/config/settings, you'll find a `sample_dev.py` file. Copy it and name the copy `local_settings.py`. (You can name it whatever, but if you pick a personal name, please add it to .gitignore to protect any API keys that might be stored there.) Change the SECRET_KEY value while you're in there. Your local settings file is not particularly vulnerable, but as a matter of best practice, it's worth taking a second to make a secure key. You can do this from a Python interpreter with:

```
import secrets
print(secrets.token_urlsafe(80))
```

If you look at `manage.py`, you'll notice that the Django settings file can be controlled by an environment variable. How you manage that is up to you, but I personally find it convenient to add it to the venv activate.bat script. You can do this with `set DJANGO_SETTINGS_MODULE=django_insurance.config.settings.local_settings`. Note that any changes you make to `activate.bat` won't be reflected until you re-run the script. To do this, run `deactivate`, then `env\Scripts\activate.bat`
