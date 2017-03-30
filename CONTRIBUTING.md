# Contributing 

1. Fork the repo, create a new branch, develop and test your code changes.
2. Make sure that your commit messages clearly describe the changes.
3. Send a pull request. 
4. Thank you for your contribution.

## Here are some guidelines

You'll have to create a development environment to hack on Code-Fight, using a Git checkout:

* While logged into your GitHub account, navigate to the Code-Fight repo on Github.
https://github.com/TaiwanSparkUserGroup/Code-Fight

* Fork and clone the repository to your GitHub account by clicking the "Fork" button.

* Clone your fork of repo from your GitHub account to your local computer, substituting your account username E.g.:

```
$ cd ~
$ git clone git@github.com:USERNAME/Code-Fight
$ cd Code-Fight
# Configure remotes such that you can pull changes from the Code-Fight
# repository into your local repository.
$ git remote add upstream https://github.com/TaiwanSparkUserGroup/Code-Fight
# fetch and merge changes from upstream into master
$ git fetch upstream
$ git merge upstream/master
```

Now your local repo is set up such that you will push changes to your GitHub repo, from which you can submit a pull request.

* Create a virtualenv in which to install gcloud-python:

```
$ cd ~/Code-Fight
$ virtualenv -python2.7 env
```

Now you can install packages you need.

* Create a new branch for each pull request

```
$ cd ~/Code-Fight
$ git checkout -b new_branch
```

* Before pull request...

Please check every unittests are passed.

```
$ cd ~/Code-Fight
$ nosetests
```

* Now you can commit and pull request

```
$ cd ~/Code-Fight
$ git commit -m "what you do in this commit"
$ git push origin your_branch
```

After pushing the commit, you can go to your repo on Github and see a new button called `compare & pull requst`.
Press it and describe this PR in the text box and we'll review your PR.
If it is ok, we'll merge your PR with the master branch.
