from todo.templates  import list_display, menu_display, menu_select, message_display, id_input_display, todo_display, update_input_display, input_display
from todo.exception import NotFoundError, DuplicateError
from todo import views
from todo.models import Todo

while True:
  menu_display()
  menu = menu_select()

  if menu == "1" :
    todoList = views.getAlltodos()
    list_display(todoList)

  elif menu == "2" :
    while True :
      todo = input_display()
      try:
        views.register(todo)
        message_display(todo.id + "등록성공")
      except DuplicateError as error :
        message_display(error)
      finally:
          break

  elif menu == "3" :
    id = id_input_display("수정")
    try:
      todo = views.getTodo(id)
      new_person = update_input_display()
      views.update(new_person)
      message_display(id + " 일정 수정성공")
    except NotFoundError as error:
      message_display(error)  
     
  elif menu == "4" :
    id = id_input_display(" 일정 삭제")
    try:
      views.remove(id)
      message_display(id + "삭제성공")
    except NotFoundError as error :
      message_display(error)  

  elif menu == "5":
    id = id_input_display("검색")
    try:
      todo = views.getTodo(id)
      todo_display(todo)
    except NotFoundError as error:
      message_display(error)

  elif menu == "0" :
      views.save_list()
      message_display("일정 관리를 종료합니다.")
      break
  else :
    print()
    message_display("1,2,3,4,5,0번 중 하나를 선택하세요")        



