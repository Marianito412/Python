# File Sorter V2
file sorter v2 is a more customizable version of file sorter, it uses tags in the file name to find out the destination of files

## Usage
Flie Sorter V2 won't work out-of-the-box since sorter.json is setup with my file system so there are a couple things to be done before using it:

1. Setup sorter.json with the directories that you want your tags to redirect to, note that every tag dictionary has a key-value pair called "Index", this defines the order in which the paths will be appended.

2. Go to main.py and change the variable folder_to_track in both of it's instances to the path of the folder in which you will dump the files to be sorted.

Be very careful when assigning the index values since
```bash
/Users/Mariano/Desktop/Mariano/Documents/SEMESTRE 1 2020/APRECIACION DE CINE GR 3/Homework
```
Might be the directory you want but
```bash
Homework/Users/Mariano/Desktop/Mariano/Documents/SEMESTRE 1 2020/APRECIACION DE CINE GR 3
```
May not be the desired path

You will also need to be careful to use this order when writing the tags on the filename (ApC#Homework#File1.pdf is right but Homework#ApC#File1.pdf is not)

## Known Issues
1. Tags need to be assigned in the order of the indexes when naming the file otherwise the program crashes
2. Anything you found, I KNOW EVERYTHING!! (Just kndding, if you find some bug please let me know)

## Todo
1. Add config file for customizing things such as tag separator ("#" by default), or the folder_to_track
2. Add Gui application (this one is rather far away)
3. A bunch of things I will think of in the shower and then forget