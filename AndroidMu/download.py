#!/usr/bin/python
#coding=utf-8

import xml.dom.minidom
import os
from subprocess import call

import subprocess
import sys

# 1. 修改为源码要保存的路径
rootdir = sys.argv[1]
  
# 2. 设置 git 安装的路径
git = "/usr/bin/git"
 
# 3. 修改为第一步中 manifest 中 default.xml 保存的路径
dom = xml.dom.minidom.parse(sys.argv[2])
root = dom.documentElement
  
#prefix = git + " clone https://android.googlesource.com/"
prefix = git + " clone https://aosp.tuna.tsinghua.edu.cn/"
# 4. 没有梯子使用清华源下载
# prefix = git + " clone https://aosp.tuna.tsinghua.edu.cn/"
suffix = ".git" 

def runCommandWait(cmd):
    print "\trun_command:[", cmd, ']'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
    out, err = p.communicate()
    return p.returncode, out, err
 
if not os.path.exists(rootdir): 
    os.mkdir(rootdir) 

codeArry=['frameworks/base','libcore']
 
for node in root.getElementsByTagName("project"): 
    os.chdir(rootdir) 
    d = node.getAttribute("path")
    if d not in codeArry:
        continue

    last = d.rfind("/")
    if last != -1: 
        d = rootdir + "/" + d[:last] 
        if not os.path.exists(d): 
            os.makedirs(d) 
        os.chdir(d) 
    cmd = prefix + node.getAttribute("name") + suffix
    path = rootdir + "/" + node.getAttribute("path")
    print cmd ," ",path
    runCommandWait(cmd + " "+path)
    #call(cmd)
