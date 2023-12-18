from llama_index import VectorStoreIndex, SimpleDirectoryReader
import logging
import sys
import cmd

# logging.basicConfig(stream=sys.stdout, level=logging.INFO)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

documents = SimpleDirectoryReader("logs").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

class Prompt(cmd.Cmd):
    intro = 'Welcome to the Prompt. Type help or ? to list commands.\n'
    prompt = '(logbot) '

    # Command definitions
    def do_query(self, arg):
        """Query logs."""
        response = query_engine.query(arg)
        print(response)

if __name__ == '__main__':
    Prompt().cmdloop()