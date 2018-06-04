#!/bin/bash

git clone https://github.com/Morfeu5z/llapCloudFlask.git /server/
gcc -Wall -o /server/static/tool/Binary/cpuController /server/static/tool/Binary/Test.c
python3 /server/PipelineMachine.py -i 0.0.0.0 -p 5000
/bin/bash