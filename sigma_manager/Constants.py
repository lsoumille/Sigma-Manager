## Constants
## Soumille Lucas
## 03/07/2018

GIT_PROTOCOL = "SSH"
RULE_PATH = "/tmp/rules"
CONFIGURATION_PATH = "/tmp/conf"
DESTINATION_PATH_1 = "/tmp/target1"
DESTINATION_PATH_2 = "/tmp/target2"

ITER_SIGMA_RULE_REPOSITORY = "ssh://git@git.iter.org/itsecu/sigma_rules.git"
ITER_CONFIGURATION_REPOSITORY = "ssh://git@git.iter.org/itsecu/sigma_configuration.git"
ITER_ELASTALERT_REPOSITORY = "ssh://git@git.iter.org/itsecu/elastalert_rules.git"
ITER_ELASTALERT_REPOSITORY_BRANCH_1 = "kib1"
ITER_ELASTALERT_REPOSITORY_BRANCH_2 = "kib2"

CONFIGURATION_BINDING_FILENAME = "elk-iter.yml"
CONFIGURATION_ALERT_FILENAME = "rule_alert_profile.yml"
CONFIGURATION_ALERT_PROFILES = "profiles"
CONFIGURATION_IGNORE_SIGMA = "ignore_rule.yml"
CONFIGURATION_BACKEND_ASSIGNATION = "backend_assignation.yml"

SIGMA_BACKEND = "elastalert"

DEFAULT_ALERT_PROFILE = "default"

IGNORE_SIGMA_VALUE = "elastalert"

ALL_BACKENDS = "all"