# github-user-activity

A small command line tool I made to practice Python. You give it a GitHub username and it shows what that person did recently on GitHub (stars, pushes, new branches, forks).

I built it from the roadmap.sh project idea: https://roadmap.sh/projects/github-user-activity

## How to use it

You need Python 3. Nothing else to install.

    python github_activity.py Hasse94

Replace `Hasse94` with any GitHub username. You get something like this:

    - Starred anthropics/skills
    - Pushed to main in Hasse94/task-tracker-cli
    - Created a branch in Hasse94/task-tracker-cli

If the username doesn't exist, it tells you. Same if you forget to type one or you have no internet.

## Good to know

It uses GitHub's public events API, so it only shows recent stuff. Older activity is gone.

GitHub doesn't send the number of commits in a push anymore, so I show the branch name instead.