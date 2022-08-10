[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8146182&assignment_repo_type=AssignmentRepo)


Setting up Python virtual environment

```
$ python -m venv myENV
```
Activate the environment

```
$ source myENV/bin/activate
```

install flask and update pip

```
$ pip install flask
$ pip install --upgrade pip
```

manage packages installed:

```
$ pip freeze > requirements.txt
```

Later when you clone or start fresh, you can install packages:

```
$ pip install -r requirments.txt