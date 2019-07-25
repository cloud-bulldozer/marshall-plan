#!/bin/bash

''':'
vers=( /usr/bin/python[2-3] )
latest="${vers[$((${#vers[@]} - 1))]}"
if !(ls $latest &>/dev/null); then
    echo "no python present"
    exit 1
fi
cat <<'# EOF' | exec $latest - "$@"
''' #'''
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import sys

def generate_config(instances, cluster_number):
    config = {'_id': 'rs0'}
    members_list = []
    for i in range(instances):
        mongo_instance = 'mongo' + str(cluster_number) + '-' + str(i) + '.mongo' + str(cluster_number)
        members_list.append({'_id': i, 'host': mongo_instance})
    config['members'] = members_list
    return config

def main():
    if len(sys.argv) < 2:
        sys.exit("usage: initiate_rs.py [number_of_replicas] [cluster_number]")
    replicas = int(sys.argv[1])
    cluster_number = int(sys.argv[2])
    primary_mongo = 'mongo' + str(cluster_number) + '-0.mongo' + str(cluster_number)
    c = MongoClient(primary_mongo, 27017)
    c.admin.command("replSetInitiate", generate_config(replicas,cluster_number))
    client = MongoClient(primary_mongo, replicaset='rs0')
    try:
        # The ismaster command is cheap and does not require auth.
        client.admin.command('ismaster')
    except ConnectionFailure:
        print("Server not available")
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
# EOF
