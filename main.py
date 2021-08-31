
from lib.utils import eval_file, workspace_path_join
from lib.parser import Parser

params = eval_file(workspace_path_join("input/params.txt"))



Parser(**params).run()