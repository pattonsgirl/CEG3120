## Project 5 Demonstration Rubric ( / 10)

Observe current state of site running on server, before making a change
- show the page in the browser
- show the docker status

1. [ ] making a change to the project file (from your local system)
2. [ ] `commit` and `push` of the change (from your local system)
3. [ ] `tag` the `commit` and `push` the `tag` (from your local system)
4. [ ] the GitHub Action triggering, relevant logs that it worked
5. [ ] DockerHub receiving a new set of tagged images (modified time should be visible)
6. [ ] Payload sent log from DockerHub or GitHub
7. [ ] status of `webhook` running as a service on the server
8. [ ] `webhook` logs that validate container refresh has been triggered
9. [ ] post-change state of site running on server
    - show the page in the browser
    - show the docker status
10. [ ] prove that hook has some trigger rule / protection in place