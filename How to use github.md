# How to use GitHub or BitBucket

## Create new repo <Test>
follow each site instruction

## clone this repo in your private computer
    # github (default is public repo)
    git clone https://github.com/sastation/Test.git

    # bitbucket (default is private repo)
    git clone https://sastation@bitbucket.org/sastation/Test.git

## add new file and then pull it
    cd Test
    touch test.txt
    git add test.txt
    git commit -m "add text.txt"
    git -u pull origin master

## add all files after you do something
    cd Test
    git add .
    git commit -m "add for function A"
    git -u pull origin master
