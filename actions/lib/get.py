from st2actions.runners.pythonrunner import Action
from common import xstreamWrapper


class Get(Action):
    def run(self, xstream_url, public_key, private_key, tenant_id, resource, id, name, filters):
        xs = xstreamWrapper(xstream_url, public_key, private_key, resource)

        if resource not in xs.actions.keys():
            return (False, xs.actions.keys())

        if filters:
            filters.append(xs.name_fields.get(resource, "Name"))
            filters.append(xs.id_feilds.get(resource, "{}ID".format(resource)))
            if not set(filters).issubset(set(xs.valid_fields[resource])):
                return (False, ["Invalid Filters", xs.valid_fields[resource].keys()])
        else:
            filters = xs.valid_fields[resource].keys()

        if id:
            response = xs.toDict(xs.actions[resource].find(id))
        elif name:
            response = xs.toDict(
                xs.actions[resource].find(
                    filter="{} eq '{}'".format(xs.name_fields.get(resource, "Name"), name)
                )
            )

        if type(response) == list and len(response) > 0:
            return (True, xs.filter(filters, response[0]))
        elif response:
            return (True, xs.filter(filters, response))
        return (False, "{} {} not found".format(resource, (id or name)))
