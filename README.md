# Welcome to Shrimp!Shrimp! TwTrip respository

## Development Guide

### Brief env setup Steps:
1. Git clone repo (ssh  git@github.com:TaiwanCodingShrimp/Auto_Stock_trading.git)
2. Install pyenv on your computer (ref: [Install and User guide for both windows/Mac](https://www.maxlist.xyz/2022/05/06/python-pyenv/)  ref: [Install for Windows](https://github.com/pyenv-win/pyenv-win))---pyenv install 3.10  (PS. And dont forhet to shell)
3. Install poetry on your computer (ref: [install on windows](https://tony0502.medium.com/poetry-%E5%AE%89%E8%A3%9D%E5%9C%A8windows-10-41d7263c13fe) ref:[install on Mac/Windows & User guide](https://www.maxlist.xyz/2022/05/08/python-poetry/#google_vignette))
4. Run "poetry install" to install the project and dependencies in the dir (PS. remember to shell)
5. Run "pre-commit install" to install pre-commit in hooks

> [!NOTE]
> Our dev python version is 3.10
>
>This is quite interseting, you should read abot this ---> [ Why using poetry but not just pip and container?](https://blog.kyomind.tw/python-poetry/)
>
> [More pyenv&poetry Guide](https://blog.kyomind.tw/poetry-pyenv-practical-tips/)
>
> ### About pre-commit
>ref: [ref](https://blog.kyomind.tw/pre-commit/)
>
> step1. "pre-commit install" (should make sure you have shell your poetry env)
>
> Step2. For usage. "pre-commit run --all-files"

## Basic GitFlow
### 處理新的issue，務必要開一個針對這個issue的分支，不要直接對master修改 !!! （This is vital)
#### Brief Steps:  (run in your terminal or cmd)
1. git checkout master (switch your local branch to master)
2. git pull (update your local master)
3. git checkout -b "輸入你的branch名字" (open a new branch and switch to it)
4. 開始你的更改
5. git add
6. git commit (記得run pre-commit)   如果有安裝好環境，跑commit就會執行了
7. git push
8. create your PR(Pull Request)
9. Request code review ！！！
11. After aproved ,Do "Squash merge "
> [!NOTE]
> ＧitFlow is very important !!!! Do follow it !!!
>
> Before merging PLEASE CHECK YOUR CODE THOROUGHLY !!!
>
> For more git details: 連結1-> [ref-多人協作](https://myapollo.com.tw/blog/git-tutorial-collaboration/)
      連結2-> [ref-git基本操作](https://medium.com/@flyotlin/%E6%96%B0%E6%89%8B%E4%B9%9F%E8%83%BD%E6%87%82%E7%9A%84git%E6%95%99%E5%AD%B8-c5dc0639dd9)
>
> pre-commit兩個方式：
> 安裝好自動會在git commit觸發 或是 可以手動執行 pre-commit run --all-files
