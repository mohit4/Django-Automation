# Django-Automation

![](django-automation.PNG)

### Introduction

Django is an open source full stack web application development framework packed with many amazing utilites that combined together gives a modern developer the ability to create a craft in minimum amount of time. Even though some power is already packed inside, sometimes we rely on automation to boost our productivity. This repository is created for one sole purpose, to explore the areas that can be automated and bring together power scripts and programs in one place so the end-user, in our case, the developer can benefit from it tremendously.

### Known automation areas

* Basic CRUD Views generation after parsing the models
* Basic URL generation using views list
* Django Fixture generation using models
* Dynamic fake data generation by automatically scanning the models

### Ongoing Development

| Area | Problem statement | Proposed solution |
| :--- | :---- | :--- |
| Data Generation | Django fixture is a great tool for populating initial, or test data into the web application. But everytime JSON or YAML files has to be manually written taken reference from model. Need a tool to scan the model and generate Django fixtures | **AutoFix** : A tool to scan existing models in web application and generate Django fixture in desired and acceptable format |

### Tech Stack

* Python 3.9