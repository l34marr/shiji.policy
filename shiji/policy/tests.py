import unittest2 as unittest
from shiji.policy.testing import SHIJI_POLICY_INTEGRATION_TESTING

from Products.CMFCore.utils import getToolByName

class TestSetup(unittest.TestCase):
    
    layer = SHIJI_POLICY_INTEGRATION_TESTING
    
    def test_portal_title(self):
        portal = self.layer['portal']
        self.assertEqual("ShiJi Site", portal.getProperty('title'))
    
    def test_portal_description(self):
        portal = self.layer['portal']
        self.assertEqual("Welcome to ShiJi Site", portal.getProperty('description'))
    
    def test_role_added(self):
        portal = self.layer['portal']
        self.assertTrue("Contractor" in portal.validRoles())
    
    def test_workflow_installed(self):
        portal = self.layer['portal']
        workflow = getToolByName(portal, 'portal_workflow')
        
        self.assertTrue('track_workflow' in workflow)

    def test_workflows_mapped(self):
        portal = self.layer['portal']
        workflow = getToolByName(portal, 'portal_workflow')
        
        self.assertEqual(('track_workflow',), workflow.getDefaultChain())

    def test_contact_action_installed(self):
        portal = self.layer['portal']
        portal_actions = getToolByName(portal, 'portal_actions')
        
        self.assertTrue('enquiry' in portal_actions['site_actions'])
        self.assertFalse(portal_actions['site_actions']['contact'].visible)

