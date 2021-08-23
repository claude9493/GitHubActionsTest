python .\src\get_weather.py
jupyter nbconvert --to notebook --execute ./src/vis_weather.ipynb --inplace
jupyter nbconvert --TemplateExporter.exclude_input=True ./src/vis_weather.ipynb --output-dir='./' --output='index.html' 
