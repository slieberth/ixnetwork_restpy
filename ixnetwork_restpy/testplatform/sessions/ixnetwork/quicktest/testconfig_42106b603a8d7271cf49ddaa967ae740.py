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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class TestConfig(Base):
    """NOT DEFINED
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testConfig'
    _SDM_ATT_MAP = {
        'BinaryBackoff': 'binaryBackoff',
        'BinaryFrameLossUnit': 'binaryFrameLossUnit',
        'BinaryLoadUnit': 'binaryLoadUnit',
        'BinaryResolution': 'binaryResolution',
        'BinarySearchType': 'binarySearchType',
        'BinaryTolerance': 'binaryTolerance',
        'BurstSize': 'burstSize',
        'CalculateJitter': 'calculateJitter',
        'CalculateLatency': 'calculateLatency',
        'ComboBackoff': 'comboBackoff',
        'ComboFrameLossUnit': 'comboFrameLossUnit',
        'ComboLoadUnit': 'comboLoadUnit',
        'ComboResolution': 'comboResolution',
        'ComboTolerance': 'comboTolerance',
        'CountRandomFrameSize': 'countRandomFrameSize',
        'CustomLoadUnit': 'customLoadUnit',
        'DelayAfterTransmit': 'delayAfterTransmit',
        'DetailedResultsEnabled': 'detailedResultsEnabled',
        'Duration': 'duration',
        'EnableDataIntegrity': 'enableDataIntegrity',
        'EnableExtraIterations': 'enableExtraIterations',
        'EnableFastConvergence': 'enableFastConvergence',
        'EnableLayer1Rate': 'enableLayer1Rate',
        'EnableMinFrameSize': 'enableMinFrameSize',
        'EnableOldStatsForReef': 'enableOldStatsForReef',
        'ExtraIterationOffsets': 'extraIterationOffsets',
        'FastConvergenceDuration': 'fastConvergenceDuration',
        'FastConvergenceThreshold': 'fastConvergenceThreshold',
        'ForceRegenerate': 'forceRegenerate',
        'FrameLossUnit': 'frameLossUnit',
        'FrameOrderingByRfc2889': 'frameOrderingByRfc2889',
        'FrameSizeMode': 'frameSizeMode',
        'FramesPerBurstGap': 'framesPerBurstGap',
        'Framesize': 'framesize',
        'FramesizeList': 'framesizeList',
        'Gap': 'gap',
        'GenerateTrackingOptionAggregationFiles': 'generateTrackingOptionAggregationFiles',
        'InitialBinaryLoadRate': 'initialBinaryLoadRate',
        'InitialComboLoadRate': 'initialComboLoadRate',
        'InitialStepLoadRate': 'initialStepLoadRate',
        'LatencyBins': 'latencyBins',
        'LatencyBinsEnabled': 'latencyBinsEnabled',
        'LatencyType': 'latencyType',
        'LoadRateList': 'loadRateList',
        'LoadType': 'loadType',
        'MapType': 'mapType',
        'MaxBinaryLoadRate': 'maxBinaryLoadRate',
        'MaxComboLoadRate': 'maxComboLoadRate',
        'MaxIncrementFrameSize': 'maxIncrementFrameSize',
        'MaxQuickSearchLoadRate': 'maxQuickSearchLoadRate',
        'MaxRandomFrameSize': 'maxRandomFrameSize',
        'MaxStepLoadRate': 'maxStepLoadRate',
        'MinBinaryLoadRate': 'minBinaryLoadRate',
        'MinComboLoadRate': 'minComboLoadRate',
        'MinFpsRate': 'minFpsRate',
        'MinIncrementFrameSize': 'minIncrementFrameSize',
        'MinKbpsRate': 'minKbpsRate',
        'MinQuickSearchLoadRate': 'minQuickSearchLoadRate',
        'MinRandomFrameSize': 'minRandomFrameSize',
        'Numtrials': 'numtrials',
        'PercentMaxRate': 'percentMaxRate',
        'PortDelayEnabled': 'portDelayEnabled',
        'PortDelayUnit': 'portDelayUnit',
        'PortDelayValue': 'portDelayValue',
        'ProtocolItem': 'protocolItem',
        'QuickSearchFrameLossUnit': 'quickSearchFrameLossUnit',
        'QuickSearchLoadUnit': 'quickSearchLoadUnit',
        'QuickSearchResolution': 'quickSearchResolution',
        'QuickSearchSearchType': 'quickSearchSearchType',
        'QuickSearchTolerance': 'quickSearchTolerance',
        'RateSelect': 'rateSelect',
        'ReportSequenceError': 'reportSequenceError',
        'ReportTputRateUnit': 'reportTputRateUnit',
        'Resolution': 'resolution',
        'Rfc2889ordering': 'rfc2889ordering',
        'SendFullyMeshed': 'sendFullyMeshed',
        'ShowDetailedBinaryResults': 'showDetailedBinaryResults',
        'StepComboLoadRate': 'stepComboLoadRate',
        'StepFrameLossUnit': 'stepFrameLossUnit',
        'StepIncrementFrameSize': 'stepIncrementFrameSize',
        'StepLoadUnit': 'stepLoadUnit',
        'StepStepLoadRate': 'stepStepLoadRate',
        'StepTolerance': 'stepTolerance',
        'SupportedTrafficTypes': 'supportedTrafficTypes',
        'Tolerance': 'tolerance',
        'TrafficType': 'trafficType',
        'TxDelay': 'txDelay',
        'UsePercentOffsets': 'usePercentOffsets',
    }

    def __init__(self, parent):
        super(TestConfig, self).__init__(parent)

    @property
    def BinaryBackoff(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryBackoff'])
    @BinaryBackoff.setter
    def BinaryBackoff(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BinaryBackoff'], value)

    @property
    def BinaryFrameLossUnit(self):
        """
        Returns
        -------
        - str(% | frames): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryFrameLossUnit'])
    @BinaryFrameLossUnit.setter
    def BinaryFrameLossUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BinaryFrameLossUnit'], value)

    @property
    def BinaryLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryLoadUnit'])
    @BinaryLoadUnit.setter
    def BinaryLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BinaryLoadUnit'], value)

    @property
    def BinaryResolution(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryResolution'])
    @BinaryResolution.setter
    def BinaryResolution(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BinaryResolution'], value)

    @property
    def BinarySearchType(self):
        """
        Returns
        -------
        - str(linear | perFlow | perPort): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinarySearchType'])
    @BinarySearchType.setter
    def BinarySearchType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BinarySearchType'], value)

    @property
    def BinaryTolerance(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryTolerance'])
    @BinaryTolerance.setter
    def BinaryTolerance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BinaryTolerance'], value)

    @property
    def BurstSize(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['BurstSize'])
    @BurstSize.setter
    def BurstSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BurstSize'], value)

    @property
    def CalculateJitter(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CalculateJitter'])
    @CalculateJitter.setter
    def CalculateJitter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CalculateJitter'], value)

    @property
    def CalculateLatency(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CalculateLatency'])
    @CalculateLatency.setter
    def CalculateLatency(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CalculateLatency'], value)

    @property
    def ComboBackoff(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ComboBackoff'])
    @ComboBackoff.setter
    def ComboBackoff(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ComboBackoff'], value)

    @property
    def ComboFrameLossUnit(self):
        """
        Returns
        -------
        - str(% | frames): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ComboFrameLossUnit'])
    @ComboFrameLossUnit.setter
    def ComboFrameLossUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ComboFrameLossUnit'], value)

    @property
    def ComboLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ComboLoadUnit'])
    @ComboLoadUnit.setter
    def ComboLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ComboLoadUnit'], value)

    @property
    def ComboResolution(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ComboResolution'])
    @ComboResolution.setter
    def ComboResolution(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ComboResolution'], value)

    @property
    def ComboTolerance(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ComboTolerance'])
    @ComboTolerance.setter
    def ComboTolerance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ComboTolerance'], value)

    @property
    def CountRandomFrameSize(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CountRandomFrameSize'])
    @CountRandomFrameSize.setter
    def CountRandomFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CountRandomFrameSize'], value)

    @property
    def CustomLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomLoadUnit'])
    @CustomLoadUnit.setter
    def CustomLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomLoadUnit'], value)

    @property
    def DelayAfterTransmit(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayAfterTransmit'])
    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DelayAfterTransmit'], value)

    @property
    def DetailedResultsEnabled(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DetailedResultsEnabled'])
    @DetailedResultsEnabled.setter
    def DetailedResultsEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DetailedResultsEnabled'], value)

    @property
    def Duration(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Duration'])
    @Duration.setter
    def Duration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Duration'], value)

    @property
    def EnableDataIntegrity(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDataIntegrity'])
    @EnableDataIntegrity.setter
    def EnableDataIntegrity(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDataIntegrity'], value)

    @property
    def EnableExtraIterations(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableExtraIterations'])
    @EnableExtraIterations.setter
    def EnableExtraIterations(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableExtraIterations'], value)

    @property
    def EnableFastConvergence(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableFastConvergence'])
    @EnableFastConvergence.setter
    def EnableFastConvergence(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableFastConvergence'], value)

    @property
    def EnableLayer1Rate(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLayer1Rate'])
    @EnableLayer1Rate.setter
    def EnableLayer1Rate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLayer1Rate'], value)

    @property
    def EnableMinFrameSize(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMinFrameSize'])
    @EnableMinFrameSize.setter
    def EnableMinFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMinFrameSize'], value)

    @property
    def EnableOldStatsForReef(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableOldStatsForReef'])
    @EnableOldStatsForReef.setter
    def EnableOldStatsForReef(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableOldStatsForReef'], value)

    @property
    def ExtraIterationOffsets(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExtraIterationOffsets'])
    @ExtraIterationOffsets.setter
    def ExtraIterationOffsets(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExtraIterationOffsets'], value)

    @property
    def FastConvergenceDuration(self):
        """
        Returns
        -------
        - number: sec
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastConvergenceDuration'])
    @FastConvergenceDuration.setter
    def FastConvergenceDuration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastConvergenceDuration'], value)

    @property
    def FastConvergenceThreshold(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastConvergenceThreshold'])
    @FastConvergenceThreshold.setter
    def FastConvergenceThreshold(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastConvergenceThreshold'], value)

    @property
    def ForceRegenerate(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ForceRegenerate'])
    @ForceRegenerate.setter
    def ForceRegenerate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ForceRegenerate'], value)

    @property
    def FrameLossUnit(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameLossUnit'])
    @FrameLossUnit.setter
    def FrameLossUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FrameLossUnit'], value)

    @property
    def FrameOrderingByRfc2889(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameOrderingByRfc2889'])
    @FrameOrderingByRfc2889.setter
    def FrameOrderingByRfc2889(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FrameOrderingByRfc2889'], value)

    @property
    def FrameSizeMode(self):
        """
        Returns
        -------
        - str(custom | fixed | increment | random): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameSizeMode'])
    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FrameSizeMode'], value)

    @property
    def FramesPerBurstGap(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['FramesPerBurstGap'])
    @FramesPerBurstGap.setter
    def FramesPerBurstGap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FramesPerBurstGap'], value)

    @property
    def Framesize(self):
        """
        Returns
        -------
        - number: Bytes
        """
        return self._get_attribute(self._SDM_ATT_MAP['Framesize'])
    @Framesize.setter
    def Framesize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Framesize'], value)

    @property
    def FramesizeList(self):
        """
        Returns
        -------
        - list(str): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['FramesizeList'])
    @FramesizeList.setter
    def FramesizeList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FramesizeList'], value)

    @property
    def Gap(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Gap'])
    @Gap.setter
    def Gap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Gap'], value)

    @property
    def GenerateTrackingOptionAggregationFiles(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['GenerateTrackingOptionAggregationFiles'])
    @GenerateTrackingOptionAggregationFiles.setter
    def GenerateTrackingOptionAggregationFiles(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GenerateTrackingOptionAggregationFiles'], value)

    @property
    def InitialBinaryLoadRate(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialBinaryLoadRate'])
    @InitialBinaryLoadRate.setter
    def InitialBinaryLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialBinaryLoadRate'], value)

    @property
    def InitialComboLoadRate(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialComboLoadRate'])
    @InitialComboLoadRate.setter
    def InitialComboLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialComboLoadRate'], value)

    @property
    def InitialStepLoadRate(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialStepLoadRate'])
    @InitialStepLoadRate.setter
    def InitialStepLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialStepLoadRate'], value)

    @property
    def LatencyBins(self):
        """DEPRECATED 
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyBins'])
    @LatencyBins.setter
    def LatencyBins(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatencyBins'], value)

    @property
    def LatencyBinsEnabled(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyBinsEnabled'])
    @LatencyBinsEnabled.setter
    def LatencyBinsEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatencyBinsEnabled'], value)

    @property
    def LatencyType(self):
        """
        Returns
        -------
        - str(cutThrough | storeForward): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyType'])
    @LatencyType.setter
    def LatencyType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatencyType'], value)

    @property
    def LoadRateList(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadRateList'])
    @LoadRateList.setter
    def LoadRateList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoadRateList'], value)

    @property
    def LoadType(self):
        """
        Returns
        -------
        - str(binary | combo | custom | quickSearch | step | unchanged): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadType'])
    @LoadType.setter
    def LoadType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoadType'], value)

    @property
    def MapType(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MapType'])
    @MapType.setter
    def MapType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MapType'], value)

    @property
    def MaxBinaryLoadRate(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxBinaryLoadRate'])
    @MaxBinaryLoadRate.setter
    def MaxBinaryLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxBinaryLoadRate'], value)

    @property
    def MaxComboLoadRate(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxComboLoadRate'])
    @MaxComboLoadRate.setter
    def MaxComboLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxComboLoadRate'], value)

    @property
    def MaxIncrementFrameSize(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxIncrementFrameSize'])
    @MaxIncrementFrameSize.setter
    def MaxIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxIncrementFrameSize'], value)

    @property
    def MaxQuickSearchLoadRate(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxQuickSearchLoadRate'])
    @MaxQuickSearchLoadRate.setter
    def MaxQuickSearchLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxQuickSearchLoadRate'], value)

    @property
    def MaxRandomFrameSize(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRandomFrameSize'])
    @MaxRandomFrameSize.setter
    def MaxRandomFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxRandomFrameSize'], value)

    @property
    def MaxStepLoadRate(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxStepLoadRate'])
    @MaxStepLoadRate.setter
    def MaxStepLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxStepLoadRate'], value)

    @property
    def MinBinaryLoadRate(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinBinaryLoadRate'])
    @MinBinaryLoadRate.setter
    def MinBinaryLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinBinaryLoadRate'], value)

    @property
    def MinComboLoadRate(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinComboLoadRate'])
    @MinComboLoadRate.setter
    def MinComboLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinComboLoadRate'], value)

    @property
    def MinFpsRate(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinFpsRate'])
    @MinFpsRate.setter
    def MinFpsRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinFpsRate'], value)

    @property
    def MinIncrementFrameSize(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinIncrementFrameSize'])
    @MinIncrementFrameSize.setter
    def MinIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinIncrementFrameSize'], value)

    @property
    def MinKbpsRate(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinKbpsRate'])
    @MinKbpsRate.setter
    def MinKbpsRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinKbpsRate'], value)

    @property
    def MinQuickSearchLoadRate(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinQuickSearchLoadRate'])
    @MinQuickSearchLoadRate.setter
    def MinQuickSearchLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinQuickSearchLoadRate'], value)

    @property
    def MinRandomFrameSize(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinRandomFrameSize'])
    @MinRandomFrameSize.setter
    def MinRandomFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinRandomFrameSize'], value)

    @property
    def Numtrials(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Numtrials'])
    @Numtrials.setter
    def Numtrials(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Numtrials'], value)

    @property
    def PercentMaxRate(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PercentMaxRate'])
    @PercentMaxRate.setter
    def PercentMaxRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PercentMaxRate'], value)

    @property
    def PortDelayEnabled(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortDelayEnabled'])
    @PortDelayEnabled.setter
    def PortDelayEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortDelayEnabled'], value)

    @property
    def PortDelayUnit(self):
        """
        Returns
        -------
        - str(bytes | nanoseconds): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortDelayUnit'])
    @PortDelayUnit.setter
    def PortDelayUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortDelayUnit'], value)

    @property
    def PortDelayValue(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortDelayValue'])
    @PortDelayValue.setter
    def PortDelayValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortDelayValue'], value)

    @property
    def ProtocolItem(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan]): Protocol Items
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolItem'])
    @ProtocolItem.setter
    def ProtocolItem(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolItem'], value)

    @property
    def QuickSearchFrameLossUnit(self):
        """
        Returns
        -------
        - str(%): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['QuickSearchFrameLossUnit'])
    @QuickSearchFrameLossUnit.setter
    def QuickSearchFrameLossUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QuickSearchFrameLossUnit'], value)

    @property
    def QuickSearchLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['QuickSearchLoadUnit'])
    @QuickSearchLoadUnit.setter
    def QuickSearchLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QuickSearchLoadUnit'], value)

    @property
    def QuickSearchResolution(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['QuickSearchResolution'])
    @QuickSearchResolution.setter
    def QuickSearchResolution(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QuickSearchResolution'], value)

    @property
    def QuickSearchSearchType(self):
        """
        Returns
        -------
        - str(linear | perFlow | perPort | perTrafficItem): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['QuickSearchSearchType'])
    @QuickSearchSearchType.setter
    def QuickSearchSearchType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QuickSearchSearchType'], value)

    @property
    def QuickSearchTolerance(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['QuickSearchTolerance'])
    @QuickSearchTolerance.setter
    def QuickSearchTolerance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QuickSearchTolerance'], value)

    @property
    def RateSelect(self):
        """
        Returns
        -------
        - str(fpsRate | kbpsRate | percentMaxRate): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['RateSelect'])
    @RateSelect.setter
    def RateSelect(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RateSelect'], value)

    @property
    def ReportSequenceError(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReportSequenceError'])
    @ReportSequenceError.setter
    def ReportSequenceError(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReportSequenceError'], value)

    @property
    def ReportTputRateUnit(self):
        """
        Returns
        -------
        - str(gbps | gBps | kbps | kBps | mbps | mBps): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReportTputRateUnit'])
    @ReportTputRateUnit.setter
    def ReportTputRateUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReportTputRateUnit'], value)

    @property
    def Resolution(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Resolution'])
    @Resolution.setter
    def Resolution(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Resolution'], value)

    @property
    def Rfc2889ordering(self):
        """
        Returns
        -------
        - str(noOrdering | unchanged | val2889Ordering): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Rfc2889ordering'])
    @Rfc2889ordering.setter
    def Rfc2889ordering(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Rfc2889ordering'], value)

    @property
    def SendFullyMeshed(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendFullyMeshed'])
    @SendFullyMeshed.setter
    def SendFullyMeshed(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendFullyMeshed'], value)

    @property
    def ShowDetailedBinaryResults(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShowDetailedBinaryResults'])
    @ShowDetailedBinaryResults.setter
    def ShowDetailedBinaryResults(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ShowDetailedBinaryResults'], value)

    @property
    def StepComboLoadRate(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepComboLoadRate'])
    @StepComboLoadRate.setter
    def StepComboLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepComboLoadRate'], value)

    @property
    def StepFrameLossUnit(self):
        """
        Returns
        -------
        - str(% | frames): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepFrameLossUnit'])
    @StepFrameLossUnit.setter
    def StepFrameLossUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepFrameLossUnit'], value)

    @property
    def StepIncrementFrameSize(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepIncrementFrameSize'])
    @StepIncrementFrameSize.setter
    def StepIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepIncrementFrameSize'], value)

    @property
    def StepLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepLoadUnit'])
    @StepLoadUnit.setter
    def StepLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepLoadUnit'], value)

    @property
    def StepStepLoadRate(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepStepLoadRate'])
    @StepStepLoadRate.setter
    def StepStepLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepStepLoadRate'], value)

    @property
    def StepTolerance(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepTolerance'])
    @StepTolerance.setter
    def StepTolerance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepTolerance'], value)

    @property
    def SupportedTrafficTypes(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportedTrafficTypes'])
    @SupportedTrafficTypes.setter
    def SupportedTrafficTypes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportedTrafficTypes'], value)

    @property
    def Tolerance(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Tolerance'])
    @Tolerance.setter
    def Tolerance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Tolerance'], value)

    @property
    def TrafficType(self):
        """
        Returns
        -------
        - str(burstyLoading | constantLoading): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficType'])
    @TrafficType.setter
    def TrafficType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficType'], value)

    @property
    def TxDelay(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxDelay'])
    @TxDelay.setter
    def TxDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TxDelay'], value)

    @property
    def UsePercentOffsets(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['UsePercentOffsets'])
    @UsePercentOffsets.setter
    def UsePercentOffsets(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UsePercentOffsets'], value)

    def update(self, BinaryBackoff=None, BinaryFrameLossUnit=None, BinaryLoadUnit=None, BinaryResolution=None, BinarySearchType=None, BinaryTolerance=None, BurstSize=None, CalculateJitter=None, CalculateLatency=None, ComboBackoff=None, ComboFrameLossUnit=None, ComboLoadUnit=None, ComboResolution=None, ComboTolerance=None, CountRandomFrameSize=None, CustomLoadUnit=None, DelayAfterTransmit=None, DetailedResultsEnabled=None, Duration=None, EnableDataIntegrity=None, EnableExtraIterations=None, EnableFastConvergence=None, EnableLayer1Rate=None, EnableMinFrameSize=None, EnableOldStatsForReef=None, ExtraIterationOffsets=None, FastConvergenceDuration=None, FastConvergenceThreshold=None, ForceRegenerate=None, FrameLossUnit=None, FrameOrderingByRfc2889=None, FrameSizeMode=None, FramesPerBurstGap=None, Framesize=None, FramesizeList=None, Gap=None, GenerateTrackingOptionAggregationFiles=None, InitialBinaryLoadRate=None, InitialComboLoadRate=None, InitialStepLoadRate=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LoadRateList=None, LoadType=None, MapType=None, MaxBinaryLoadRate=None, MaxComboLoadRate=None, MaxIncrementFrameSize=None, MaxQuickSearchLoadRate=None, MaxRandomFrameSize=None, MaxStepLoadRate=None, MinBinaryLoadRate=None, MinComboLoadRate=None, MinFpsRate=None, MinIncrementFrameSize=None, MinKbpsRate=None, MinQuickSearchLoadRate=None, MinRandomFrameSize=None, Numtrials=None, PercentMaxRate=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, QuickSearchFrameLossUnit=None, QuickSearchLoadUnit=None, QuickSearchResolution=None, QuickSearchSearchType=None, QuickSearchTolerance=None, RateSelect=None, ReportSequenceError=None, ReportTputRateUnit=None, Resolution=None, Rfc2889ordering=None, SendFullyMeshed=None, ShowDetailedBinaryResults=None, StepComboLoadRate=None, StepFrameLossUnit=None, StepIncrementFrameSize=None, StepLoadUnit=None, StepStepLoadRate=None, StepTolerance=None, SupportedTrafficTypes=None, Tolerance=None, TrafficType=None, TxDelay=None, UsePercentOffsets=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - BinaryBackoff (number): NOT DEFINED
        - BinaryFrameLossUnit (str(% | frames)): NOT DEFINED
        - BinaryLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): NOT DEFINED
        - BinaryResolution (number): NOT DEFINED
        - BinarySearchType (str(linear | perFlow | perPort)): NOT DEFINED
        - BinaryTolerance (number): NOT DEFINED
        - BurstSize (number): NOT DEFINED
        - CalculateJitter (bool): NOT DEFINED
        - CalculateLatency (bool): NOT DEFINED
        - ComboBackoff (number): NOT DEFINED
        - ComboFrameLossUnit (str(% | frames)): NOT DEFINED
        - ComboLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): NOT DEFINED
        - ComboResolution (number): NOT DEFINED
        - ComboTolerance (number): NOT DEFINED
        - CountRandomFrameSize (number): NOT DEFINED
        - CustomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): NOT DEFINED
        - DelayAfterTransmit (number): NOT DEFINED
        - DetailedResultsEnabled (bool): 
        - Duration (number): NOT DEFINED
        - EnableDataIntegrity (bool): NOT DEFINED
        - EnableExtraIterations (bool): NOT DEFINED
        - EnableFastConvergence (bool): NOT DEFINED
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableMinFrameSize (bool): NOT DEFINED
        - EnableOldStatsForReef (bool): NOT DEFINED
        - ExtraIterationOffsets (str): NOT DEFINED
        - FastConvergenceDuration (number): sec
        - FastConvergenceThreshold (number): NOT DEFINED
        - ForceRegenerate (bool): NOT DEFINED
        - FrameLossUnit (str): NOT DEFINED
        - FrameOrderingByRfc2889 (bool): NOT DEFINED
        - FrameSizeMode (str(custom | fixed | increment | random)): NOT DEFINED
        - FramesPerBurstGap (number): NOT DEFINED
        - Framesize (number): Bytes
        - FramesizeList (list(str)): NOT DEFINED
        - Gap (number): NOT DEFINED
        - GenerateTrackingOptionAggregationFiles (bool): NOT DEFINED
        - InitialBinaryLoadRate (number): NOT DEFINED
        - InitialComboLoadRate (number): NOT DEFINED
        - InitialStepLoadRate (number): NOT DEFINED
        - LatencyBins (str): NOT DEFINED
        - LatencyBinsEnabled (bool): NOT DEFINED
        - LatencyType (str(cutThrough | storeForward)): NOT DEFINED
        - LoadRateList (str): NOT DEFINED
        - LoadType (str(binary | combo | custom | quickSearch | step | unchanged)): NOT DEFINED
        - MapType (str): NOT DEFINED
        - MaxBinaryLoadRate (number): NOT DEFINED
        - MaxComboLoadRate (number): NOT DEFINED
        - MaxIncrementFrameSize (number): NOT DEFINED
        - MaxQuickSearchLoadRate (number): NOT DEFINED
        - MaxRandomFrameSize (number): NOT DEFINED
        - MaxStepLoadRate (number): NOT DEFINED
        - MinBinaryLoadRate (number): NOT DEFINED
        - MinComboLoadRate (number): NOT DEFINED
        - MinFpsRate (number): NOT DEFINED
        - MinIncrementFrameSize (number): NOT DEFINED
        - MinKbpsRate (number): NOT DEFINED
        - MinQuickSearchLoadRate (number): NOT DEFINED
        - MinRandomFrameSize (number): NOT DEFINED
        - Numtrials (number): NOT DEFINED
        - PercentMaxRate (number): NOT DEFINED
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): NOT DEFINED
        - PortDelayValue (number): NOT DEFINED
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - QuickSearchFrameLossUnit (str(%)): NOT DEFINED
        - QuickSearchLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): NOT DEFINED
        - QuickSearchResolution (number): NOT DEFINED
        - QuickSearchSearchType (str(linear | perFlow | perPort | perTrafficItem)): NOT DEFINED
        - QuickSearchTolerance (number): NOT DEFINED
        - RateSelect (str(fpsRate | kbpsRate | percentMaxRate)): NOT DEFINED
        - ReportSequenceError (bool): NOT DEFINED
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): NOT DEFINED
        - Resolution (number): NOT DEFINED
        - Rfc2889ordering (str(noOrdering | unchanged | val2889Ordering)): NOT DEFINED
        - SendFullyMeshed (bool): NOT DEFINED
        - ShowDetailedBinaryResults (bool): NOT DEFINED
        - StepComboLoadRate (number): NOT DEFINED
        - StepFrameLossUnit (str(% | frames)): NOT DEFINED
        - StepIncrementFrameSize (number): NOT DEFINED
        - StepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): NOT DEFINED
        - StepStepLoadRate (number): NOT DEFINED
        - StepTolerance (number): NOT DEFINED
        - SupportedTrafficTypes (str): NOT DEFINED
        - Tolerance (number): NOT DEFINED
        - TrafficType (str(burstyLoading | constantLoading)): NOT DEFINED
        - TxDelay (number): NOT DEFINED
        - UsePercentOffsets (bool): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def Apply(self):
        """Executes the apply operation on the server.

        Applies the specified Quick Test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('apply', payload=payload, response_object=None)

    def ApplyAsync(self):
        """Executes the applyAsync operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyAsync', payload=payload, response_object=None)

    def ApplyAsyncResult(self):
        """Executes the applyAsyncResult operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyAsyncResult', payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self):
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the specified Quick Test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyITWizardConfiguration', payload=payload, response_object=None)

    def GenerateReport(self):
        """Executes the generateReport operation on the server.

        Generate a PDF report for the last succesfull test run.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('generateReport', payload=payload, response_object=None)

    def Run(self, *args, **kwargs):
        """Executes the run operation on the server.

        Starts the specified Quick Test and waits for its execution to finish.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        run(InputParameters=string)list
        -------------------------------
        - InputParameters (str): The input arguments of the test.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('run', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Starts the specified Quick Test.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(InputParameters=string)
        -----------------------------
        - InputParameters (str): The input arguments of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stops the currently running Quick Test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)

    def WaitForTest(self):
        """Executes the waitForTest operation on the server.

        Waits for the execution of the specified Quick Test to be completed.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('waitForTest', payload=payload, response_object=None)
