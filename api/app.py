from flask import Flask
import requests
from ec2_metadata import ec2_metadata

app = Flask(__name__)


@app.route("/cluster2")
def cluster2():
    return "Hello from Cluster2!"

@app.route("/cluster1")
def cluster1():
    return hello()

@app.route("/")
def cluster():
    return "Hello, World!"


def hello():
    instance_id = ec2_metadata.instance_id
    instance_type = ec2_metadata.instance_type
    return instance_id + " is responding on " + instance_type


if __name__ == "_main_":
    app.run(host='0.0.0.0', port=80)

