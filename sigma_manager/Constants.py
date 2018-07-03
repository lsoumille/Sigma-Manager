## Constants
## Soumille Lucas
## 03/07/2018

GIT_PROTOCOL = "SSH"
RULE_PATH = "/tmp/rules"
CONFIGURATION_PATH = "/tmp/conf"
DESTINATION_PATH = "/tmp/target"

ITER_SIGMA_RULE_REPOSITORY = "ssh://git@git.iter.org/itsecu/sigma_rules.git"
ITER_CONFIGURATION_REPOSITORY = "ssh://git@git.iter.org/itsecu/sigma_configuration.git"

CONFIGURATION_BINDING_FILENAME = "iter-elk.yml"
CONFIGURATION_ALERT_FILENAME = "rule_alert_profile.yml"
CONFIGURATION_ALERT_PROFILES = "profiles"

SIGMA_BACKEND = "elastalert"

DEFAULT_ALERT_PROFILE = "default"