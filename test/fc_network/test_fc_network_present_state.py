import unittest
import mock
from hpOneView import oneview_client

from fc_network import FC_NETWORK_CREATED, FC_NETWORK_ALREADY_EXIST
from fc_network import present, get_by_name


DEFAULT_FC_NETWORK_TEMPLATE = dict(
    name= 'New FC Network 2',
    connectionTemplateUri=None,
    autoLoginRedistribution= True,
    fabricType= 'FabricAttach'
)


class FcNetworkPresentStateSpec(unittest.TestCase):

    @mock.patch.object(oneview_client, 'OneViewClient')
    @mock.patch('fc_network.get_by_name')
    def test_should_create_new_fc_network(self, mock_get_by_name, mock_ov_client):
        mock_get_by_name.return_value = []
        changed, msg, _ = present(mock_ov_client, DEFAULT_FC_NETWORK_TEMPLATE)

        self.assertEquals(msg, FC_NETWORK_CREATED)
        self.assertTrue(changed)


    @mock.patch.object(oneview_client, 'OneViewClient')
    @mock.patch('fc_network.get_by_name')
    def test_should_not_update_when_fc_network_already_exist(self, mock_get_by_name, mock_ov_client):
        mock_get_by_name.return_value = [DEFAULT_FC_NETWORK_TEMPLATE]
        changed, msg, _ = present(mock_ov_client, DEFAULT_FC_NETWORK_TEMPLATE)

        self.assertEquals(msg, FC_NETWORK_ALREADY_EXIST)
        self.assertFalse(changed)


if __name__ == '__main__':
  unittest.main()
