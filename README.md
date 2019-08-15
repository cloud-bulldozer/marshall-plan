# Infra Operator

The intent of this Operator is to deploy common Infra required to run workloads against
a performance baseline of Kubernetes cluster on your provider.

## Infrastructure status

| Workload                                       | Deployment  Strategy  | Status in Operator |
| ---------------------------------------------- | --------------------  | ------------------ |
| [Couchbase](docs/couchbase.md)                 | Couchbase Operator    | Working            |
| [MongoDB](docs/mongo.md)                       | Statefulset/Service   | Working            |
| [Postgres](docs/postgres.md)                   | Statefulset/Service   | Working            |
| [Kafka](docs/kafka.md)                         | Strimzi Operator      | Working            |
| [Postgres-Zalando](docs/postgres-zalando.md)   | Zalando Operator      | Working            |


## Installation
[Installation](docs/installation.md)

## Contributing
Please submit a PR

## Community
Key Members(slack_usernames): aakarsh, dblack or rook
* [**#sig-scalability on Kubernetes Slack**](https://kubernetes.slack.com)
* [**#forum-kni-perfscale on CoreOS Slack**](https://coreos.slack.com)
