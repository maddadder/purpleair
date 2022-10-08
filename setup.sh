cd /home/alice/git3/purpleair
python3 -m venv ./env
source env/bin/activate
pip install -r requirements.txt

cd /home/alice/git3/purpleair
source env/bin/activate

python remoteSensor.py
