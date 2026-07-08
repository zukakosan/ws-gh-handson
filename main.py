from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="TODO App")


class TodoCreate(BaseModel):
    title: str


class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False


# インメモリで TODO を管理する（DB は不要）
todos: list[Todo] = [
    Todo(id=1, title="Buy groceries", completed=False),
    Todo(id=2, title="Read a book", completed=True),
    Todo(id=3, title="Write report", completed=False),
]


@app.get("/")
def read_root():
    """ウェルカムメッセージを返す。"""
    return {"message": "Welcome to the TODO App!"}


@app.get("/todos", response_model=list[Todo])
def list_todos():
    """すべての TODO を一覧で返す。"""
    return todos


@app.post("/todos", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate):
    """新しい TODO を作成して返す。"""
    new_id = max((t.id for t in todos), default=0) + 1
    new_todo = Todo(id=new_id, title=todo.title, completed=False)
    todos.append(new_todo)
    return new_todo


# TODO: ハンズオンで個別の TODO を取得するエンドポイントを実装する
# GET /todos/{todo_id} で指定した id の TODO を返し、
# 見つからない場合は 404 を返すようにする。
#
@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    """指定した id の TODO を返す。見つからない場合は 404 を返す。"""
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")