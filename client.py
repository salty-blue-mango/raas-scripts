from sseapiclient.tornado import SyncClient

raas = 'http://localhost:8080'
client = SyncClient.connect(raas, 'root', 'salt', rpc_api_version='2', force_restfull=False)