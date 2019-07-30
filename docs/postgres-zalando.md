# PostgreSQL

[PostgreSQL](https://www.postgresql.org/) is an open source object-relational database system.

## Prerequisites
### OLM
The [Operator Lifecycle Manager (OLM)](https://github.com/operator-framework/operator-lifecycle-manager/blob/master/Documentation/install/install.md) is required to run the [Zalando PostgreSQL operator](https://github.com/zalando/postgres-operator) from [operatorhub.io](https://operatorhub.io). If your distribution of OpenShift/Kubernetes does not include this, you will need to install it first.

```bash
$ kubectl apply -f https://raw.githubusercontent.com/operator-framework/operator-lifecycle-manager/master/deploy/upstream/quickstart/crds.yaml
$ kubectl apply -f https://raw.githubusercontent.com/operator-framework/operator-lifecycle-manager/master/deploy/upstream/quickstart/olm.yaml
```

## Using the Postgres Infra

### Customizing your CR

An example to enable only the Postgres infra (this does _not_ run a workload):

```yaml
apiVersion: builder.cloudbulldozer.io/v1alpha1
kind: Infra
metadata:
  name: postgres-zalando
  namespace: builder-infra
spec:
  infrastructure:
    name: postgres-zalando
    args:
      servers:
        # Typical deployment size is 3
        size: 1
      storage:
        # persistent storage volume is required
        class_name: "standard"
        volume_size: 1G
      deployment:
        # These are deployment defaults from roles/postgres-infra/defaults
        # that can be overridden here.
        #
        ## For Generic K8s w/ Upstream OLM
        #postgres_operator_package: "postgres-operator"
        #olm_catalog: operatorhubio-catalog
        #olm_namespace: olm
        #
        ## For OpenShift v3 w/ Upstream OLM
        #postgres_operator_package: TODO
        #olm_catalog: TODO
        #olm_namespace: TODO
        #
        ## For OpenShift v4 w/ Built-In OLM
        #postgres_operator_package: "postgres-operator"
        #olm_catalog: operatorhubio-catalog
        #olm_namespace: openshift-operator-lifecycle-manager
```

**Please see the example [CR file](../resources/crds/infra_v1alpha1_postgres_zalando_cr.yaml) for further examples for different deployment environments.**

### Persistent Storage
If you set `spec.infrastructure.args.stroage.use_persistent_storage` to `true`, then you will need to provide a valid
StorageClass name for `spec.infrastructure.args.storage.class_name`

A valid volume size for `spec.infrastructure.args.storage.volume_size` is required whether or not you enable persistent storage.

*Setting up a StorageClass is outside the scope of this documentation.*

### Starting the Infra
Once you are finished creating/editing the custom resource file and the infra operator is running, you can start the infra with:

```bash
$ kubectl apply -f /path/to/cr.yaml
```

Deploying the above will first result in the postgres operator running.

```bash
$ kubectl get pods -l name=postgres-operator
NAME                                  READY     STATUS    RESTARTS   AGE
postgres-operator-7b489f685c-j6vs8   1/1       Running   0          4m59s
```

Once the postgres operator is running, the benchmark operator will then launch the postgres
server infrastructure in a stateful manner.

```bash
$ kubectl get pods -l spilo-role=master
NAME                                  READY     STATUS    RESTARTS   AGE
infra-postgres-cluster-0             1/1       Running   0          9m58s
```
