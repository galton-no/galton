from behave import step


@step('I run "{command}"')
def step_impl(context, command):
    raise NotImplementedError(u'STEP: When I run "python manage.py check"')


@step('I see "{output}"')
def step_impl(context, output):
    raise NotImplementedError(u'STEP: Then I should see "System check identified no issues (1 silenced)."')
