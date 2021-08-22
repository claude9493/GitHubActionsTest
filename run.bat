@REM python .\src\get_weather.py
jupyter nbconvert --to notebook --execute ./src/vis_weather.ipynb --inplace
jupyter nbconvert --to HTML ./src/vis_weather.ipynb