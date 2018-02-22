#!/bin/bash
#set -x
export BASENAME=lanz2inf
export BASEDIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export pidfile=${BASEDIR}/${BASENAME}.pid

# point to locally installed python modules
export PYTHONPATH=${BASEDIR}/Lib/site-packages/:/opt/exchange/Python/lib/python2.7/site-packages:${PYTHONPATH}

# python script to execute
if [ -z ${PYTHONEXE+x} ]
then
    PYTHONEXE="python ${BASEDIR}/kfk2inf/kfk2inf.py"
fi

function log() {
    printf "%.23s %s[%s]: %s\n" $(date +%F.%T.%N) ${BASH_SOURCE[1]##*/} ${BASH_LINENO[0]} "${@}";
}

log "Starting ${BASENAME} ..."
if [ -f $pidfile ]
then
    pid=`cat $pidfile`
    if ps $pid > /dev/null
    then
        log "${BASENAME} already started"
        exit 1
    fi
    # pid file is out-of-date
    rm "$pidfile"
fi
exec ${PYTHONEXE} "$@" -c lanz2inf_config.yaml --pidfile $pidfile &
