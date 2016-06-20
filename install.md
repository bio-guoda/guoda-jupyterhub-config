# Installation

## Initial package installation

    apt install npm nodejs nodejs-legacy pkg-config python2.7-dev python3.5-dev
    npm install -g configurable-http-proxy
    pip3 install jupyter jupyterhub sudospawner notebook matplotlib numpy pandas idigbio
    pip2 install matplotlib numpy ipykernel pandas idigbio
    ipython2 kernel install --name="Python 2" --display-name="Python 2"

## System configuraton

    BASE=/opt/guoda-jupyterhub-conf
    adduser --system --group --home /var/lib/jupyterhub --disabled-login jupyterhub
    # Allow the user to authenticate other users
    adduser jupyterhub shadow
    cp $BASE/etc/sudoers.d/jupyterhub /etc/sudoers.d/jupyterhub
    ln -s $BASE/etc/jupyterhub_config.py /etc/
    ln -s $BASE/etc/systemd/system/jupyterhub.service /etc/systemd/system/
    systemctl daemon-reload


## Spark configuration

    salt-call state.sls spark saltenv=prod

# Other Notes

## Adding users to the system


    adduser --gecos "" $USERNAME
    adduser $USERNAME jupyterhub



## Registering new kernels

[Kernel specs](http://jupyter-client.readthedocs.io/en/latest/kernels.html#kernelspecs)

From in a virtualenv

    pip install ipykernel
    ipython kernel install --user --name $NAME --display-name
