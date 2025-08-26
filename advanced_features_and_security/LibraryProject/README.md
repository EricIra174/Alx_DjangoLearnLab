🔐 Why Use Permissions and Groups?
In a real-world web app, not every user should have access to do everything (like editing or deleting books). So we use:

Permissions: Define what actions are allowed (like can_create, can_view, can_edit, can_delete).

Groups: Organize users by roles (like Editors, Viewers) and assign the right permissions to each group.

🧩 Step-by-Step Explanation

1. Custom Permissions in models.py
   python
   Copy
   Edit
   class Meta:
   permissions = [
   ("can_view", "Can view books"),
   ("can_create", "Can create books"),
   ("can_edit", "Can edit books"),
   ("can_delete", "Can delete books"),
   ]
   ✅ This tells Django to create these specific permissions for your Book model.
   🧠 Think of this as saying: “Hey Django, I want four specific rules for what users can do with books.”

When you run:

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Django creates these permissions in the database.

2. Create Groups and Assign Permissions
   You can do this in two ways:

✅ Option A: Django Admin Interface
Go to /admin

Click on “Groups”

Create a group like Editors

Assign can_create, can_edit, can_delete, can_view permissions to it

Assign users to this group

✅ Option B: Python Script (in assign_roles.py or Django shell)
python
Copy
Edit
editors_group.permissions.add(can_view, can_create, can_edit, can_delete)
🎯 Goal: Every user in the Editors group now has full control over books.

3. Protect Views with Permissions
   Use @permission_required to block access unless the user has permission:

python
Copy
Edit
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
...
📌 This means only users with can_view permission can see the list of books.
🔐 If a user doesn’t have permission, they’ll get a 403 Forbidden error.

4. How Permissions Are Checked
   Behind the scenes:

When a user logs in, Django knows which groups they belong to

Each group has a set of permissions

Django checks: "Does this user have the required permission?" before running the view
