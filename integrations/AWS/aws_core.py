from datetime import datetime, timedelta
from fastapi import Depends
from repositories.integrations import IntegrationsRepository
from api.endpoints.depends import get_current_user, get_integration_repository
from models.user import User

import boto3
from botocore.exceptions import ClientError


class Core:

    async def get_client_boto3(self, service: str, region: str = "us-east-1",
                               integration: IntegrationsRepository = Depends(get_integration_repository),
                               current_user: User = Depends(get_current_user)):
        list_of_integrations = await integration.get_by_owner_id(id=int(current_user.id))
        return boto3.client(service, aws_access_key_id=list_of_integrations.api_key,
                            aws_secret_access_key=list_of_integrations.api_secret,
                            region_name=region)

    async def _get_metric_value(self):
        return await self.get_client_boto3(service='cloudwatch').get_metric_data(
            MetricDataQueries=[
                {
                    'Id': 'myRequest',
                    'MetricStat': {
                        'Metric': {
                            'Namespace': 'AWS/Lambda',
                            'MetricName': "test",
                            'Dimensions': [
                                {
                                    'Name': 'FunctionName',
                                    'Value': "test"
                                },

                            ],
                        },
                        "Period": 3600,
                        "Stat": "Average",
                        "Unit": "Bytes"
                    },
                    "Label": "myRequestLabel",
                    "ReturnData": True
                },
            ],
            StartTime="test",
            EndTime="test",
            ScanBy='TimestampDescending',
            MaxDatapoints=1,
        )

    async def lambda_metric_monitoring(self):
        metric_values = dict()
        metric_values[self.metric_name] = self._get_metric_lambda_value()['MetricDataResults'][0]['Values']
