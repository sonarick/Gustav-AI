import json,sys
from pathlib import Path
from datetime import datetime

class ChatManager:
    def __init__(self):
        base=Path(sys.executable).parent if getattr(sys,'frozen',False) else Path(__file__).parent.parent
        self.chat_dir=base/'data'/'chats'
        self.chat_dir.mkdir(parents=True,exist_ok=True)
        self.current_chat=None
    def new_chat(self):
        self.current_chat=self.chat_dir/(datetime.now().strftime('%Y-%m-%d_%H-%M-%S.json'))
        with open(self.current_chat,'w',encoding='utf-8') as f:
            json.dump({'title':'Новый чат','created':datetime.now().strftime('%d.%m.%Y %H:%M'),'messages':[]},f,ensure_ascii=False,indent=4)
    def save_message(self,role,text):
        if self.current_chat is None:self.new_chat()
        data=json.loads(self.current_chat.read_text(encoding='utf-8'))
        data['messages'].append({'role':role,'content':text})
        self.current_chat.write_text(json.dumps(data,ensure_ascii=False,indent=4),encoding='utf-8')
