from enum import Enum
from typing import Union

from pydantic import BaseModel


class AgentInstanceMetadata(BaseModel):
    agent_instance_id: str


class AgentInstantiationErrorType(Enum):
    INVALID_PARAMS = "INVALID_PARAMS"
    INSUFFICIENT_CREDITS = "INSUFFICIENT_CREDITS"
    OTHER = "OTHER"


class AgentInstantiationError(BaseModel):
    error_type: AgentInstantiationErrorType
    error_message: str


class AgentInstantiationResponse(BaseModel):
    response_model: Union[AgentInstanceMetadata, AgentInstantiationError]


class AgentRunDetail(BaseModel):
    status: str
