:echo off �ǹر����������������ʾ��������ʾ����
@echo off

echo cmake��֧������·�������ļ���Ҫ�ŵ�Ӣ��·��������
echo �л�����ǰ�Ų����ڵ�Ŀ¼
cd  %~dp0

: cmake��������makefile�ļ�,Ҳ������cmake-gui����
: -B ָ�������ļ���buildĿ¼������buildĿ¼����makefile�ļ�
: -S ָ��CMakeLists.txt���ڵ�Ŀ¼
: -Gָ��generator����ѡ��Ninja������Visual Studio 16 2019����
cmake -B %~sdp0build_mingw -G "MinGW Makefiles"

: �л���makefile�ļ����ڵ�Ŀ¼ִ�б�������
cd  %~sdp0build_mingw
make

cmd /k echo.