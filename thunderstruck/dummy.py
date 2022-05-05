import ray
from fastapi import FastAPI
from ray import serve

app = FastAPI()

ray.init(address="auto", namespace="thunder")
serve.start(detached=True)


@ray.remote
class Forwarder:

    @ray.method(num_returns=1)
    def send(self, item: dict):
        print(item)
        return 1


@serve.deployment(route_prefix="/")
@serve.ingress(app)
class Ingest:



    @app.get("/batch")
    def method(self):
        return "Hello 1!"

    @app.post("/batch")
    def get_summary(self, event: dict):
        forwarder = Forwarder.remote()
        result = ray.get(forwarder.send.remote(event))
        print(f'Result {event}')
        return {'event': event, 'result': result}


Ingest.deploy()
