<div align="center">

<img src="website/static/img/AutoPR_Mark_color.png" alt="AutoPR logo" width=300 />

<h1>🌳 AutoPR 🌳</h1>

[![Discord](https://badgen.net/badge/icon/discord?icon=nope&label&color=purple)](https://discord.gg/ykk7Znt3K6)
[![Docs](https://badgen.net/badge/icon/docs?icon=docs&label&color=blue)](https://docs.autopr.com)

Run AI-powered workflows over your codebase

</div>

## 🌟 Features

🌳 Living summaries of your code in nested READMEs   
📝 TODOs kept track of in issues  
⏳ Keep history of an API call's result in git    
📄 Summarize changes by adding a "summarize" label to a PR  
🫵 Custom actions configured in YAML

## 🚀 Getting Started

Please see the [installation guide](https://docs.autopr.com/installing/github).

## 📝 Maintainer Note

Though used internally, this project is currently not actively maintained.

Until v0.1.2, AutoPR autonomously generated pull requests from issues. 
If you'd still prefer to use AutoPR for this, set the following line in your github actions yaml:

```yaml
      uses: docker://ghcr.io/irgolic/autopr:v0.1.2
```

---

Below is an example of AutoPR's Living README:

<!-- Living README Summary -->
## 🌳 Living Summary

The folder contains files and configurations for setting up a Python project with automation tools. It includes Docker setup, licensing information, Makefile for task automation, GitHub Actions configuration, Python scripts for automating tasks, and schema definitions for defining workflows and triggers. These components collectively provide a framework for automating tasks, managing code quality, and orchestrating workflows efficiently within a Python application.


### [`Dockerfile`](https://github.com/submissionpurposeonly/awaretest/blob/7827ac89c146b063711453fd33b36658f1ad4ab0/./Dockerfile)

🏗️ Sets up a Docker image based on the `duffn/python-poetry:3.9-bullseye` image    
🔧 Installs git from the bullseye-backports repository    
📥 Copies an entrypoint script and makes it executable    
📥 Copies the `pyproject.toml` and `poetry.lock` files    
🔧 Activates the virtual environment and installs the project dependencies using Poetry    
📥 Copies the rest of the files to the `/app` directory    
🔧 Installs the application using Poetry    
🚀 Sets the entrypoint to `/entrypoint.sh` for running the app    


### [`LICENSE.md`](https://github.com/submissionpurposeonly/awaretest/blob/7827ac89c146b063711453fd33b36658f1ad4ab0/./LICENSE.md)

📄 This file contains the MIT License.  
🔒 The license grants permission to use, modify, and distribute the software.  
📝 The license requires the copyright notice and permission notice to be included in all copies.  
🚫 The software is provided "as is" without warranty.  
📅 The license is valid until 2023.  
💼 The license is owned by Raphael Francis Ltd.  


### [`Makefile`](https://github.com/submissionpurposeonly/awaretest/blob/7827ac89c146b063711453fd33b36658f1ad4ab0/./Makefile)

📝 This file is a makefile-like configuration file.  
🔧 It defines various targets and their associated commands.  
💻 The targets are: `format`, `type`, `test`, `schema`, and `all`.  
🔧 The `format` target runs a command to format code using the `black` tool.  
🔧 The `type` target runs a command to perform type checking using `pyright`.  
🔧 The `test` target runs pytest on the `autopr/tests` directory.  
🔧 The `schema` target runs a command to generate configuration entrypoints using `autopr.models.config`.  
🔧 The `all` target runs all the targets in sequence: `format`, `type`, `test`, and `schema`.  
🔧 This file is meant to automate common development tasks and ensure code quality.  


### [`action.yml`](https://github.com/submissionpurposeonly/awaretest/blob/7827ac89c146b063711453fd33b36658f1ad4ab0/./action.yml)

📄 This file is a configuration file for an automatic pull request workflow.  
🔧 It specifies the details for running the workflow, such as the Docker image to use.  
🎨 It also includes branding information, such as the icon and color to use.  
🔑 The file defines inputs required for the workflow, such as the GitHub token and base branch.  
🎥 It includes a default loading GIF URL to display while the pull request is being generated.  
🌿 The file defines a template for the name of the target branch.  
🔄 It specifies whether to overwrite existing branches and pull requests when creating from issues.  


### [`autopr/`](https://github.com/submissionpurposeonly/awaretest/blob/7827ac89c146b063711453fd33b36658f1ad4ab0/./autopr)

This folder contains a collection of Python files and directories that define modular functionalities for automating tasks in an autonomous agent system. It includes actions for various tasks, a GitHub Actions workflow entry point, logging configuration, main service implementation, data models, services for managing automated actions, trigger configurations, and workflows for handling tasks like workflow configuration management and repository updates. These files collectively provide a framework for defining, automating, and managing complex workflows within a Python application efficiently.  


### [`entrypoint.sh`](https://github.com/submissionpurposeonly/awaretest/blob/7827ac89c146b063711453fd33b36658f1ad4ab0/./entrypoint.sh)

📝 The file is a shell script  
🔧 It sets the Git configuration for a specific directory  
✉️ It sets the user email and name for Git commits  
📦 It activates a virtual environment  
🐍 It runs a Python module called `autopr.gh_actions_entrypoint`  


### [`poetry.lock`](https://github.com/submissionpurposeonly/awaretest/blob/7827ac89c146b063711453fd33b36658f1ad4ab0/./poetry.lock)

📄 This file is an executive summary  of a project or report  
🔍 It provides a high-level overview of the main points  
📝 It highlights key findings, conclusions, and recommendations  
📊 It may include a summary of data or analysis  
👥 It is intended for someone who is new to the project or report  
🚫 It does not include trivial details or technical explanations  
💡 It gives a clear understanding of the purpose and scope of the project  
👀 It provides a quick glance at the content without going into depth  
💼 It serves as a starting point for further exploration or discussion  
📌 It is concise and easy to read, even if the file is empty  


### [`pyproject.toml`](https://github.com/submissionpurposeonly/awaretest/blob/7827ac89c146b063711453fd33b36658f1ad4ab0/./pyproject.toml)

📋 This file is a configuration file for a Python project using Poetry.  
🔍 It contains information about the project's name, version, and authors.  
📄 The license of the project is specified as MIT.  
📦 It lists the packages and their dependencies required for the project.  
🧪 There are separate dependencies for testing and development.  
🔧 The build system used is Poetry.  
🔍 The file also includes configuration for the Pyright static type checker.  
🔍 It specifies the line length and target version for the Black code formatter.  


### [`strict_workflow_schema.json`](https://github.com/submissionpurposeonly/awaretest/blob/7827ac89c146b063711453fd33b36658f1ad4ab0/./strict_workflow_schema.json)

📄 The file is a JSON schema describing a strict workflow definition.  
🔍 It defines various actions that can be performed within the workflow.  
🔀 Actions include commenting, setting issue titles, walking files, making API calls, running bash commands, and more.  
📝 Each action has its own set of inputs and outputs.  
🔄 The workflow steps are defined as an array of actions.  
📚 The schema also includes definitions for various data types and declarations used within the actions.  
📝 The purpose of the file is to provide a standardized structure for defining and executing strict workflows.  
🗂️ The schema can be used to validate and ensure the correctness of workflow definitions.  
🧩 It allows for easy integration with other tools and systems that support the schema.  
📚 The file can serve as a reference for understanding the structure and capabilities of strict workflows.  


### [`trigger_schema.json`](https://github.com/submissionpurposeonly/awaretest/blob/7827ac89c146b063711453fd33b36658f1ad4ab0/./trigger_schema.json)

📋 This file defines a data structure for a trigger configuration model.    
🔗 It includes various trigger definitions like `CronTrigger`, `CommentTrigger`, and `LabelTrigger`.    
🔧 Each trigger has associated action models and field templates.    
🛠️ Actions include tasks like making API calls, executing bash commands, and processing files.    
🔄 The triggers can be set to run on specific conditions like cron schedules or specific events.    
📝 The file structure allows for defining complex workflows and automation processes.    
🔍 It provides flexibility to configure different actions based on triggers.    
📂 Trigger configurations are organized under `TopLevelTriggerConfig`.    
📄 The file serves as a blueprint for setting up automated actions based on different triggers.    
🚀 Overall, it enables the automation of various tasks based on specified conditions.    


### [`workflow_schema.json`](https://github.com/submissionpurposeonly/awaretest/blob/7827ac89c146b063711453fd33b36658f1ad4ab0/./workflow_schema.json)

📄 This file is a JSON schema definition for a workflow definition.  
🔧 It defines various types and properties for different actions and declarations used in the workflow.  
📝 The schema includes definitions for actions like commenting, setting issue title, walking files, making API calls, running bash commands, etc.  
📚 It also defines different types of declarations like template, variable, constant, and lambda declarations.  
📋 The workflow definition includes a name, description, inputs, and outputs.  
🔢 It consists of a list of steps which can be actions, workflow invocations, or conditional statements.  
🔀 Conditional statements can have if-else branches and support different conditions like lambda expressions and context checks.  
🔄 Workflow invocations can be either regular or iterable.  
🔑 Overall, this file provides a structured definition for creating and executing workflows with various actions and conditions.  

<!-- Living README Summary -->
