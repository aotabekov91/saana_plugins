from plug import Plug

class Normal(Plug):

    def setup(self):

        super().setup()
        self.current=None

    def setMode(self, mode):
        raise
        self.current=mode
        print(self.current)

    def handle(self, request):
        print(request)
