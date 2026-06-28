from query.query import QueryRunner

runner = QueryRunner()

runner.query("How much does a Bulldog weigh?")

print("\n--- Second Question ---\n")

runner.query("What is 4 * 7 / 3?")