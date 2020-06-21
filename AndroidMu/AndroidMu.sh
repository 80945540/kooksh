#!/bin/sh

AndoirdSourceDir='/home/kook/AndroidSource/'
AndroidAlpsRootDir=('/home/kook/AndroidSource/AndroidQ' '/home/kook/AndroidSource/AndroidPie')    #要查找android 版本的源码
AndroidFwkAttention=('/frameworks/base' '/libcore' ) #fwk 关注的代码目录

AndroidVersion=('android-5.0.0_r1' 'android-6.0.0_r1' 'android-7.0.0_r1' 'android-8.0.0_r1' 'android-9.0.0_r1' 'android-q-preview-1')
function print_help {
    cat <<EOF
  1，该功能可以在指定路面下查找到对应文件中对应的字符串，根据自己的需求在后面加上自己对应的参数
        -- params 1  文件名字
        -- params 2  文件里面的属性字符串
  2，该脚本可以下载 android 原始代码
EOF
}

if [ $# -eq 2 ]; then
   findfile=$1
   findfilestr=$2
   #echo "find file ",$findfile,"  file string ",$findfilestr #查看查找文件以及需要的 字符串

   for ((i=0;i<${#AndroidVersion[@]};i+=1));do
       for((j=0;j<${#AndroidFwkAttention[@]};j+=1));do
           targetPath=$AndoirdSourceDir${AndroidVersion[$i]}${AndroidFwkAttention[$j]}
           #echo $targetPath     $findfile
           targetFiles=$(find $targetPath -name $findfile) #在目标目录下查找 需要的文件
           #echo $targetFiles
           targetFile=(${targetFiles// /}) # 拿到文件列表字符串分割成数组
           for ((k=0;k<${#targetFile[@]};k+=1));do
              #echo "找到文件" ${targetFile[$k]}
              tarStr=$(grep $findfilestr ${targetFile[$k]})
              echo "在文件 ${targetFile[$k]}找到字符串 $findfilestr"
           done
       done
   done
else
    echo "$@" | grep -wq "clone" &&  clone=1
    if [ $clone -eq 1 ];then
        git clone https://aosp.tuna.tsinghua.edu.cn/platform/manifest.git manifest
        cd manifest
        for ((i=0;i<${#AndroidVersion[@]};i+=1));do
            git co ${AndroidVersion[$i]}
            defaultPath=$(pwd)/default.xml
            currtRootdir=$AndoirdSourceDir/${AndroidVersion[$i]}
            if [ -d $modulePath  ];then
                echo ""
            else
                mkdir $currtRootdir
            fi
            python ../download.py $currtRootdir $defaultPath
        done
    else
        print_help
    fi
fi