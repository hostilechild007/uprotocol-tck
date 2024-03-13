from threading import Thread
import sys
import git
repo = git.Repo('.', search_parent_directories=True)
sys.path.append(repo.working_tree_dir)

from python.test_manager.testmanager import SocketTestManager

test_manager = SocketTestManager("127.0.0.5", 12345)
thread = Thread(target=test_manager.listen_for_client_connections)
thread.start()