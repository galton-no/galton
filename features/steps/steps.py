from behave import step
import pexpect


@step('I run "{command}"')
def step_impl(context, command):
    context.child = pexpect.spawn(command, encoding='utf-8')


@step('I see "{output}"')
def step_impl(context, output):
    context.child.expect(output)
