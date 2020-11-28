from fabric import task


@task
def deploy(ctx):
    with ctx.cd("apps/django-sockpuppet-expo"):
        ctx.run('git pull')
        with ctx.prefix(". .env/bin/activate"):
            ctx.run('env')
