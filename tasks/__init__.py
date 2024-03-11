import colorama
from invoke import Collection

from tasks.collection import compose_collection

import tasks.aws
import tasks.codebuild
import tasks.format
import tasks.terraform_backend
import tasks.terraform_codepipeline
import tasks.terraform_ecr

# Enable color
colorama.init()

# Apply AWS environment
tasks.aws.apply_aws_env()

# Build our task collection
ns = Collection()

# Compose from codebuild.py
compose_collection(
    ns,
    tasks.codebuild.ns,
    name="codebuild",
    include=["build"],
)

# Compose from format.py
compose_collection(
    ns,
    tasks.format.ns,
    sub=False,
)

# Compose Terraform tasks
ns_terraform = Collection("terraform")

# Compose from codepipeline.py
compose_collection(
    ns_terraform,
    tasks.terraform_codepipeline.ns,
    name="codepipeline",
    include=["apply"],
)

# Complete Terraform tasks
compose_collection(
    ns,
    ns_terraform,
    name="terraform",
)

#
# Additional non-needed tasks.
#

# Compose from aws.py
# Needed only for initial configuration.
# compose_collection(ns, tasks.aws.ns, name="aws")

# Compose from terraform_backend.py
# Needed only for initial configuration.
# compose_collection(ns_terraform, tasks.terraform_backend.ns, name="backend")
# compose_collection(ns, ns_terraform, name="terraform")

# Compose from terraform_codepipeline.py
# Needed only for initial configuration.
# compose_collection(ns_terraform, tasks.terraform_codepipeline.ns, name="codepipeline")
# compose_collection(ns, ns_terraform, name="terraform")

# Compose from terraform_ecr.py
# Needed only for initial configuration.
# compose_collection(ns_terraform, tasks.terraform_ecr.ns, name="ecr")
# compose_collection(ns, ns_terraform, name="terraform")
