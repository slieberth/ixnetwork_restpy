# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE. 
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class Topology(Base):
    """Topology port level configuration
    The Topology class encapsulates a required topology resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'topology'
    _SDM_ATT_MAP = {
        'ApplyOnTheFlyState': 'applyOnTheFlyState',
        'NgpfProtocolRateMode': 'ngpfProtocolRateMode',
        'ProtocolActionsInProgress': 'protocolActionsInProgress',
        'ProtocolStackingMode': 'protocolStackingMode',
        'Status': 'status',
        'Vports': 'vports',
    }

    def __init__(self, parent):
        super(Topology, self).__init__(parent)

    @property
    def BgpIpv4Peer(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv4peer.bgpipv4peer_439a44dd340bf6fd724df996ab26569d.BgpIpv4Peer): An instance of the BgpIpv4Peer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv4peer.bgpipv4peer_439a44dd340bf6fd724df996ab26569d import BgpIpv4Peer
        return BgpIpv4Peer(self)._select()

    @property
    def BgpIpv6Peer(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv6peer.bgpipv6peer_7e5e36454dedaa483fd7dd20abef422b.BgpIpv6Peer): An instance of the BgpIpv6Peer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv6peer.bgpipv6peer_7e5e36454dedaa483fd7dd20abef422b import BgpIpv6Peer
        return BgpIpv6Peer(self)._select()

    @property
    def Esmc(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.esmc.esmc_a6e91ae9ab0a9252a7e1dbcd069fcc86.Esmc): An instance of the Esmc class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.esmc.esmc_a6e91ae9ab0a9252a7e1dbcd069fcc86 import Esmc
        return Esmc(self)._select()

    @property
    def Ethernet(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.ethernet_ccd3a65106ab16a2364be51d1a412f05.Ethernet): An instance of the Ethernet class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.ethernet_ccd3a65106ab16a2364be51d1a412f05 import Ethernet
        return Ethernet(self)._select()

    @property
    def Ipv4(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv4.ipv4_d3982d161b434ec799d31ef7237a4b96.Ipv4): An instance of the Ipv4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv4.ipv4_d3982d161b434ec799d31ef7237a4b96 import Ipv4
        return Ipv4(self)._select()

    @property
    def Ipv6(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6.ipv6_a9f2dfb33a5d9c10d60b9830b8455095.Ipv6): An instance of the Ipv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6.ipv6_a9f2dfb33a5d9c10d60b9830b8455095 import Ipv6
        return Ipv6(self)._select()

    @property
    def Ipv6Autoconfiguration(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6autoconfiguration.ipv6autoconfiguration_186fdf3eb8d47323f28ec9e4d4c3e927.Ipv6Autoconfiguration): An instance of the Ipv6Autoconfiguration class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6autoconfiguration.ipv6autoconfiguration_186fdf3eb8d47323f28ec9e4d4c3e927 import Ipv6Autoconfiguration
        return Ipv6Autoconfiguration(self)._select()

    @property
    def IsisL3Router(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.isisl3router.isisl3router_b5c245f4973246022b20f2613546d45a.IsisL3Router): An instance of the IsisL3Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.isisl3router.isisl3router_b5c245f4973246022b20f2613546d45a import IsisL3Router
        return IsisL3Router(self)

    @property
    def Macsec(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.macsec.macsec_8998c1b41f29384c2c688534cb45d85d.Macsec): An instance of the Macsec class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.macsec.macsec_8998c1b41f29384c2c688534cb45d85d import Macsec
        return Macsec(self)._select()

    @property
    def Mka(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.mka.mka_aedde1a3ca5c00a7f6b976a4fce2c20d.Mka): An instance of the Mka class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.mka.mka_aedde1a3ca5c00a7f6b976a4fce2c20d import Mka
        return Mka(self)._select()

    @property
    def Ospfv2Router(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ospfv2router.ospfv2router_74c05cad626e75b691d6431d3166eb2c.Ospfv2Router): An instance of the Ospfv2Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ospfv2router.ospfv2router_74c05cad626e75b691d6431d3166eb2c import Ospfv2Router
        return Ospfv2Router(self)

    @property
    def Ospfv3Router(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ospfv3router.ospfv3router_4c45a88f00fdf201bca989331894ee2f.Ospfv3Router): An instance of the Ospfv3Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ospfv3router.ospfv3router_4c45a88f00fdf201bca989331894ee2f import Ospfv3Router
        return Ospfv3Router(self)._select()

    @property
    def Pce(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.pce.pce_5defd13c57ea406c73fd4b2cb010a30f.Pce): An instance of the Pce class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.pce.pce_5defd13c57ea406c73fd4b2cb010a30f import Pce
        return Pce(self)._select()

    @property
    def StaticMacsec(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.staticmacsec.staticmacsec_9ab47bdf2b3b33d22965d0aa28f2bb3d.StaticMacsec): An instance of the StaticMacsec class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.staticmacsec.staticmacsec_9ab47bdf2b3b33d22965d0aa28f2bb3d import StaticMacsec
        return StaticMacsec(self)._select()

    @property
    def ApplyOnTheFlyState(self):
        """
        Returns
        -------
        - str(allowed | notAllowed | nothingToApply): Checks whether the apply changes operation is allowed
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplyOnTheFlyState'])

    @property
    def NgpfProtocolRateMode(self):
        """
        Returns
        -------
        - str(basic | smooth): Decides whether protocol's sessions will started in normal or smooth mode
        """
        return self._get_attribute(self._SDM_ATT_MAP['NgpfProtocolRateMode'])
    @NgpfProtocolRateMode.setter
    def NgpfProtocolRateMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NgpfProtocolRateMode'], value)

    @property
    def ProtocolActionsInProgress(self):
        """
        Returns
        -------
        - list(str): Lists all current protocol actions in progress
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolActionsInProgress'])

    @property
    def ProtocolStackingMode(self):
        """
        Returns
        -------
        - str(parallel | sequential): Decides whether protocol's sessions will started sequentially or parallelly across the layers
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolStackingMode'])
    @ProtocolStackingMode.setter
    def ProtocolStackingMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolStackingMode'], value)

    @property
    def Status(self):
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): The current state of the scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def Vports(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport]): List of virtual ports included in the port level configuration
        """
        return self._get_attribute(self._SDM_ATT_MAP['Vports'])

    def update(self, NgpfProtocolRateMode=None, ProtocolStackingMode=None):
        """Updates topology resource on the server.

        Args
        ----
        - NgpfProtocolRateMode (str(basic | smooth)): Decides whether protocol's sessions will started in normal or smooth mode
        - ProtocolStackingMode (str(parallel | sequential)): Decides whether protocol's sessions will started sequentially or parallelly across the layers

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def AbortApplyOnTheFly(self):
        """Executes the abortApplyOnTheFly operation on the server.

        Aborts any on the fly changes that are outstanding

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('abortApplyOnTheFly', payload=payload, response_object=None)

    def ApplyOnTheFly(self):
        """Executes the applyOnTheFly operation on the server.

        Apply any outstanding on the fly changes

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyOnTheFly', payload=payload, response_object=None)

    def ConfigureAll(self):
        """Executes the configureAll operation on the server.

        Configures all protocols in current scenario

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('configureAll', payload=payload, response_object=None)

    def FetchAndUpdateConfigFromCloud(self, *args, **kwargs):
        """Executes the fetchAndUpdateConfigFromCloud operation on the server.

        Learn MAC / IP address for a topology running on VM ports, deployed in AWS.

        fetchAndUpdateConfigFromCloud(Mode=string)
        ------------------------------------------
        - Mode (str): Mode. Options are: cmdrefreshall, cmdrefreshmac, cmdrefreshipv4

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('fetchAndUpdateConfigFromCloud', payload=payload, response_object=None)
