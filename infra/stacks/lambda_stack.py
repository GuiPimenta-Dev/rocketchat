from functions.hello_world.config import HelloWorldConfig
from docs.config import DocsConfig
from aws_cdk import Stack
from constructs import Construct
from infra.services import Services

from lambda_forge.trackers import reset


@reset
class LambdaStack(Stack):
    def __init__(self, scope: Construct, context, **kwargs) -> None:

        super().__init__(scope, f"{context.name}-Lambda-Stack", **kwargs)

        self.services = Services(self, context)

        # Docs
        DocsConfig(self.services)

        # HelloWorld
        HelloWorldConfig(self.services)
