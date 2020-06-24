import uuid

from database import Database
import datetime

__author__='jslvtr'

class Post(object):

    def __init__(self,blog_id, title, content, author,date=datetime.datetime.utcnow(), id=None):
    # init method stands for initialize,
    # its a method that gets called when ur
    # creating a new thing ie post
        self.blog_id = blog_id
        self.title=title
        self.content=content
        self.author=author
        self.created_date= date
        self.id =uuid.uuid4().hex if id is None else id

    def save_to_mongo(self):
        Database.insert(collection ='posts',
                        data=self.json())

    def json(self):
        # the json method creates the json
        # representation of the post itself
        #  the json rep is a key value set as below
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author':self.author,
            'content': self.content,
            'title':self.title,
            'created_date': self.created_date
        }
    @classmethod
    def from_mongo(cls, id):
        #get data from db and give it an id thus returning a post using the id
        post_data=Database.find_one(collection='posts',query={'id':id})
        return cls(blog_id=post_data['blog_id'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   date=post_data['created_date'],
                   id=post_data['id'])

    @staticmethod
    #returning lists of posts from a specific blog
    def from_blog(id):
        return [ post for post in Database.find(collection='posts', query={'blog_id': id})]




