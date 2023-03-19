## What is Continuous Integration?

> In software engineering, continuous integration (**CI**) is the practice of merging all developers' working copies to a shared mainline several times a day. Nowadays it is typically implemented in such a way that it triggers an automated build with testing. - Wikipedia

- [Wikipedia - Continuous Integration](https://en.wikipedia.org/wiki/Continuous_integration)
- [AWS - Continuous Integration + Recommended Tools](https://aws.amazon.com/devops/continuous-integration/)

### What we need to combine

1. Developer changes
    - `git` - project tracking via versioning
2. Approved changes to the repo (for example, changes pushed to `main`)
    - git server / GitHub - central place to keep projects up to date across multiple developers
3. When a new image should be built
    - Docker - `Dockerfile` allows building of new images, copying project contents & updating packages for application environment

## Testing

To test something, you need to know the testing parameter based on your application

This starts to get into Software Engineering quick, so I'll leave some pointers about what to think about when it comes to testing and creating tests:
- [Real Python - Getting Started with Testing in Python](https://realpython.com/python-testing/)
- [Python Docs - Testing Your Code](https://docs.python-guide.org/writing/tests/)
- [Java Programming MOOC - Intro to Testing](https://java-programming.mooc.fi/part-6/3-introduction-to-testing)
- [Software Testing Help - Web Application Testing](https://www.softwaretestinghelp.com/web-application-testing/)
- [Snyk - code security checker](https://snyk.io/lp/static-analysis-snyk-code-checker)

## Linting

In general, **lint** is a static code analysis tool used to flag programming errors, bugs, stylistic errors and suspicious constructs.

*Most* linters zoom in on adherence to a Code Standard for the language or set of validation rules (best practices).

Just about [every language has a linter](https://github.com/caramelomartins/awesome-linters) (this list isn't complete, but is a great starting point)

Among the not listed is `ruff` a newer python linter that is storming through the community
- [GitHub - `ruff`](https://github.com/charliermarsh/ruff)

## git-hooks

Have your developers test and lint regularly is great, but if it's going to be standard practice, there should be no escaping the rules.

Situation:  
"I told Bob to not leave unused variables in his code!  I'm denying this Pull Request"

Instead of project managers shooting down code reviews, have a check in place that prevents going forward with a `push` or moving to a `Pull Request` by bringing it to the developer's attention.

`git` offers `hooks` - these are scripts set into the local repository that trigger when `git` commands are run.  It is most common to find `pre-commit` hooks.  This is a hook that would trigger when a `commit` is made, which could be used to test or lint code.  If the changes made in the `commit` pass some condition, then the `commit` can proceed.  Else the `commit` can be ignored until improvements are made.

`hooks` are a very basic way to implement `CI` (check code before a review) and `CD` (after `push`, `scp` code to a server)

Resources:
- [githooks.com](https://githooks.com/)
- [Awesome Git Hooks](https://github.com/aitemr/awesome-git-hooks)
    - [favorite for fun](https://github.com/lolcommits/lolcommits)
- [RedHat - git hooks examples](https://www.redhat.com/sysadmin/git-hooks)
- [pre-commit.com - framework for managing `pre-commit` hooks](https://pre-commit.com/)

## CI / CD Tools

Continuous Deployment (**CD**) is the post-integration.  The tools used for **CI** also handle **CD**.  This is just a list of tools so that you can see what realm they are a part of.

- [GitHub Actions](https://github.com/features/actions)
- [AWS Code Pipeline](https://aws.amazon.com/codepipeline/)
    - requires IAM tokens, which AWS Educate does not give clean access to
- [Jenkins](https://www.jenkins.io/)
- CI focus: 
    - [Travis CI](https://www.travis-ci.com/)
    - [Circle CI](https://circleci.com/)
- CD focus:
    - [Argo CD](https://argoproj.github.io/cd/)

Resources:
- [Scale Factory - Survey of CI / CD Tools 2022](https://www.scalefactory.com/blog/2022/11/24/a-survey-of-ci/cd-tools/)
