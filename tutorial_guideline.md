# Git and GitHub Tutorial Guideline

## Phase 1: Explain the concept of Git
This is the most important part of the session. Start by helping the audience understand what Git is and why it matters.

Focus on the core ideas:
- Git stores different versions of your code.
- It keeps a history of changes so work can be reviewed and restored if needed.
- It supports collaboration between individuals, teams, and projects.
- GitHub provides an online platform for hosting repositories and working together remotely.

Use simple examples to explain these ideas clearly. For instance, explain that if a file is edited incorrectly, Git allows you to revisit an earlier version instead of losing progress.

## Phase 2: Install Git
If the audience is using Windows, guide them through installing Git from the official website.

Explain the basics:
- Download Git for Windows.
- Run the installer.
- Accept the default settings unless there is a specific reason to change them.
- Open Git Bash or the terminal and confirm the installation using `git --version`.

## Phase 3: Introduce the GitHub basics
Make it clear that this is a beginner-friendly Git/GitHub tutorial. The goal is not to cover everything, but to help learners understand the fundamentals and build confidence through practice.

Explain that after this session, they should continue experimenting with Git on their own so they can become more comfortable with the workflow.

## Phase 4: Practice the basics locally
Now move into a practical exercise.

Teach the audience to:
1. Install Git on their system.
2. Create a new folder for a simple repository.
3. Run `git init` to initialize the repository.
4. Create a text file with their name in it.
5. Use `git add` to stage the file.
6. Use `git commit -m "message"` to save the change.

Make sure to explain what each command does in simple language.

## Phase 5: Explain GitHub as the remote platform
After the local Git practice, introduce GitHub as the online location where code can be stored and shared.

Explain the difference between:
- the local machine, where work is done,
- and the GitHub repository, where the code is stored remotely.

Then show them how to:
- create a new repository on GitHub,
- connect it to the local project,
- push the local repository to GitHub,
- and view the code online.

## Phase 6: Work with branches in the project
Next, move into the real tutorial repository.

Explain the concept of branches simply:
- A branch lets you work on a feature or task without affecting the main project.
- Different people can work independently on their own branch.
- Once the work is complete, the branch can be merged into the main project.

Show them how to:
1. Clone the main `git-github` tutorial repository.
2. Create a new branch.
3. Work on their assigned task.
4. Commit the change.
5. Push the branch to GitHub.
6. Open a pull request.(explain git merging here )

## Phase 7: Show the project check and GitHub Actions
Once the task is complete, show the GitHub Actions message or prompt that indicates the solution passed.

This is a good opportunity to explain that GitHub can run checks automatically, which helps confirm that the project is working as expected.

## Phase 8: End with an assignment
Close the session by telling the audience to apply the same workflow in a small assignment.

Encourage them to do the project again with a teammate:
- create separate branches,
- add their own contribution,
- commit and push their work,
- open a pull request,
- and merge the changes together.

This reinforces the basic Git and GitHub collaboration workflow in a practical and realistic way.