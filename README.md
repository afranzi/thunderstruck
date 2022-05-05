# Thunderstruck

![deploy](https://github.com/afranzi/thunderstruck/actions/workflows/ci-deploy.yml/badge.svg?branch=main)
![standard-checks](https://github.com/afranzi/thunderstruck/actions/workflows/ci-standard-checks.yml/badge.svg?branch=main)
![tests](https://github.com/afranzi/thunderstruck/actions/workflows/ci-test.yml/badge.svg?branch=main)

> `Thunderstruck` aims to simplify the CDP development by providing a modular approach to forward events into different 
> destinations.

## Local execution

> Start
````shell
ray start --head --port=6379 --dashboard-port=8265 # Start local Ray cluster.
serve start # Start Serve on the local Ray cluster.
python thunderstruck/dummy.py # Start our code
````

> Stop
````shell
serve shutdown
ray stop
````

## Roadmap

- [x] : Prepare skeleton & workflows.
- [ ] : Event ingest server
- [ ] : Event persistence in Postgres DB
- [ ] : K8s Helm.
- [ ] : Event Transformation + Forwarding with modules.