# Exchange4Students

SSW-322 Engineering Design VI Final Project

## Running the Project

_Prereq: make sure you have pip installed, refer to documentation [here](https://pypi.org/project/pip/) for instructions_

1. Clone this repository

```
git clone https://github.com/elenirotsides/Exchange4Students.git
```

2. Navigate into the project

```
cd Exchange4Students
```

3. Install the required packages

```
pip install -r requirements.txt
```

4. Run the flask server from the src folder

```
python src/app.py
```

**or**

If you have python 2 and python 3 installed, python 2 will most likely be the default (unless you've changed the default to be python 3), so you need to make sure you're using python 3 to run this application.

```
python3 src/app.py
```

## Mongo Setup

In order to test, you need to make sure you have MongoDB installed, see https://docs.mongodb.com/manual/administration/install-community/ for details. I also recommend installing MongoDB Compass Community (https://docs.mongodb.com/compass/master/install/), which is basically a GUI for Mongo. I prefer Compass over the traditional way of interacting with Mongo, which is via the command line.

By default, Mongo will run on port 27017, so don't change that because that's what the code references right now.

Run `mongod` on your command line. Depending on your settings you may need to run `sudo mongod --config /etc/mongod.conf` on Linux or Mac. You'll have to leave this running in the background.

Then, open MongoDB Compass. When you open MongoDB Compass, it'll ask you to enter the `Connection String`. Click  "Fill in connection fields individually." Here are what my settings look like:

![Mongo settings](mongo.png)

Then, hit Connect to connect to the database.

FYI: I don't use my local instance of MongoDB for any intense dev work, which is why I don't have anything selected for the Authentication field.

**I recommend saving your connection string as a favorite in Compass, so you don't have to keep typing stuff in each time you want to connect to the database**

## Seed your Database

### What is it?

Its always easiest to have a script you can run that will 'seed' the database for you with fake data when in the development stage (which is all the time). A seed file is like a script you can run that will populate the database with fake data so the focus can remain on the coding and less on needing to get data in the database.

### How do I run it?

You run the seed file from the src folder

`python src/seed.py` or `python3 src/seed.py`

Watch your terminal as the seed file executes. Blink and you'll miss it!

**You do not need to delete your existing database, as this script will do it for you!**

If by any chance something fails, that means the database schema has been changed and you'll need to slightly edit the file. See the next section for details on that.

### What if the database schema gets updated?

No worries, you can edit the seed file! Example: if we decide to add a timestamp field to the database, then the functions in the seed file will need the timestamp argument to be provided. So, you'll just go in and add that little piece to each function. This is much easier than having to write all the functions from scratch to get fake data in the db so you can proceed with coding.
