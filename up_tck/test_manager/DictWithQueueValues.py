from collections import defaultdict, deque
import threading
from typing import Deque, Dict, Any

from typing import Any

class DictWithQueueValues:
    def __init__(self) -> None:
        self.key_to_queue: Dict[str, Deque[Any]] = defaultdict(deque)
        self.lock = threading.Lock()
        
    def append(self, key: str, umsg: Any) -> None:
        with self.lock:
            self.key_to_queue[key].append(umsg)
    
    def popleft(self, key: str) -> Any:
        # Blocks till get an onreceive
        while len(self.key_to_queue[key]) == 0:
            continue

        with self.lock:
            onreceive: Any = self.key_to_queue[key].popleft()

        return onreceive