import aws_cdk as core
import aws_cdk.assertions as assertions

from scalable_django_channels.scalable_django_channels_stack import ScalableDjangoChannelsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in scalable_django_channels/scalable_django_channels_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ScalableDjangoChannelsStack(app, "scalable-django-channels")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
