# create and activate your virtualenv - use format live|backup|dev plus the date
# for example, backup-14-05-22
virtualenv backup-14-05-22
cd backup-14-05-22
source bin/activate

# clone this project into the virtualenv
git clone git@github.com:evildmp/arkestra_medic.git

# install all the packages it needs
pip install -r arkestra_medic/requirements.txt

# don't forget to install the Arkestra packages that need to be installed from source
pip install -r src/arkestra/REQUIREMENTS.txt

# copy the database; give it the same name as the virtualenv

# copy (from an existing installation) and modify the secret settings file as required

# check that the database has the correct permissions for the user

# check that the runserver works
python arkestra_medic/manage.py runserver 0.0.0.0:8000

# gather the static media files ready to be served by the production webserver
python arkestra_medic/manage.py collectstatic -l

# edit the restart_fgci file so that it refers to the virtualenv name

# start the project
arkestra_medic/restart-fcgi start

# it may be necessary to install flup for the previous step to work
pip install flup

# edit the fcgi.conf (this is an nginx configuration) file:
#   change instances of /path/to/virtualenv to match the virtualenv's path
#   so that the upstream name matches that of the virtualenv
#   so that the list (i.e. port) and server_name values are correct

# add a line to /opt/nginx/conf/nginx.conf to include this configuration, for example:
#   include /home/daniele/backup-14-05-21/arkestra_medic/fastcgi.conf;

# restart nginx
sudo /etc/init.d/nginx restart

# copy the site's media files (uploaded and processed images and video and other 
# files) from the existing installation:
#   arkestra_medic/arkestra_medic/filer_public
#   arkestra_medic/arkestra_medic/filer_public_thumbnails
#   arkestra_medic/arkestra_medic/rendered_video

# edit the symplectic-scripts file to reflect the correct virtualenv name
