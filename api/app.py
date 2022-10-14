from flask import Flask
import requests

app = Flask(__name__)

instance_name_url = "http://169.254.169.254/latest/meta-data/tags/instance/Name"
instance_cluster_type_url = "http://169.254.169.254/latest/meta-data/tags/instance/ClusterType"


@app.route("/cluster2")
def cluster2():
    hello()


@app.route("/cluster1")
def cluster1():
    hello()

@app.route("/")
def cluster():
    return "Hello, World!"


def hello():
    instance_name = requests.get(instance_name_url).text
    instance_cluster_type = requests.get(instance_cluster_type_url).text
    return instance_name + " is responding on " + instance_cluster_type


if __name__ == "_main_":
    app.run(host='0.0.0.0', port=80)

