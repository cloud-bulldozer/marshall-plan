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
      servers: 3 # has to be > 0
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
mongo-1   2/2     Running   0          6m48s
mongo-2   2/2     Running   0          6m45s
```

The connection string URI is "mongodb://mongo/ycsb?replicaSet=rs0"
