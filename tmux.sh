#!/bin/bash
#
# tumx启动脚本

# 兼容zsh
export DISABLE_AUTO_TITLE="true"
session="Main"
tmux has-session -t $session
if [ $? = 0 ];then
    tmux attach-session -t $session
    exit
fi

tmux new-session -d -s $session -n home
tmux send-keys -t $session:0 'cd ~' C-m
tmux new-window -t $session:1 zsh 
tmux new-window -t $session:2 zsh 
tmux new-window -t $session:3 zsh
tmux select-window -t $session:1
tmux attach-session -t $session

# tmux new-window -t $session:1 -n runtime zsh 
# tmux split-window -t $session:3 -v
