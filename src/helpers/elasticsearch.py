import requests
import json
import re


def scan_elasticsearch(base_url, query):
    scroll_id = None
    query = dict(query)
    query['sort'] = ['_doc']
    query['size'] = 1000
    while True:
        if scroll_id is None:
            url = base_url + '/_search'
            response = requests.get(url, data=json.dumps(query), params={'scroll': '1m'})
        else:
            url = base_url + '/_search/scroll'
            response = requests.post(url, data=scroll_id.encode('ascii'), params={'scroll': '1m'})

        if scroll_id is not None:
            query['scroll_id'] = scroll_id
        if response.status_code != 200:
            raise Exception('ElasticSearch returned non-200 status code\n{0}', response.content)
        documents = response.json()
        for hit in documents['hits']['hits']:
            yield hit
        scroll_id = documents['_scroll_id']
        if not documents['hits']['hits']:
            return


def parse_string_list(s):
    s = s.strip()
    if s.startswith('['):
        parsed = json.loads(s)
        if not isinstance(parsed, list):
            raise ValueError('Expected a JSON list of strings')
        if not all(isinstance(item, str)):
            raise ValueError('Expected a JSON list of strings')
        return parsed
    return re.split('[, ]', s)


def scan_elasticsearch_content(base_url, query_string, fields=None):
    if fields is not None:
        fields = parse_string_list(fields)
    if query_string.startswith('{'):
        query = json.dumps(query_string)
    else:
        query = {
            'query': { 'query_string': { 'query': query_string } }
        }
    if fields is not None:
        query['fields'] = fields

    content = []
    for result in scan_elasticsearch(base_url, query):
        content.append(result)

    return content