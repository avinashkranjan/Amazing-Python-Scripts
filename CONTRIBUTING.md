# Contributing Guidelines

This documentation contains a set of guidelines to help you during the contribution process. 
We are happy to welcome all the contributions from anyone willing to improve/add new scripts to this project. Thank you for helping out and remember,
**no contribution is too small.**

# Submitting Contributions👩‍💻👨‍💻
Below you will find the process and workflow used to review and merge your changes.
## Step 1 : Find an issue
- Take a look at the Existing Issues or create your **own** Issues!
- Wait for the Issue to be assigned to you after which you can start working on it.
- Note : Every change in this project should/must have an associated issue. 

![Screenshot (190)](https://user-images.githubusercontent.com/55796944/92216403-e1055080-eeb3-11ea-95f6-1b95b90813f5.jpg)

## Step 2 : Fork the Project
- Fork this Repository. This will create a Local Copy of this Repository on your Github Profile. Keep a reference to the original project in `upstream` remote.
```
$ git clone https://github.com/<your-username>/Amazing-Python-Scripts
$ cd Amazing-Python-Scripts
$ git remote add upstream https://github.com/avinashkranjan/Amazing-Python-Scripts
```
![Screenshot (191)](https://user-images.githubusercontent.com/55796944/92216605-23c72880-eeb4-11ea-9b89-e15e0a1f254d.jpg)


- If you have already forked the project, update your copy before working.
```
$ git remote update
$ git checkout <branch-name>
$ git rebase upstream/<branch-name>
```
## Step 3 : Branch
Create a new branch. Use its name to identify the issue your addressing.
```
# It will create a new branch with name Branch_Name and switch to that branch 
$ git checkout -b branch_name
```
## Step 4 : Work on the issue assigned
- Work on the issue(s) assigned to you. 
- Add all the files/folders needed.
- After you've made changes or made your contribution to the project add changes to the branch you've just created by:
```
# To add all new files to branch Branch_Name
$ git add .
```
## Step 5 : Commit
- To commit give a descriptive message for the convenience of reveiwer by:
```
# This message get associated with all files you have changed
$ git commit -m "message"
```
- **NOTE**: A PR should have only one commit. Multiple commits should be squashed.
## Step 6 : Work Remotely
- Now you are ready to push your work to the remote repository.
- Once your work is ready and adheres to the project conventions, upload your changes to your fork:

```
# To push your work to your remote repository
$ git push -u origin Branch_Name
```

## Step 7 : Pull Request
- Go to your repository in browser and click on compare and pull requests. Then add a title and description to your pull request that explains your contribution.

- Voila! Your Pull Request has been submitted and will be reviewed by the moderators and merged.🥳

## Need more help?🤔
You can refer to the following articles on basics of Git and Github and also contact the Project Mentors, in case you are stuck:
- [Forking a Repo](https://help.github.com/en/github/getting-started-with-github/fork-a-repo)
- [Cloning a Repo](https://help.github.com/en/desktop/contributing-to-projects/creating-an-issue-or-pull-request)
- [How to create a Pull Request](https://opensource.com/article/19/7/create-pull-request-github)
- [Getting started with Git and GitHub](https://towardsdatascience.com/getting-started-with-git-and-github-6fcd0f2d4ac6)
- [Learn GitHub from Scratch](https://lab.github.com/githubtraining/introduction-to-github)


## Tip from us😇
It always takes time to understand and learn. So, do not worry at all. We know **you have got this**!💪
