## gradeScraper info
Two pyhton scripts.

The first one that should run is gradeScraper.py

One does use Selenium https://selenium-python.readthedocs.io/ to log in to Ugla.
It uses your ugla login and passwords that are stored in environment variables, because security
Here is an example on how to store and access environment variables in python for Windows machines: https://www.youtube.com/watch?v=IolxqkL7cD8&t=217s

Selenium looks for certain inputs and/or buttons by searching for their ID or name.

After it has logged in it downloads the html for the Ugla - Námskeiðin mín page. It is important that you put that url as the url to access. The HTML from ugla is downloaded to uglaHTML file.

The second script that runs is the checkAndEmail.py file.
There you load the uglaHTML file that stores the HTML for Ugla - Námskeiðin mín page. On that site you will find your grade in a table, it is IMPORTANT that you change one value in that file for it to work correctly.

This script uses BeautifulSoup to search in the HTML, this looks like a real handy module, I recommend to play around with it youtube.com/watch?v=ng2o98k983k&t=633s

In line #13 in the checkAndEmail.py file you count how many instances of "olokid gildir_kanski_til_gradu info" are in the HTML code. This will change when you receive a grade. So you have to make it match the number of grades you are still to receive.
For example: I have still to receive 2 grades, hence the value is <2 now. So when this value goes below 2 it should send me an email to notify me.

It is defenitely not a good way because you would need to change the value after you get a grade so that you will still get an email for the next grade. I'll leave it as problem for you to solve.

If your statement returns the true value, i.e that you have received an grade it will send you an email using smtplib https://docs.python.org/3/library/smtplib.html.
For me made a gmail account to send me emails. You could do the same or use some different method. The smtplib module is set up to send a message to my gmail.

There is a .bat file that runs the both scripts. You could use task scheduler in Windows to schedule these Python scripts to run x times a day as you will.

## Use

Feel free to fork this and play with as you like. In no means is this a super good or well designed project. It does work and since I'm only waiting for one grade to arrive and it should do so in the next few days I feel like this works for me as it is.

if you want to play around with it you will of course need python set up on your machine, I used Python 3.8.2 and pip to install modules.
The modules I used in this project:

os - https://docs.python.org/3/library/os.html

smtplib - https://docs.python.org/3/library/smtplib.html

beautifulSoup - https://beautiful-soup-4.readthedocs.io/en/latest/

time - https://docs.python.org/3/library/time.html

Selenium - https://selenium-python.readthedocs.io/

This is just made for fun so there is 100% possibilty to do this project a lot better, but here is at least a starting point :)

### Extra files

There are some extra files in this directory, most of them where used because I was going to use another method to check for grades first. These files are: compare.py, origin.html, test.html and diff.html

chromedriver.exe is needed for the Selenium to work. See in the documentation.

