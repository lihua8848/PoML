from abc import abstractmethod

from src.blockchain.peer.consensus_peer import ConsensusPeer


class ConsensusConnectorModel:
    """
    this abstract class define the method of the connector
    
    """

    def __init__(self, peer: ConsensusPeer):
        self.peer = peer

    @abstractmethod
    def broadcast(self, data, target: list):
        """
        broadcast the data to all peers
        :param data:
        :param target:
        """
        pass

    @abstractmethod
    def handle_training_request(self, data):
        pass

    @abstractmethod
    def handle_upload_request(self, data):
        pass
