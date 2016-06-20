
npm-packages:
  pkg.installed:
    - pkgs:
        - npm
        - nodejs
        - nodejs-legacy
        - pkg-config
        - python2.7-dev
        - python3.5-dev

configurable-http-proxy:
  npm.installed:
    - requires:
        - pkg: npm-packages

pip-packages:
  pip.installed:
    - bin_env: /usr/local/bin/pip3
    - pkgs:
        -
