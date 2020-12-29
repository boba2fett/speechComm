sudo apt-get install python3-venv -y
python3 -m venv .
source bin/activate
sudo apt-get install bison libasound2-dev swig libpulse-dev -y
sudo apt-get install espeak ffmpeg libespeak1 -y
pip3 install pyaudio
pip3 install speechrecognition
pip3 install pocketsphinx
pip3 install pyttsx3
pip3 install colorama
mv lib/python3.9/site-packages/speech_recognition/pocketsphinx-data/en-US/pronounciation-dictionary.dict lib/python3.9/site-packages/speech_recognition/pocketsphinx-data/en-US/pronounciation-dictionary.dict.backup
python3 build.py