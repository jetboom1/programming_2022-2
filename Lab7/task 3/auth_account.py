import auth
import menu
import notebook

class AdminPanel:
    """creates an admin panel for managing permissions"""
    def __init__(self, username, password):
        self.authenticator = auth.Authenticator()
        self.authorizer = auth.Authorizer(self.authenticator)
        self.notebook = notebook.Notebook()
        self.authenticator.add_user(username, password)
        self.authorizer.add_permission("admin") #access to all features, including changing permissions
        self.authorizer.add_permission("viewer") #access to view notes
        self.authorizer.add_permission("editor") #access to adding and deleting notes
        self.authorizer.permit_user("admin", username)

    def run(self):
        """runs the admin panel"""
        while True:
            username = input("Username: ")
            password = input("Password: ")
            try:
                self.authenticator.login(username, password)
                if self.authorizer.check_permission("admin", username):
                    print("Welcome, admin")
                    self.admin_menu()
                elif self.authorizer.check_permission("viewer", username):
                    print("Welcome, viewer")
                    self.viewer_menu()
                elif self.authorizer.check_permission("editor", username):
                    print("Welcome, editor")
                    self.editor_menu()
                else:
                    print("You do not have permission to access this system")
            except auth.InvalidPassword:
                print("Invalid password")
            except auth.UsernameAlreadyExists:
                print("Username already exists")
            except auth.NotLoggedIn:
                print("You are not logged in")
            except auth.PermitError:
                print("You do not have permission to access this system")
            except Exception as e:
                print(e)
    def admin_menu(self):
        """admin panel"""
        while True:
            print("""
            1. Add user
            2. Add permission
            3. Permit user
            4. Check permission
            5. View notebook as editor
            6. Exit
            """)
            choice = input("Enter your choice: ")
            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                try:
                    self.authenticator.add_user(username, password)
                    print("User added")
                except auth.UsernameAlreadyExists:
                    print("Username already exists")
            elif choice == "2":
                perm_name = input("Permission name: ")
                try:
                    self.authorizer.add_permission(perm_name)
                    print("Permission added")
                except auth.PermitError:
                    print("Permission already exists")
            elif choice == "3":
                print('Available permissions:')
                for perm in self.authorizer.permissions.keys():
                    print('>>> ' + perm)
                perm_name = input("Permission name: ")
                print('Available users:')
                for login in self.authenticator.users.keys():
                    print('>>> ' + login)
                username = input("Username: ")
                try:
                    self.authorizer.permit_user(perm_name, username)
                    print("Permission granted")
                except auth.PermitError:
                    print("Permission already granted")
                except auth.UsernameAlreadyExists:
                    print("Username does not exist")
                except auth.InvalidUsername:
                    print("Invalid username")
                except Exception as e:
                    print(e)
            elif choice == "4":
                print('Available permissions:')
                for perm in self.authorizer.permissions.keys():
                    print('>>> '+perm)
                perm_name = input("Permission name: ")
                print('Available users:')
                for login in self.authenticator.users.keys():
                    print('>>> ' + login)
                username = input("Username: ")
                try:
                    if not self.authorizer.check_permission(perm_name, username):
                        print("User does not have permission")
                    else:
                        print("User has permission")
                except auth.PermitError:
                    print("User does not have permission")
                except auth.NotLoggedIn:
                    print("User is not logged in")
            elif choice == "5":
                self.editor_menu()
            elif choice == "6":
                print("Exiting")
                break
            else:
                print("Invalid choice")
        self.run()
    def editor_menu(self):
        nb_menu = menu.Menu(self.notebook)
        nb_menu.run()

    def viewer_menu(self):
        nb_menu = menu.ViewerMenu(self.notebook)
        nb_menu.run()

if __name__ == '__main__':
    print('Welcome to the set up of the admin panel')
    print('Please enter username and password, they will be used to create admin account')
    admin_panel = None
    while not admin_panel:
        username = input('Username: ')
        password = input('Password: ')
        try:
            print('Now log in to the admin panel with the credentials you entered')
            admin_panel = AdminPanel(username, password)
            break
        except auth.PasswordTooShort:
            print('Password is too short, try again')
    admin_panel.run()