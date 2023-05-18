# cloud_metadata
cloud provider metadata retrieval

Containerized cloud provider metadata retrieval for AWS 

Validates vulnerabilities by scanning following urls from within a container:
~~~
"http://0251.00376.000251.0000376/",
"http://0251.0376.0251.0376/",
"http://0251.254.169.254",
"http://0x41414141A9FEA9FE/",
"http://0xA9.0xFE.0xA9.0xFE/",
"http://0xA9FEA9FE/",
"http://169.254.169.254.nip.io/",
"http://169.254.169.254",
"http://169.254.169.254/latest/dynamic/instance-identity/document",
"http://169.254.169.254/latest/meta-data/",
"http://169.254.169.254/latest/meta-data/ami-id",
"http://169.254.169.254/latest/meta-data/hostname",
"http://169.254.169.254/latest/meta-data/iam/security-credentials/",
"http://169.254.169.254/latest/meta-data/iam/security-credentials/aws-elasticbeanorastalk-ec2-role",
"http://169.254.169.254/latest/meta-data/iam/security-credentials/dummy",
"http://169.254.169.254/latest/meta-data/iam/security-credentials/PhotonInstance",
"http://169.254.169.254/latest/meta-data/iam/security-credentials/s3access",
"http://169.254.169.254/latest/meta-data/public-keys/",
"http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key",
"http://169.254.169.254/latest/meta-data/reservation-id",
"http://169.254.169.254/latest/user-data",
"http://169.254.170.2/v2/credentials",
"http://2852039166/",
"http://2852039166/latest/meta-data/",
"http://425.510.425.510/",
"http://7147006462/",
"http://instance-data"
~~~
renders POSITIVES(count),NEGATIVES(count):

Currently: deployed at http://app-55844.on-aptible.com/
