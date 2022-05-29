ssh pi@widget05-pi

source venvs/PersonalServer/bin/activate

cd projects/PersonalServer/Webserver
export FLASK_APP=server
export FLASK_ENV=development
flask run --host=0.0.0.0

