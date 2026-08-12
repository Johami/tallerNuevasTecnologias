"""
Ejemplo Pedagógico: Patrón Modelo-Vista-Controlador (MVC)
Caso de estudio: Lista de Tareas (To-Do List)
"""

# ==========================================
# 1. MODELO (MODEL)
# Responsabilidad: Gestionar los datos y la lógica de negocio.
# ==========================================
class TodoModel:
    def __init__(self):
        # Base de datos simulada en memoria
        self._tasks = []

    def add_task(self, task_name):
        if task_name:
            self._tasks.append(task_name)
            return True
        return False

    def get_all_tasks(self):
        return self._tasks

    def delete_task(self, index):
        try:
            return self._tasks.pop(index)
        except IndexError:
            return None


# ==========================================
# 2. VISTA (VIEW)
# Responsabilidad: Presentar la información al usuario (Interfaz).
# ==========================================
class TodoView:
    @staticmethod
    def show_menu():
        print("\n--- GESTOR DE TAREAS (MVC) ---")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Salir")

    @staticmethod
    def display_tasks(tasks):
        print("\nLISTA DE TAREAS ACTUAL:")
        if not tasks:
            print("[Vacía]")
        else:
            for i, task in enumerate(tasks):
                print(f"{i}. {task}")

    @staticmethod
    def get_user_input(prompt):
        return input(prompt)

    @staticmethod
    def show_message(message):
        print(f">> {message}")


# ==========================================
# 3. CONTROLADOR (CONTROLLER)
# Responsabilidad: Intermediario. Procesa entradas y coordina Modelo/Vista.
# ==========================================
class TodoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start(self):
        while True:
            self.view.show_menu()
            choice = self.view.get_user_input("Seleccione una opción: ")

            if choice == "1":
                self.list_tasks()
            elif choice == "2":
                self.add_task()
            elif choice == "3":
                self.remove_task()
            elif choice == "4":
                self.view.show_message("Saliendo del programa...")
                break
            else:
                self.view.show_message("Opción inválida.")

    def list_tasks(self):
        tasks = self.model.get_all_tasks()
        self.view.display_tasks(tasks)

    def add_task(self):
        name = self.view.get_user_input("Nombre de la tarea: ")
        if self.model.add_task(name):
            self.view.show_message("Tarea agregada con éxito.")
        else:
            self.view.show_message("Error: El nombre no puede estar vacío.")

    def remove_task(self):
        self.list_tasks()
        try:
            idx = int(self.view.get_user_input("Índice de la tarea a eliminar: "))
            removed = self.model.delete_task(idx)
            if removed:
                self.view.show_message(f"Tarea '{removed}' eliminada.")
            else:
                self.view.show_message("Índice no encontrado.")
        except ValueError:
            self.view.show_message("Por favor, ingrese un número válido.")


# ==========================================
# PUNTO DE ENTRADA (BOOTSTRAP)
# ==========================================
if __name__ == "__main__":
    # Inicializamos los componentes
    app_model = TodoModel()
    app_view = TodoView()
    
    # El controlador recibe las instancias del modelo y la vista (Inyección)
    app_controller = TodoController(app_model, app_view)
    
    # Iniciamos la aplicación
    app_controller.start()