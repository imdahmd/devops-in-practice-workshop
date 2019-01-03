#!/usr/bin/env python
from gomatic import *
import os, re

print "Updating PetClinic Pipeline..."
go_server_host = re.search('https?://([a-z0-9.\-._~%]+)', os.environ['GO_SERVER_URL']).group(1)
go_server_url = "%s:%s" % (go_server_host, "8153")
configurator = GoCdConfigurator(HostRestClient(go_server_url))
secret_variables = {'GCLOUD_SERVICE_KEY': 'AES:EkVNDGAoQie0Jp8OedQNdw==:hJWtsxbOqH14y+A+Bs5tPeFUkad1TMM/YWYJg++8xwo9lenHDq35l8OYCxpp3yhwC+1NSf2Gk/u4NTnmnZNCV5lUMJaYAXBF+wSx3xXUdTNPJfi1X4KwodOVji+KNalHkCujOL+C43L1x1p7cAN+drhnPTN8FBD2YJUkFvckTGDSayZevbkD2eLm7rkHxxgi6jgc86THZ+Ah3TTncA90BC+IJW+UNj/0u2Xk5SPFZuYCIkP6bYc2pEPTJZoRMB095C57XKXYBzwZQLutUQfnNQGdqDMC3C8D9Nh2z6VFJOZI2irwAvUqTeO+fDswKo2sLOMxj4iy1tvUMAp5A5O6pRus75y0jnI0Luljc/jvdYC7YW+k6ujkfTeRBqWkpDtLz+VFYKHIzbQuvklroLOMiF6BgH8g4psvPOGeqvC+CmCBoV6SaAEIp3LhsWeUgMuK6K+P7MQaI+gfExInTmbc8jak2snNqAae5wmx+MwDTYYwzxaWhrG5w4mKTyJvqDoTqyYHWkR++S7QODXe9a1do6XbCxcbVB2vTwsAEoIEovvpgyhIIDj8FE0bKWAMUUooojp4833QDch85j1omhIu8hzlPghKENi81uG7nuzp0cP6NILNtbaEPJ6HxHoLyJVXf0VfKcTj5VRErNDskbm2YqVPt/e5XheNU5VqSdnvJxLYd6k7B/BZaToYGDK52PC6npZfx5rPZxtbiwamL8C8Ki8kdglfC2c7mxMcTEl4sZsVOYvmnIeJ+hg3+8iT5FcXKyOEJWXxNuwtolueETuJSPQ0Z3TnqxycFKXsnGD4csG7OzbJwy8qiB/JQ7GWzFeapKyUMGRia9bJA0BHkGRTZoZptehmwWjGOaBLl89Gddx5DVZHLZgI8K2oaSSvTJvEAJlK9lMjaADNoLK65vEp5jNvuUMsgDQgotf4aUZ0md98+jnBGroMk/rY+RlFUDoCz1Jt+CeCgNyo4ezNUMjKdRbaAviqeDoUTHBjSXAyJljQTe0giFTFE9FCbb/Yf13adZh2jqJncYZmbl2V0p/leP+zAmPjh3+Kghixb48ayQ+VFHKi1umtRPXIs/sUgRAgaLV64KdQ33/dn8zU0V52UMiU9gBWpnMlmxzLbdDAfhBfSeuwJkYDquBn6YP/pi3DNR6a5pnLSLOiek5Kh1+bEisZMYUf22666k74Rn9Pq8Di/L+63yaQrpHNu9asr883IQqlzaeMP7fZIcEb2/EL//O8mm1Ct1J18yGSN2Fp2M9Ty7LVqxlRWe2M8U/xaez0zo5IjaLdN7Ty4I12FF1aXS47MeLG5J1SFGb/5M8x4xvv9yu7cH8S3fr5yFsIyFnSc1w6oJLrSTsJo1PHqM8dHE7dOaoPO6gW1LA4OzaLvl48A3PvGa7JOALHIHQaA7mTtrEwR8ZC1QVOSHZmiRFlU5pksd6G9oOPLKB21+tzMSROTSxyKaPJyCHxPClJ5Ti9vK0z4htM+65Q6bv3pKBdXRwSO+NdMCVkJn4q7ZOWWSJqJNPM6d8Z3x7MsURKnuvXvPc+A/RX+2QcRQQDGNGBUSDDFhzL96Tp2ulAfbyIQQdogaoJsfHGcYcCN2x/pGsPsDeCf2A8zcydO4hf3H+NsHPLsffgINtoVGhxUkXUbfHFDiIwBqMRIgVT2MJ/T+QKoFq7hf6B4hgYhujVCs/yquBF2QOeXIRy8R8MFZh7svw+F44mhu/0+B2Byogqkqu4r1+7Bkbo0mzRkytfEIx/wG7QCh2Q9kD1Ut7Vj/rVkirPBetRWJdgw6iLKnITrMydFn+EgJLsCbzJgBQsXFFD5hnu2t70HFVjSbyEZN5fYCyzcUpWeIR7kD85RdRWQ2Cm7TuOc7IERVEm1EAKAlIAcPYRdAi+fyUOvE/1hFDTrQMXh6kLZqgtd+YzS4WnrdK75+t9Kp4NPQ3POuKqTE2/TkDAqlRPTJyptRfI+M7ijioICWAMI8ATcJFgo/hCjaEVd4NlZ/gLOHAltOlE5ktAimIyYKLNEIhwhGdDWRxWzppvtTqStVMGIqnY/g7l3cnq3+CqdH/z1pMAJGkaPxlpG2EbIOKrq6Y+sYfro4EsknqWNVZIFkpOw1inzqgbk8opYgdChro0dXJOxKVF8UBEaFX7tCixd8aMnY5SZaePYQBBxin12Y/RFJjRubelb6VFM8brMO3IrhN4OaJI25t6CQewHGFTKwON9c5Gz/AvwoXi5mB8qSnDlw0i3zIIaS0EQ4d04hqJizV9Ipt/tAdeUNXs9zuleTN0kEvDVVHQKYdYmOr7DXLqfdGoHAcy1YwfFgzuj7f8+wRjRhD0zxLEOKAayw138AhAh+Yvs7FJqoFlfOXWva2wwUqnPUzxApgPIffsiSNCmqKL72WL98Cg8fAGy2XaKOb4/fyl3RSaiaKtLNSYcj9g0PJEk+MUQFkZiaqdeoZdmpd9i+oDjwfW1O4QMQQq9ULrwZmBE6gAzU1l9lV5M4GB7cLCz0diZ817TvKIJXU70q2/2ZW/eudTYLdLsTPFZLGTXYhAr2twI4KlpmziAcS87gRlP+E+kMoVtWDkGQDxBnoHYNMoGPlr6YZ3Lj3oMq4xjjhTNbJjfUqGSO2+Q/Pe+9x902FWI2DRmIjmkkFqC7/nLPVGevzi6H85d+fM4QY7u8o/cLv+pacGXHLlicKlnC30vHlSmPkBKRz4pv1mD0uE4KW8bqdobak4kyuRdx4Sik0/EenwpVWnfvquQumF2zN1StBdwF9gYeZZabWLu9KtVkIUzXlWNrWDTFE+13qfN1oz3hrFEEBtysuvXfZIIbUxYO2qTjRw0TqquY/BJPeXH9LYutJHIB2qEVtcbH+w9vyc5Fbr9mqihcxm2udeaiheJ2P0nRGY6wKofVmNYVHcO2Jk4Tbs/tTurBM/NKlWdLpxy/4Y95C0EvPny46HjwoWaY3vtQCblMgqzNt4+SF2xK9iUETwKMmjn6ixuvgNqKGd2a+KQBk/Lw2R/VRDvn0VaNQDOybWRpslM3iSfFytPP7MAEvhPHc02eUQ7yZg+rA7WskyzSfhrNnsgzWQETL1eqUCQ7U647p6l7j+kooTA7tlgUjIuXeM4OE3gSjHu5CPB71zgxYg5SVnZ1z7farG8mP9d65OEzTbgJ0kfGHsyXRi2xkwtEbaU5kBLvvfMk7BvOhxVeAzGWGqF6yyRnsaoTV8N3svGV07kgBkdFwTCYNGTA7s+NcT8oqfem8T/GEOM5gbXYXw6OVgylG0iQagGM8hjlPkx/89Xl1U78FbTUI1IknxB0SWl2AjeebP2VLIdz4il1uF3fdN+E0xc81PSvN5czIznPKFHVpQR2e3fiyzyjpD8EjSZaGNN0A6df+Qp/BWDqPNpA/xAaI6ns3VBi/FsTkxZMqcbngagXytsjUHOHty8PafUv9TvF3VYbwH8gw899uTcib8lBHxIEEhr8xOZQsHxuvrb07FJ9lBBa27fthVYIpeNpgUQ9hpqmrzEskkrIs8dqKDkhtsg2+UNFOzofPXTBbRMc9o1FRnXjl5ZZmCt8gsJf+OvyXuYLs6IGicIXFXNXLzma8Xgzaj5UNXBVhKDPFmJaoaA+JgauVof0n++PSS68JK0u7+grMBn+VtPPrIRASTjOUehRTauOW0UmPOqW9RreErlNs1Gp0PiQv47m+6jL96Ng3sNBQhfC64TEcayAiCdw7/mE/bQ8LsOZGxc7qADoCivpOx8uS9X2l3MFeRWKkXbq82M94BOZC/9jiVhstyGbC+B2a154BwuWPMJBcpB/kehZKIJzNcXpFUW1ogFWCuaqWTRiXFMVp7V2hM9E108VK4eRyMZLZl9yoSdRY1+ki5zboiDfhIbGvYkQTrKA76aXD6nQEjYRTanEXzmivtaIMXB+JbofNPzh4UKexgoJeHJvbxL0BvGGv9Q4YqTJZOXZ4UKgX6de4GA/Xi76IfRHz1iT8TAMGXSe0COMVs2HIrvAbZW4O1MRvG15jvD5pw7YjV8FTcF4lvmeTQNROfotZ4DXtl1Zw4smkHo2rqFRSkrlxBnENewNDqTChZrsZVbG3A/sjJ+Yr2qR+zmjHwqjFrHkOqcPkFyYi1d7BsNdDPokNLvx2ikq9vJDK6hj86B0zTf8dxgvo6crzm3qp7TRJpInku8dhct9m1jDVhuOnQQ2rLei+1zRY2mQ=='}
configurator = GoCdConfigurator(HostRestClient("35.244.252.225", ssl=False))
pipeline = configurator\
    .ensure_pipeline_group("sample")\
    .ensure_replacement_of_pipeline("PetClinic")\
    .set_git_material(GitMaterial("https://github.com/imdahmd/devops-in-practice-workshop", ignore_patterns=set(['pipelines/*']))).ensure_environment_variables({'GCLOUD_PROJECT_ID': 'devops-workshop-03012019'}).ensure_encrypted_environment_variables(secret_variables)
