## Installation
This guide uses minishift version v1.33.0+ as the local Kubernetes cluster
and quay.io for the public registry. We also test on minikube version v0.35+.
`kubectl` is used but can be substituted* with `oc`.

### Supported versions
* [OKD](https://www.okd.io/)
  * Experimental: 3.11
* [OpenShift® Container Platform](https://www.openshift.com/products/container-platform/)
  * Fully supported: 4.0
  * Experimental: 3.11
* [kubernetes](https://kubernetes.io/)
  * Experimental: 1.11-1.13

Note: Experimental tag refers to some workloads that might be functioning

### Requirements
<!---
TODO(aakarsh):
Get the specific versions for requirements
-->

The main requirements are as follows:
* Running Kubernetes cluster - [supported versions](#Supported-Versions)
* [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
* [git](https://git-scm.com/downloads)

Note: Please login as admin user

The following requirements are needed to make/test changes to operator:
* [operator-sdk](https://github.com/operator-framework/operator-sdk)
* [docker](https://docs.docker.com/install/)

Note: You also require a [quay](https://quay.io/) account to push images

The following optional requirements are needed if using OKD/OCP < 4.0:
* [dep](https://golang.github.io/dep/docs/installation.html)
* [operator-sdk](https://github.com/operator-framework/operator-sdk)
* [go](https://golang.org/dl/)
* [OLM](https://github.com/operator-framework/operator-lifecycle-manager)

The workloads could also have their own requirements which would be specified
in the installation guide.

### Deploying operator

First we'll need to clone the operator:

```bash
# git clone https://github.com/cloud-bulldozer/cloud-builder
# cd cloud-builder
# export KUBECONFIG=<your_kube_config> # if not already done
```

We try to maintain all resources created/required by ripsaw in the namespace
ripsaw, so we'll create the namespace and add a context with admin user and
can be done as follows:

```bash
# kubectl apply -f resources/namespace.yaml
# kubectl config set-context builder-infra --namespace=builder-infra --cluster=<your_cluster_name> --user=<your_cluster_admin_user>
# kubectl config use-context builder-infra
```

We'll now apply the permissions and operator definitions.

```bash
# kubectl apply -f deploy
# kubectl apply -f resources/crds/infra_v1alpha1_builder_crd.yaml
# kubectl apply -f resources/operator.yaml
```


### Deploying Infra
Now that we've deployed our operator, follow infra specific instructions to
stand them up:
* [kafka](kafka.md)
* [postgres](postgres.md)
* [MongoDB](mongo.md)
* [couchbase](couchbase.md)

### Clean up
Now that we're running workloads we can cleanup by running following commands

```bash
# kubectl delete -f <your_cr_file>
# kubectl delete -f resources/crds/infra_v1alpha1_builder_crd.yaml
# kubectl delete -f resources/operator.yaml
# kubectl delete -f deploy
```
