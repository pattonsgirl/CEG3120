# Project 1 Rubric

## Total Score: / 50.5

Grading notes:
- **Command example** = a usage of the command with real arguments where the command needs them (bare commands like `git checkout` are noted in feedback).
- **Explanation** = what the command does, in your own words. A partly incorrect explanation earns half credit; one that describes a different concept earns none.

## Command line git ( / 15)

0.5 points each

- status
    - [ ] command example
    - [ ] explanation
- log
    - [ ] command example
    - [ ] explanation
- clone
    - [ ] command example
    - [ ] explanation
- remote
    - [ ] command example
    - [ ] explanation
- add
    - [ ] command example
    - [ ] explanation
- rm 
    - [ ] command example
    - [ ] explanation
    - [ ] untrack (`--cached`, file kept) vs untrack & remove from workspace - both explained
- commit
    - [ ] command example
    - [ ] explanation
- push
    - [ ] command example
    - [ ] explanation
- pull
    - [ ] command example
    - [ ] explanation
- branch
    - [ ] command example
    - [ ] explanation
- checkout
    - [ ] command example
    - [ ] explanation
- fetch
    - [ ] command example
    - [ ] explanation
- merge
    - [ ] command example
    - [ ] explanation
- init
    - [ ] command example
    - [ ] explanation
    - [ ] initialize an existing folder vs create a bare repository - both explained

## git files & folders ( / 4)

1 pt each

- .git folder
    - [ ] explain the overall purpose of the folder
    - [ ] purpose of each item in the folder's contents
- .gitignore file
    - [ ] specifies location for proper function - in root of repository folder
    - [ ] explains the purpose

## Command line docker ( / 14.5)

0.5 points each

- ps
    - [ ] command example
    - [ ] explanation
    - [ ] includes active and ability to view all (`-a`)
- images
    - [ ] command example
    - [ ] explanation
- run
    - [ ] command example
    - [ ] explanation
    - [ ] includes flags: `-it`, `-p`, `--name`
- start
    - [ ] command example
    - [ ] explanation
- stop
    - [ ] command example
    - [ ] explanation
- exec
    - [ ] command example
    - [ ] explanation
- attach
    - [ ] command example
    - [ ] explanation
- import
    - [ ] command example
    - [ ] explanation
- export
    - [ ] command example
    - [ ] explanation 
- inspect
    - [ ] command example
    - [ ] explanation
- logs
    - [ ] command example
    - [ ] explanation
- kill
    - [ ] command example
    - [ ] explanation
- rm
    - [ ] command example
    - [ ] explanation
    - [ ] includes `docker rm` versus `docker rmi`

## SSH ( / 9)

Steps get credit when following the guide would actually perform the task.

- SSH authentication to GitHub repositories
    - [ ] creating key pair
    - [ ] setting up public key in user settings (Settings → SSH and GPG keys)
    - [ ] getting the ssh URI for cloning (Code → SSH tab)
- SSH authentication to an AWS instance
    - [ ] where to retrieve private key
    - [ ] permissions needed for private key
    - [ ] where to find public IP
    - [ ] writing an `ssh` command to establish a connection
- Using the `config` file in the `.ssh` folder
    - [ ] example entry block
    - [ ] using entry after block is configured (`ssh <alias>`)

## Demonstrations ( / 8)

2 pts each

- [ ] A commit history of more than one commit, with messages that state the change at that point in time (GitHub default "Update README.md" messages = 1 / 2)
- [ ] A merge commit in your GitHub history from another branch (a fast-forward, or a normal commit with "merge" in its message, does not count)
- [ ] More than the `main` branch is selectable in GitHub.  We can switch to the other branch and see content that may not be synced to `main`
- [ ] A `.gitignore` file in the repository's root folder that ignores a set of files (or a folder) and works

## Point Deductions

- [ ] (-20%) Submission not in course repository
- [ ] (up to -10%) Poor markdown formatting, scaled by severity (-10% = illegible / plain text with no structure)
    - includes assignment text left in the guide (instructions, `DEMONSTRATE` notes, Submission / Rubric sections) - 5% penalty
- [ ] (-10%) No Resources section / no sources cited (-5% if only partially provided, e.g. only an AI-use note)
- [ ] (-10% per day, up to 3 days) Late submission
- [ ] Submission appears AI-generated or describes work not done - score held at 0 pending an instructor meeting

Percentage deductions are taken from the total possible (e.g. 10% of 50.5 = 5.05).
