# MongoDB

[MongoDB](https://www.mongodb.com/) is a document-based, distributed database

## Using the MongoDB Infra

### Pre-requisites
MongoDB uses volumeClaimTemplates to request volumes, thus you'll need to create a storageclass. Creating a storageclass
is outside the scope of this documentation.

### Customizing your CR

An example to enable only the MongoDB infra (this does _not_ run a workload):

```yaml
apiVersion: builder.cloudbulldozer.io/v1alpha1
kind: Infra
metadata:
  name: mongo-infra
  namespace: builder-infra
spec:
  infrastructure:
    name: mongo
    args:
      clusters: 1 # number of mongo clusters
      cluster_size: 3 # number of pods per mongo cluster
      storageclass: # uses the sc with the annotation storageclass.kubernetes.io/is-default-class: "true" if the option is not specified
      storagesize: 10Gi # default value if option not specified
      port: 27017 # default value if option not specified
      extra_options: # list of extra options that need to be passed as is to starting mongo daemon
        - "--smallfiles"
        - "--noprealloc"
```

### Starting the Infra
Once you are finished creating/editing the custom resource file and the infra operator is running, you can start the infra with:

```bash
$ kubectl apply -f /path/to/cr.yaml
```

You can then check if mongo pods are created as follows

```bash
$ kubectl get pods -l "role=mongo"
NAME      READY   STATUS    RESTARTS   AGE
mongo-0   2/2     Running   0          6m51s
```

The connection string URI for the first cluster would be mongodb://mongo0-0.mongo0.builder-infra.svc.cluster.local:27017 and for second cluster it would be mongodb://mongo1-0.mongo1.builder-infra.svc.cluster.local:27017
