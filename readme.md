# Git and GitHub Tutorial

This is a small, beginner-friendly exercise for learning how Git and GitHub support teamwork. The calculator is only an example. The main goal is to let two students make separate contributions and then combine those contributions into one working project.
This is a learning exercise, not a production calculator or a portfolio project. The Python code is intentionally simple so that students can focus on Git concepts instead of complicated syntax.
## The exercise
The team is building a calculator with two functions:
- Teammate one creates an addition function.
- Teammate two creates a subtraction function.
- The shared `main.py` file imports both functions and checks that the addition result is greater than the subtraction result.
For the example values, `a = 10` and `b = 5`. Because `b` is positive:
`a + b` is greater than `a - b`.
The check is a simple way to show that both teammates' work is available after the branches are combined. It is not intended to be a complete test of a calculator.


## Suggested Git workflow
1. Start with the same repository for both teammates.
2. Teammate one creates the addition function in `workbook_one/teammate_one/add.py`.
3. Teammate two creates the subtraction function in `workbook_one/teammate_two/subtract.py`.
4. Each teammate creates a branch, commits their work, and pushes the branch to GitHub.
5. Each teammate opens a pull request.
6. Review and merge both pull requests into the shared branch.
7. Run `main.py` after both contributions have been merged.
The exercise should demonstrate that each person can work independently while Git keeps a history of the work and GitHub provides a place to review and combine it.

## Repository guide
- `workbook_one/` contains the practical exercise.
- `workbook_one/main.py` is the shared integration check. Students should not modify it during the exercise.
- `workbook_one/teammate_one/what_to_do.md` contains teammate one's task.
- `workbook_one/teammate_two/what_to_do.md` contains teammate two's task.
- `dont_have_git.md` contains setup guidance for students who do not have Git installed.
- `.github/workflows/github_actions.yml` contains the GitHub Actions workflow for running the project check.
The check may fail before both teammate files exist. That is expected: the shared project is incomplete until both contributions have been added and merged.