from xstream.client import Proxy, KeyPairMiddleware
import toml
import json


class xstreamWrapper:
    def __init__(
        self,
        xstream_url,
        public_key,
        private_key,
        resource,
        api_key="/opt/stackstorm/packs/onboarding/actions/fields.toml",
    ):
        xsapi = Proxy("{}/api/v1.3/".format(xstream_url), KeyPairMiddleware(public_key, private_key))

        with open(api_key) as fh:
            self.valid_fields = toml.load(fh)

        self.actions = {
            "VirtualMachine": xsapi.VirtualMachine,
            "ComputeCluster": xsapi.ComputeCluster,
            "HypervisorHost": xsapi.HypervisorHost,
            "Hypervisor": xsapi.Hypervisor,
            "HardwareTemplate": xsapi.HardwareTemplate,
            "Network": xsapi.Network,
            "Profile": xsapi.Profile,
            "ResourcePool": xsapi.ResourcePool,
            "Site": xsapi.Site,
            "Storage": xsapi.Storage,
            "TaskInfo": xsapi.TaskInfo,
            "Tenant": xsapi.Tenant,
            "User": xsapi.User,
            "VirtualSwitch": xsapi.VirtualSwitch,
            "ServiceOffering": xsapi.ServiceOffering,
            "Profile": xsapi.Profile,
        }
        self.search_fields = {"Tenant": "ParentTenantID"}
        self.id_feilds = {"TaskInfo": "TaskId"}
        self.name_fields = {
            "User": "UserPrincipalName",
            "VirtualMachine": "Name",
            "Storage": "ExternalIdentifier",
            "TaskInfo": "TaskName",
        }
        self.resource = resource

    def filter(self, filters, result):
        filtered = {}
        for key in filters:
            filtered[key] = result.get(key, None)
        return filtered

    def whatever(self, search):
        for key, value in search.items():
            if key not in self.valid_fields.keys():
                return False
            if type(value) == dict:
                self.validate(value, self.valid_fields[key])
        return True

    def toDict(self, response):
        return json.loads(json.dumps(response))

    def validate(self, filters):
        filters = set(filters)
        if filters.issubset(self.valid_fields[self.resource]):
            return True
        return False
