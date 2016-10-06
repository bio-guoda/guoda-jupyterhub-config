import os

c.JupyterHub.base_url = '/'
c.JupyterHub.ssl_key = '/etc/ssl/private/idigbio.org.key'
c.JupyterHub.ssl_cert = '/etc/ssl/certs/idigbio.org.crt'
c.Application.log_level = 10


c.Authenticator.create_system_users = True
c.Authenticator.admin_users = {'unwashedmeme', 'godfoder', 'mjcollin'}
c.Authenticator.add_user_cmd = [
    'sudo', 'adduser', '-q', '--gecos', '""', '--disabled-password', '--ingroup', 'jupyterhub'
]
c.JupyterHub.authenticator_class = 'oauthenticator.LocalGitHubOAuthenticator'
#c.JupyterHub.authenticator_class = 'jupyterhub.auth.PAMAuthenticator'

c.GitHubOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']
c.GitHubOAuthenticator.client_id = os.environ['GITHUB_CLIENT_ID']
c.GitHubOAuthenticator.client_secret = os.environ['GITHUB_CLIENT_SECRET']


c.JupyterHub.spawner_class = 'sudospawner.SudoSpawner'
