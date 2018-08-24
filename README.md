# KCLPureGenerator
Script for finding the KCL Pure URL for a given KCL academic. Works well on a big long `.txt` list of accademics 

## How to Install This
[Download this repo as a zip and extract it](https://github.com/mattallinson/KCLPureGenerator/archive/master.zip)
You may need to [install Python](https://www.python.org/downloads/) if you are using a windows machine

## How to Run This
Open a terminal in the folder that you have unzipped the repo to, copy and paste your big long `.txt` list of accademics into the same folder.

In your terminal type:
```
$ ~ python3 pure_profile_generator.py <list of accademics>.txt
```

You should get the following output 

```
239 / 245
Firstname Lastname 
	URL Found 👍
240 / 245
Firstname Lastname 
	URL Found 👍
241 / 245
Firstname Lastname 
	NO URL FOUND ⚠️
242 / 245
Firstname Lastname 
	URL Found 👍
```

You will also get a new file appearing in your folder called pure-profiles.txt, which will now look like this

```
Firstname Lastname, https://kclpure.kcl.ac.ukhttps://kclpure.kcl.ac.uk/portal/en/persons/firstname-lastname(2e0ffa7c-9dcc-49e3-9bf0-7d782ed37c1f).html
Firstname Lastname, https://kclpure.kcl.ac.ukhttps://kclpure.kcl.ac.uk/portal/en/persons/firstname-lastname(891c46cb-582b-4d53-8621-afdda264e395).html
Firstname Lastname,  --not found -- 
Firstname Lastname, https://kclpure.kcl.ac.uk/portal/firstname-lastname.html
```

### Turn This Into An Excel

* Open Microsoft Excel.
* Click on the Data tab.
* In the Get External Data group, click From Text.
* Double-click the text file that you want to import in the Import Text File dialogue box.
* Click Import. The Text Import Wizard will begin.
* Select Delimited and click Next.
* Uncheck Tab and select Comma.
* Click Next.
* Click Finish.