## Constants
## Soumille Lucas
## 03/07/2018

GIT_PROTOCOL = "SSH"
RULE_PATH = "/tmp/rules"
CONFIGURATION_PATH = "/tmp/conf"
DESTINATION_PATH = "/tmp/target"

ITER_SIGMA_RULE_REPOSITORY = "ssh://git@git.iter.org/itsecu/sigma_rules.git"
ITER_CONFIGURATION_REPOSITORY = "ssh://git@git.iter.org/itsecu/sigma_configuration.git"
ITER_ELASTALERT_REPOSITORY = "ssh://git@git.iter.org/itsecu/elastalert_rules.git"

CONFIGURATION_BINDING_FILENAME = "elk-iter.yml"
CONFIGURATION_ALERT_FILENAME = "rule_alert_profile.yml"
CONFIGURATION_ALERT_PROFILES = "profiles"
CONFIGURATION_IGNORE_SIGMA = "ignore_rule.yml"

SIGMA_BACKEND = "elastalert"

DEFAULT_ALERT_PROFILE = "default"

IGNORE_SIGMA_VALUE = "elastalert"