from st2actions.runners.pythonrunner import Action
from common import xstreamWrapper


class List(Action):
    def run(self, xstream_url, public_key, private_key, tenant_id, resource, filters, search=None):
        xs = xstreamWrapper(xstream_url, public_key, private_key, resource)

        if resource not in xs.actions.keys():
            return (False, "Please choose valid resource from {}".format(xs.resources.keys()))

        filters.append(xs.name_fields.get(resource, "Name"))
        filters.append(xs.id_feilds.get(resource, "{}ID".format(resource)))
        if not set(filters).issubset(set(xs.valid_fields[resource])):
            return (False, ["Invalid Filter", xs.valid_fields[resource].keys()])

        response = xs.toDict(
            xs.actions[resource].find(
                filter="{} eq '{}'".format(xs.search_fields.get(resource, "TenantID"), tenant_id)
            )
        )

        results = []
        if search:
            for config_item in response:
                if all(item in config_item.items() for item in search.items()):
                    results.append(xs.filter(filters, config_item))
        else:
            for config_item in response:
                results.append(xs.filter(filters, config_item))
        return (True, results)