stage = pipeline.ensure_stage("commit").ensure_environment_variables({'MAVEN_OPTS': '-Xmx1024m'})
job = stage.ensure_job("build-and-publish").set_elastic_profile_id("docker-jdk")
job.add_task(ExecTask(['./mvnw', 'clean package']))
job.add_task(ExecTask(['bash', '-c', 'docker build --tag pet-app:$GO_PIPELINE_LABEL --build-arg JAR_FILE=target/spring-petclinic-2.0.0.BUILD-SNAPSHOT.jar .']))
job.add_task(ExecTask(['bash', '-c', 'docker login -u _json_key -p"$(echo $GCLOUD_SERVICE_KEY | base64 -d)" https://us.gcr.io']))
job.add_task(ExecTask(['bash', '-c', 'docker tag pet-app:$GO_PIPELINE_LABEL us.gcr.io/$GCLOUD_PROJECT_ID/pet-app:$GO_PIPELINE_LABEL']))
job.add_task(ExecTask(['bash', '-c', 'docker push us.gcr.io/$GCLOUD_PROJECT_ID/pet-app:$GO_PIPELINE_LABEL']))
stage = pipeline.ensure_stage("deploy")
job = stage\
    .ensure_job("deploy")\
    .ensure_environment_variables({'GCLOUD_ZONE': 'us-central1-a', 'GCLOUD_PROJECT_ID': 'devops-workshop-03012019', 'GCLOUD_CLUSTER': 'devops-workshop-gke'})\
    .ensure_encrypted_environment_variables(secret_variables)
