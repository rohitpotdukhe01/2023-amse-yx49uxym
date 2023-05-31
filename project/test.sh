#!/bin/sh

## execute the pipeline.py
#echo "Execute of pipeline"
#python data/pipeline.py
#
## check if pipeline works properly
#echo "Check if pipeline works properly"
#pytest data/test.py
#

#echo "Pipeline execution started"
#python "$(dirname "$(dirname "$(realpath "$0")")")/data/pipeline.py"
#echo "Execution Completed"
#
#echo "Test started"
#python -m pytest "$(dirname "$(dirname "$(realpath "$0")")")/data/test.py"
#echo "Test ended"

# execute the pipeline
echo "Execute the pipeline"
python ../data/pipeline.py

# test of pipeline
echo "Test if pipeline works correctly"
pytest ../data/test.py