#!/usr/bin/env python3
#  coding=utf-8
#  vim:ts=4:sts=4:sw=4:et
#
#  Author: Hari Sekhon
#  Date: 2023-04-15 22:35:45 +0100 (Sat, 15 Apr 2023)
#
#  https://github.com/HariSekhon/Diagrams-as-Code
#
#  License: see accompanying Hari Sekhon LICENSE file
#
#  If you're using my code you're welcome to connect with me on LinkedIn
#  and optionally send me feedback to help steer this or other code I publish
#
#  https://www.linkedin.com/in/HariSekhon
#

"""

Kubernetes Ingress on GKE

"""

__author__ = 'Hari Sekhon'
__version__ = '0.1'

from diagrams import Diagram, Cluster, Edge

# On-premise / Open Source resources:
#
#   https://diagrams.mingrammer.com/docs/nodes/onprem
#
from diagrams.onprem.network import Nginx, Traefik
from diagrams.onprem.certificates import CertManager, LetsEncrypt
from diagrams.onprem.client import Users

# K8s resources:
#
#   https://diagrams.mingrammer.com/docs/nodes/k8s
#
from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Service

# GCP resources:
#
#   https://diagrams.mingrammer.com/docs/nodes/gcp
#
from diagrams.gcp.analytics import BigQuery, Dataflow, PubSub
from diagrams.gcp.compute import AppEngine, GKE, Functions
from diagrams.gcp.network import DNS, LoadBalancing

# pylint: disable=W0104,W0106
with Diagram('Kubernetes Traefik Ingress GKE',
             show=True,
             direction='BT',
             ):

    # letsencrypt = LetsEncrypt("LetsEncrypt Certificate Authority")
    users = Users("Users")

    with Cluster("GCP"):
        load_balancer = LoadBalancing("Cloud Load Balancer")
        dns = DNS("Cloud DNS")
        # load_balancer - dns

        with Cluster("Kubernetes Cluster"):
            gke = GKE("GKE")
            # with Cluster("Cert Manager"):
            # certmanager = CertManager("Cert Manager")
            with Cluster("Ingress"):
                traefik = Traefik("Traefik\nIngress Controller")
                # certmanager >> Edge(label="SSL cert", style="dashed") >> traefik
            # letsencrypt >> Edge(label="ACME protocol\ngenerated certificate", style="dashed") >> certmanager

            with Cluster("WebApp 2"):
                service = Service("WebApp 2 Service")
                traefik >> service
                pods = []
                for _ in range(3, 0, -1):
                    pods.append(Pod(f"Pod {_}") << service)
                #     argocd >> service
                # argocd >> pods

            with Cluster("WebApp 1"):
                service = Service("WebApp 1 Service")
                traefik >> service
                pods = []
                for _ in range(3, 0, -1):
                    pods.append(Pod(f"Pod {_}") << service)
                #     argocd >> service
                # argocd >> pods

        users >> Edge(label="HTTPS traffic") >> load_balancer
        users >> Edge(label="DNS queries") >> dns
        load_balancer >> traefik