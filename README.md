# How To Use for developpement purpose:
1. Install the python environnement
`conda env create -f environment.yml`

2. Activate the environnement
`conda activate histo`

3. Install additionnal non-conda and non-pip package in the conda environnement (Deepzoom.py)
```
cd ..
git clone https://github.com/openzoom/deepzoom.py.git
cd deepzoom.py
python setup.py install
```

4. Launch the app
`python main.py`

5. Go to [127.0.0.1:5011/](http://127.0.0.1:5010/) in your web-browser and upload your first histology image.

# How to build to deploy:

### On Linux:
1. Clone this repo and activate the environnement
 
2. Using pysintaller run the following command (might be long as it runs in the onefile mode (-F) instaed of one-dir (-D)):
```pyinstaller --clean -F -n HISTOANNOT --add-data 'src:src' main.py```

1. Copy Paste config, results, static and templates folder inside your new folder that should have appeared called dist

2. You can now run the application using ./HISTOANNOT file in the dist folder

### On Windows (untested):
1. Repeat the same steps except you replace the ":" in the pyinstaller command by ";" such as:
```pyinstaller --clean -F -n HISTOANNOT --add-data 'src;src' main.py```