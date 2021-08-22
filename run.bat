python .\src\get_weather.py
jupyter nbconvert --to notebook --execute ./src/vis_weather.ipynb --inplace
jupyter nbconvert --output-dir='./' --output='index.html' ./src/vis_weather.ipynb
