from typing import NamedTuple

class EnvDatas(NamedTuple):
  channel_access_token: str
  channel_secret: str
  @classmethod
  def from_dict(cls,argdict:dict) -> 'EnvDatas':
    return cls(**{key:argdict[key.upper()] for key in cls.__annotations__})

class Envloader:
  __instance = None
  @classmethod
  def __new__(cls,*args,**kwards):
    if cls.__instance is None:
      cls.__instance = super().__new__(cls)
      with open('./config/.env','r') as file:
        cls.env = EnvDatas.from_dict({line[:(ind:=line.find("="))]:line[ind+1:].rstrip() for line in file if line})
    return cls.__instance
  @property
  def env(self) :
    return self.env



if __name__=='__main__':
  A = Envloader()
  B = Envloader()
  print(A.env.channel_access_token)
  print(A.env.channel_secret)