job.set_elastic_profile_id('kubectl')
job.add_task(ExecTask(['bash', '-c', 'echo $GCLOUD_SERVICE_KEY | base64 -d > secret.json && chmod 600 secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud auth activate-service-account --key-file secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud container clusters get-credentials $GCLOUD_CLUSTER --zone $GCLOUD_ZONE --project $GCLOUD_PROJECT_ID']))
job.add_task(ExecTask(['bash', '-c', './deploy.sh']))
job.add_task(ExecTask(['bash', '-c', 'rm secret.json']))
stage = pipeline.ensure_stage("approve-canary")
stage.set_has_manual_approval()
job = stage\
    .ensure_job("complete-canary")\
    .ensure_environment_variables({'GCLOUD_ZONE': 'us-central1-a', 'GCLOUD_PROJECT_ID': 'devops-workshop-03012019', 'GCLOUD_CLUSTER': 'devops-workshop-gke'})\
    .ensure_encrypted_environment_variables(secret_variables)
job.set_elastic_profile_id('kubectl')
job.add_task(ExecTask(['bash', '-c', 'echo $GCLOUD_SERVICE_KEY | base64 -d > secret.json && chmod 600 secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud auth activate-service-account --key-file secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud container clusters get-credentials $GCLOUD_CLUSTER --zone $GCLOUD_ZONE --project $GCLOUD_PROJECT_ID']))
job.add_task(ExecTask(['bash', '-c', './complete-canary.sh']))
job.add_task(ExecTask(['bash', '-c', 'rm secret.json']))

configurator.save_updated_config()
