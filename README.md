# drink-and-eat-reminder
simple drink and eat reminder

How To (win10):
Install python (with pip)
pip install win10toast
Edit .bat file and add your python location and .bat file location
Go to Settings
Search Administrative Tools
Open Task Scheduler
Create a Basic Task (Trigger-> Daily, Action Start a Program, Program/script select the .bat file)
Right click on the task you created and go to properties:
	Triggers Tab: select repeat task every: xx minutes (i've choosen 15mins)
	Actions Tab: add before %comspec% /c start "" /min
		eg. %comspec% /c start "" /min "C:\targetlocation\execute drink.bat"
Right click on the task and select run.
	