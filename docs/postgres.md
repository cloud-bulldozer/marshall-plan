# Postgres

[PostgreSQL](https://www.postgresql.org/), also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and technical standards compliance

## Using the Postgres Infra

### Pre-requisites
MongoDB uses volumeClaimTemplates to request volumes, thus you'll need to create a storageclass. Creating a storageclass
is outside the scope of this documentation.

### Customizing your CR

An example to enable only the Postgres infra (this does _not_ run a workload):

```yaml
apiVersion: builder.cloudbulldozer.io/v1alpha1
kind: Infra
metadata:
  name: postgres-infra
  namespace: builder-infra
spec:
  infrastructure:
    name: postgres
    args:
      clusters: 1 # number of postgres clusters
      cluster_size: 3 # number of pods per postgres cluster
      #storageclass: # uses the sc with the annotation storageclass.kubernetes.io/is-default-class: "true" if the option is not specified or commented
      storagesize: 10Gi # default value if option not specified
      port: 5432 # default value if option not specified
```

Additionally if you'd like to use a specific postgres image tag, you can add another field args.postgres and set it to the tag. tag defaults to 10.4.

### Starting the Infra
Once you are finished creating/editing the custom resource file and the infra operator is running, you can start the infra with:

```bash
$ kubectl apply -f /path/to/cr.yaml
```

You can then check if mongo pods are created as follows

```bash
$ kubectl get pods -l "role=postgres"
NAME      READY   STATUS    RESTARTS   AGE
postgres0-0   1/1     Running   0          51s
```

The connection string URI for the first cluster would be postgres0-0.postgres0.builder-infra.svc.cluster.local:5432 and for second cluster it would be postgres1-0.postgres1.builder-infra.svc.cluster.local:27017
