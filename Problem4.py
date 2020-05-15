class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.users:
        return True
    for group in group.groups:
        if is_user_in_group(user, group):
            return True

    return False

#test case
# empty groups
initial_group=Group("initial")
print("the name of group is "+initial_group.name)
#check whether this user in empty groups
print("NO users present ")
print(is_user_in_group("bill",initial_group))#RETURNS FALSE
print("dir added")
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
sub_child.add_user("bill")
#the user bill is added
#now check whether the user is in the dir
# the current state is
# parent->child->sub->child->bill
#check again
print("bill is added\n checking for user:bill")
print(is_user_in_group("bill",parent))#returns true
