from fastapi import APIRouter, Depends, UploadFile
from typing import List
from app.schemas.node_schema import TaskNodeOut, AddNode

router = APIRouter(prefix="/nodes", tags=["Nodes"])



#                   ~~~~~~~~~~~~~~~~~~~~~~
#                         Master Node
#                   ~~~~~~~~~~~~~~~~~~~~~~


# ===========
#    GET
# ===========


# мастер нода получает список всех нод для таска (живых и мертвых)
@router.get("/{task_id}/all", response_model=List[TaskNodeOut],
    description="Мастер нода получает список всех нод для таска"
)
async def get_all_nodes(task_id: int):
    pass

# мастер нода получает список живых нод для таска
@router.get("/{task_id}/alive", response_model=List[TaskNodeOut],
    description="Мастер нода получает список всех нод для таска"
)
async def get_alive_nodes(task_id: int):
    pass

# ===========
#    POST
# ===========


# добавить новую ноду в task_nodes для выполнения задачи, сменить статус ноды в таблице nodes на assigned
@router.post("/{task_id}/add", response_model=List[TaskNodeOut],
    description="мастер нода добавляет новую ноду для выполнения текущей задачи"
)
async def add_node_to_task(node_id: AddNode, task_id: int):
    pass


# ===========
#    PUT
# ===========


# изменить статус task_node на failed, статус ноды в таблице nodes на dead
@router.put("/{node_id}/{task_id}/panic", response_model=List[TaskNodeOut],
    description="мастер нода сообщает, что воркер вышел из строя"
)
async def node_fails_task(node_id: str, task_id: int):
    pass




#                   ~~~~~~~~~~~~~~~~~~~~~~
#                         Worker Node
#                   ~~~~~~~~~~~~~~~~~~~~~~


# ===========
#    PUT
# ===========


# меняет статус task_node на running, статус ноды в таблице nodes на working
@router.put("/{node_id}/{task_id}/accept", status_code=200,
    description="воркер нода принимает задачу"
)
async def node_accepts_task(node_id: str, task_id: int):
    pass


# изменить статус task_node на completed, статус ноды в таблице nodes на ready
@router.put("/{node_id}/{task_id}/complete", status_code=200,
    description="воркер нода завершает задачу и может (но не обязана) отправить результат в виде 1 или нескольких файлов"
)
async def node_completes_task(node_id: str, task_id: int, result_files: List[UploadFile] | None = None):
    pass
