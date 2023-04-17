#!/usr/bin/env python3
#  coding=utf-8
#  vim:ts=4:sts=4:sw=4:et
#
#  Author: Hari Sekhon
#  Date: 2023-04-17 03:54:00 +0100 (Mon, 17 Apr 2023)
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

GitHub Actions CI/CD

"""

__author__ = 'Hari Sekhon'
__version__ = '0.1'

import os
#import requests

from diagrams import Diagram, Cluster, Edge

from diagrams.custom import Custom
from diagrams.onprem.client import User
from diagrams.onprem.ci import Jenkins, GithubActions
from diagrams.onprem.vcs import Git, Github
from diagrams.saas.chat import Slack
from diagrams.programming.language import Python
from diagrams.programming.flowchart import Document

headers = {'user-agent': 'Mozilla/5.0'}
# hari_url = "https://media.licdn.com/dms/image/C4E03AQFXEknu7Lf0kA/profile-displayphoto-shrink_800_800/0/1660301168114?e=1687392000&v=beta&t=-KmL-O8pEQY-esJA_f3sdvx7tC0juSDc9Di4bkacfXo"
hari_icon = "images/hari.jpeg"
# rolling_eyes_url = "https://em-content.zobj.net/thumbs/240/apple/354/face-with-rolling-eyes_1f644.png"
rolling_eyes_icon = "rolling_eyes.png"

# r = requests.get(rolling_eyes_url, headers=headers)
# with open(rolling_eyes_icon, 'wb') as f:
#     f.write(r.content)

# r = requests.get(hari_url, headers=headers)
# with open(hari_icon, 'wb') as f:
#     f.write(r.content)

graph_attr = {
    "splines": "spline",
}

# pylint: disable=W0104,W0106
with Diagram('GitHub Actions CI/CD',
             show=not bool(os.environ.get('CI', 0)),
             direction='LR',
             filename="github_actions_cicd",
             graph_attr=graph_attr,
             ):

    #hari = User("Hari\nPythonista")
    hari = Custom("Hari\nPythonista", hari_icon)
    you = User("You")
    #giovanni = User("Giovanni")
    giovanni = Custom("Giovanni", rolling_eyes_icon)
    git = Git("Git")

    hari \
        >> Edge(label="crazy midnight - 4am coding") \
        >> Python("Python") \
        >> Edge(label="git commit") \
        >> git

    with Cluster("Github"):
        github = Github("Diagrams-as-Code\nrepo")
        github_actions = GithubActions("GitHub Actions\nCI/CD\nGenerate Images\nworkflow")
        readme = Document("README.md")
        git \
            >> Edge(label="git push") \
            >> github \
            >> Edge(label="trigger workflow") \
            >> github_actions \
            >> Edge(label="git commit\n&&\ngit push\nnew / updated diagrams") \
            >> github \
            >> readme

    with Cluster("Banned by Giovanni"):
        with Cluster("Do Not Use"):
            # hari \
            #     - Edge(color='red', style="dashed") \
            Jenkins("Jenkins") \
            << Edge(label="banned", color='red', style="dashed") \
            << giovanni
            # github_actions \
            #     << Edge(label="I will just about tolerate this") \
            #     << giovanni

    slack = Slack("Slack")

    hari \
        >> Edge(label="Hey Guys,\nlook what I just did this weekend!") \
        >> slack \
        >> giovanni \
        >> Edge(label="Hari is doing his\nrain man thing again...") \
        >> slack \

    you >> readme
