from fabric import task
from invoke import run as local
from patchwork.transfers import rsync


exclude_dirs = [".git", "node_modules", ".cache", ".github", "db.sqlite3"]


@task
def deploy(ctx):
    local("yarn build", echo=True)
    local("python manage.py collectstatic --noinput", echo=True)
    rsync(ctx, "static/", "apps/django-sockpuppet-expo/static/",
          exclude=exclude_dirs)
    with ctx.cd("~/apps/django-sockpuppet-expo"):
        ctx.run('git pull')
        with ctx.prefix("source .env/bin/activate"):
            ctx.run('python -m pip install --upgrade -r requirements.in')
            ctx.run('python manage.py migrate')
    ctx.run("sudo supervisorctl restart expo:*")
