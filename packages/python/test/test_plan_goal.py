# coding: utf-8

"""
    Occam AI's public API

    API exposing Occam AI's planning, execution and supervision capabilities.

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from occam_sdk.models.plan_goal import PlanGoal

class TestPlanGoal(unittest.TestCase):
    """PlanGoal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlanGoal:
        """Test PlanGoal
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlanGoal`
        """
        model = PlanGoal()
        if include_optional:
            return PlanGoal(
                name = '',
                is_name_user_generated = True,
                chat_messages = [
                    occam_sdk.models.occam_llm_message.OccamLLMMessage(
                        content = null, 
                        role = 'assistant', 
                        name = '', 
                        parsed = occam_sdk.models.base_model.BaseModel(), )
                    ],
                user_id = 56,
                category = '',
                id = '',
                params = None
            )
        else:
            return PlanGoal(
                name = '',
        )
        """

    def testPlanGoal(self):
        """Test PlanGoal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
