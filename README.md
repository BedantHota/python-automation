# python-automation
OraganizeIt organizes your files in certain folders

# OrganizeIt

This package organizes your files into certain folders.
E.g You can use it with your 'Downloads' folder to organize you images, documents, .exe files , .etc.

## Installation
Check whether you are running latest package manager [pip](https://pip.pypa.io/en/stable/)<br>
`pip --version`
<br><br>
Upgrade your pip version (If not using the latest one)<br>
`pip install --user --upgrade pip`
<br><br>
Install `organizeit`  :
`pip install organizeit`
<br><br>
<br>
## Usage

Import installed package and OS module :
```
import os
import organizeit
```
Create an array of the names of the folders you want :
```
FOLDERS_NAME = ['Images', 'Music', 'Videos', 'Applications', 'Documents', 'Others']
```
Create a variable called `path` and store the path of the folder you want the files inside which to be organized.  

```
path = os.path.expanduser('E:\\XYZ\\Downloads')
```

Now, pass the `FOLDERS_NAME` array and the path to the `createFolders` function.

```
createFolder(FOLDERS_NAME, path)
```
The `createFolders()` function will create all new folders within the array passed.

Next, we have to use the `insertFiles()` function by passing the path to the function.

```
insertFiles(path)
```

The `insertFiles()` function loops through every file in that folders and checks for their extension and on the basis of the type of file it is.

Note: The current version can only sort your files in folders -> Images, Videos, Documents, Applications, Music only so you can't create a dynamic folder with a custom name. But, in later versions there will be an upgrade.

Thank You!  
