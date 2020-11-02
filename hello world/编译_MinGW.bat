:echo off 是关闭下面所有命令的显示，但会显示自身
@echo off

echo cmake不支持中文路径，该文件需要放到英文路径下运行
echo 切换到当前脚步所在的目录
cd  %~dp0

: cmake命令生成makefile文件,也可以用cmake-gui生成
: -B 指定编译文件的build目录，会在build目录生成makefile文件
: -S 指定CMakeLists.txt所在的目录
: -G指定generator，可选“Ninja”、“Visual Studio 16 2019”等
cmake -B %~sdp0build_mingw -G "MinGW Makefiles"

: 切换到makefile文件所在的目录执行编译命令
cd  %~sdp0build_mingw
make

cmd /k echo.