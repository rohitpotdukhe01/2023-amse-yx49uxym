#!/bin/sh

# execute the pipeline.py
echo "Execute of pipeline"
python /Users/rohitpotdukhe/PycharmProjects/2023-amse-yx49uxym/data/pipeline.py

# check if pipeline works properly
echo "Check if pipeline works properly"
pytest /Users/rohitpotdukhe/PycharmProjects/2023-amse-yx49uxym/data/test.py

