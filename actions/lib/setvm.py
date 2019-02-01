from st2actions.runners.pythonrunner import Action
from common import xstreamWrapper
from xstream.entities import ProvisionVMRequest, CustomizationSpecification


class setVM(Action):
    def run(self, xstream_url, public_key, private_key, tenant_id, vmspec, cloudinitspec):
        xs = xstreamWrapper(xstream_url, public_key, private_key, "VirtualMachine")
        xs.actions["VirtualMachine"].populate_operations()

        vm = ProvisionVMRequest(vmspec)
        if cloudinitspec:
            vm.CustomizationSpecification = CustomizationSpecification(cloudinitspec)
        response = xs.actions["VirtualMachine"].SetVM("", vm)
        return (True, response["Headers"])
