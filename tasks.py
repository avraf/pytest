from invoke import task, run

@task(default=True)
def test(ctx, quiz=None):
    if quiz:
        run('nosetests --tests=test/test_quiz{}.py --with-specplugin'.format(quiz))
    else:
        run('nosetests --with-specplugin')
