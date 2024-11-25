import pydoc

def explain_module(module_name):
    try:
        module = __import__(module_name)
        doc = pydoc.render_doc(module, renderer=pydoc.plaintext)
        print(doc)
    except ImportError:
        print(f"Module '{module_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        module_name = input("Enter the name of the module to explain (or 'exit' to quit): ")
        if module_name.lower() == 'exit':
            break
        explain_module(module_name)

if __name__ == "__main__":
    main()
