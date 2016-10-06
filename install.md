# Installation

## Initial package installation

    apt install npm nodejs nodejs-legacy pkg-config python2.7-dev python3.5-dev
    npm install -g configurable-http-proxy
    pip3 install jupyter jupyterhub sudospawner notebook matplotlib numpy pandas idigbio
    pip2 install matplotlib numpy ipykernel pandas idigbio
    ipython2 kernel install --name="Python 2" --display-name="Python 2"

## System configuraton

    salt-call state.sls spark
    salt-call state.sls hadoop

    BASE=/opt/guoda-jupyterhub-conf
    adduser --system --group --home /var/lib/jupyterhub --disabled-login jupyterhub
    # Allow the user to authenticate other users
    adduser jupyterhub shadow
    adduser jupyterhub ssl-cert
    adduser jupyterhub utmp
    cp $BASE/etc/sudoeqrs.d/jupyterhub /etc/sudoers.d/jupyterhub
    ln -s $BASE/etc/jupyterhub_config.py /etc/
    ln -s $BASE/etc/systemd/system/jupyterhub.service /etc/systemd/system/
    ln -s $BASE/usr/local/share/jupyter/kernels/* /usr/local/share/jupyter/kernels/
    systemctl daemon-reload


# Other Notes

## Adding users to the system


    adduser --gecos "" $USERNAME
    adduser $USERNAME jupyterhub


## Registering new kernels

[Kernel specs](http://jupyter-client.readthedocs.io/en/latest/kernels.html#kernelspecs)

From in a virtualenv

    pip install ipykernel
    ipython kernel install --user --name $NAME --display-name

### Spark kernels

* https://arnesund.com/2015/09/21/spark-cluster-on-openstack-with-multi-user-jupyter-notebook/
* https://github.com/ibm-et/spark-kernel/wiki/Getting-Started-with-the-Spark-Kernel
  * this points out that we should probably be setting the ENV: `"SPARK_CONFIGURATION": "spark.cores.max=4",`
