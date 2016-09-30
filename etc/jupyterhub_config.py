c.JupyterHub.base_url = '/'
c.JupyterHub.ssl_key = '/etc/ssl/private/idigbio.org.key'
c.JupyterHub.ssl_cert = '/etc/ssl/certs/idigbio.org.crt'
c.Application.log_level = 10

c.Authenticator.admin_users = {'nbird'}  # 'godfoder', 'mcollins'

c.JupyterHub.authenticator_class = 'jupyterhub.auth.PAMAuthenticator'
c.PAMAuthenticator.open_sessions = False

c.JupyterHub.spawner_class = 'sudospawner.SudoSpawner'
