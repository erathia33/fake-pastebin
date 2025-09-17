from pydantic import BaseModel, ConfigDict, Field

class PostSchema(BaseModel):
    author: str = Field(
        min_length=4, 
        max_length=25, 
        pattern=r'^[A-Za-z0-9_]+$',
        examples=["asd123_"],
        description="Usernames must only contain alphanumeric characters.",
        )
    
    title: str = Field(
        min_length=10, 
        max_length=100,
        examples=["History of the Internet"],
        description="Title must be between 10 and 100 characters.",
        )
    content: str = Field(
        max_length=4096,
        examples=["The history of the Internet originated in the efforts of scientists and engineers to build and interconnect computer networks..."],
        description="Content must not exceed 4096 characters.",
        )
