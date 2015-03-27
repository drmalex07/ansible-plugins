import ansible.utils as utils
import ansible.errors as errors

# Note #1:
# A task which invokes the `with_subelements_if_exist` lookup-plugin, can
# be easily rewritten to a loop that uses only `with_subelements`. 
#
# For example, a loop of:
#   
#   with_subelements_if_exist:
#   - foo
#   - bar
#
# could be rewritten as:
#     
#   with_subelements:
#   - foo| selectattr('bar', 'defined')| list
#   - bar
#

# Note #2:
# The code below is based on Ansible's subelements lookup-plugin.
# We only change the behaviour for non-existent subelements.

class LookupModule(object):

    def __init__(self, basedir=None, **kwargs):
        self.basedir = basedir


    def run(self, terms, inject=None, **kwargs):
        terms = utils.listify_lookup_plugin_terms(terms, self.basedir, inject)
        terms[0] = utils.listify_lookup_plugin_terms(terms[0], self.basedir, inject)

        if not isinstance(terms, list) or not len(terms) == 2:
            raise errors.AnsibleError(
                "subelements_if_exist lookup expects a list of two items, first a dict or a list, and second a string")
        terms[0] = utils.listify_lookup_plugin_terms(terms[0], self.basedir, inject)
        if not isinstance(terms[0], (list, dict)) or not isinstance(terms[1], basestring):
            raise errors.AnsibleError(
                "subelements_if_exist lookup expects a list of two items, first a dict or a list, and second a string")

        if isinstance(terms[0], dict): # convert to list:
            if terms[0].get('skipped',False) != False:
                # the registered result was completely skipped
                return []
            elementlist = []
            for key in terms[0].iterkeys():
                elementlist.append(terms[0][key])
        else: 
            elementlist = terms[0]
        subelement = terms[1]

        ret = []
        for item0 in elementlist:
            if not isinstance(item0, dict):
                raise errors.AnsibleError("subelements_if_exist lookup expects a dictionary, got '%s'" %item0)
            if item0.get('skipped',False) != False:
                # this particular item is to be skipped
                continue 
            if not subelement in item0:
                # skip if not exists
                continue
            if not isinstance(item0[subelement], list):
                raise errors.AnsibleError("the key %s should point to a list, got '%s'" % (subelement, item0[subelement]))
            sublist = item0.pop(subelement, [])
            for item1 in sublist:
                ret.append((item0, item1))

        return ret

