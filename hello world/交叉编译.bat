:echo off 是关闭下面所有命令的显示，但会显示自身
@echo off

echo cmake不支持中文路径，该文件需要放到英文路径下运行
echo 切换到当前脚步所在的目录
cd  %~dp0

: cmake命令生成makefile文件,也可以用cmake-gui生成
: -B 指定编译文件的build目录，会在build目录生成makefile文件
: -S 指定CMakeLists.txt所在的目录
: -G指定generator，可选“Ninja”、“Visual Studio 16 2019”等
: -DCMAKE_TOOLCHAIN_FILE，指定工具链的配置文件tool.make，在其中配置编译器路径、库文件路径等
cmake -B %~sdp0build_cross -G "MinGW Makefiles" -DCMAKE_TOOLCHAIN_FILE="%~sdp0tool.make"

: 切换到makefile文件所在的目录执行编译命令
cd  %~sdp0build_cross
make

cmd /k echo.