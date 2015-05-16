#!/bin/bash
RUTAPRO=/home/anthonywainer/miproyecto/estudiodjango1.8/proyecto_avanzado/                       #ruta donde se encuentra almacenado tu proyecto
NAME="sisjuridico"                                   #Name of the application (*)
DJANGODIR=${RUTAPRO}sisjuridico                                # Django project directory (*)
SOCKFILE=${RUTAPRO}run/gunicorn.sock        # we will communicate using this unix socket (*)
USER=anthonywainer                                        # the user to run as (*)
GROUP=anthonywainer                                     # the group to run as (*)
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=sisjuridico.settings.local             # which settings file should Django use (*)
DJANGO_WSGI_MODULE=sisjuridico.wsgi                     # WSGI module name (*)

echo "Iniciando proyecto $NAME como `whoami`"

# Activate the virtual environment
# source /opt/myenv/bin/activate
cd $DJANGODIR
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
#exec /opt/myenv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE