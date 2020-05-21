# handWritingToText

* Little app that tries to read your writing
	
## Demo

![](output.gif)

## Install prerequisites

```
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
```

## How to use

```
git clone https://github.com/nomspls/handWritingToText.git
pip install -r requirements.txt
```
* For python 3.8+ use:

```
pip install kivy[base] kivy_examples --pre --extra-index-url https://kivy.org/downloads/simple/ 
```

* For python 3.7 and lower use:

```
pip install kivy
```

* Launch:

```
cd handWritingToText
python WordReader.py   # or python3 WordReader.py
```

## Built with

* Python 3.7
