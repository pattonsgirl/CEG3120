# Project 0.5 - DIY Container

In your `essentials` repository for this course, pick one of the below DIY container implementations.

## Option 1: DIY git server


## Option 2: App with Dependencies

1. Add code for an application
2. Create a `README.md` file that defines:
    - what the application is
    - 

## Option 3: Undocumented App

So once upon a time, I hacked together a script, [read-page.py](read-page.py), that does the following:
1. It opens this page: https://engineering-computer-science.wright.edu/computer-science-and-engineering/courses
2. It *opens a browser window to load it* because the page is not static content
3. It scrapes the page and saves it to a file for parsing by a *second* script

The second script, [parse-jackpot.py](parse-jackpot.py) just uses the soup output from the first file and:
1. Find each course link out of the soup
2. Visits each catalog page
3. Output the pre-reqs of each course to a file

Because I put this little app together while in a mood - I documented nothing - not the dependencies, not how to install them - nothing.

Funny how not writing READMEs, like we tell you guys to, bites.

Your challenge, if you choose to accept this third and worst case challenge, is to containerize my happy little app *.

In your repository, include:
- The source code files (my python code)
- An output file of the soup and of the pre-reqs, freshly scraped
- A `README.md` with:
    - what are the software dependencies of this code
    - which container image you used as a base
    - how you installed dependencies to the container environment
    - any changes required to the app or additions needed
    - instructions on how to use your container to run the code and get my precious output files
    - any troubleshooting to be aware of

> * I know for a fact Gemini can solve this one. Try to avoid temptation for a while - get comfy with the app, understand it's dependencies, draft what you think you need, then start playing 20 questions with an AI. When you do decide to see what AI would do, remember it will *unlikely* give you the perfect answer the first time - you'll still be iteratively testing and tweaking. Cite your sources, detangle *why* it recommends this solution, and carry on.
