# Create a custom context manager to handle database connections.
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        # Simulate opening DB connection
        print(f"[OPEN] Connecting to {self.db_name}")
        self.conn = self._connect()
        return self

    def _connect(self):
        # Replace with real DB connection (psycopg2, sqlite3, etc.)
        return {"status": "connected"}

    def execute(self, query):
        print(f"[EXECUTE] {query}")
        # Simulate query execution
        return f"Result of `{query}`"

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"[ROLLBACK] بسبب error: {exc_value}")
        else:
            print("[COMMIT] Transaction successful")

        self._close()
        return False  # re-raise exception if occurred

    def _close(self):
        print(f"[CLOSE] Closing connection to {self.db_name}")
        self.conn = None