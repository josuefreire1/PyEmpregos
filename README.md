# PyEmpregos

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/cdd93e640af24fc6ba1eccf5d48997fe)](https://app.codacy.com/app/josuefreire1/PyEmpregos?utm_source=github.com&utm_medium=referral&utm_content=josuefreire1/PyEmpregos&utm_campaign=Badge_Grade_Dashboard)

Created to have an easier way to watch all job offers, in a single page, in the categories that I'm interested.

Right now this program retrieves jobs info from net-empregos and prints on the console  for the category that was selected  

**To Build (you are going to need)**: python-3.7.2 and beautifulsoup4 and csv


## How to run

Change the data.txt to the search terms that you want:

```
QA Engineer
QA Analyst
Quality Assurance Engineer
```

Then run the script:

```
python empregossraper.py
```

At the end of execution you should see a file named scrape.csv
