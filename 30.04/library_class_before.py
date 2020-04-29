from elasticsearch import Elasticsearch

INDEXES = ["двор_1", "двор_2", "двор_3", "погода"]

json_to_send = {"dt": "2020-04-21 20:46:00",
                "sensor_name_3": "TD-1109",
                "temp_3": 9.2,
                "battery_3": 83.0,
                "sending_dt_3": "2020-02-22 11:31:00"}

elas_search = Elasticsearch([{'host': 'host', 'port': 'port'}], http_auth=('username', 'password'))

index = INDEXES[2]
record = json_to_send

response = elas_search.index(index=index,
                             doc_type='_doc',
                             body=record,
                             pipeline='{}-pipeline'.format(index))
