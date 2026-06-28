import re
from agent.agent import Agent
from tools.actions import known_actions


prompt = """
You run in a loop of Thought, Action, PAUSE, Observation.
At the end of the loop you output an Answer.

Use Thought to describe what you need to do.
Use Action to run one of the actions available to you, then return PAUSE.
Observation will be the result of running those actions.

Your available actions are:

calculate:
e.g. calculate: 4 * 7 / 3
Runs a calculation and returns the number.

average_dog_weight:
e.g. average_dog_weight: Collie
Returns average weight of a dog when given the breed.

Example session:

Question: How much does a Bulldog weigh?
Thought: I should look up the dog's weight using average_dog_weight.
Action: average_dog_weight: Bulldog
PAUSE

You will be called again with this:

Observation: A Bulldog weighs 51 lbs

You then output:

Answer: A Bulldog weighs 51 lbs
""".strip()


action_re = re.compile(r"^Action: (\w+): (.*)$")


class QueryRunner:
    def __init__(self, system_prompt: str = prompt, max_turns: int = 5):
        self.system_prompt = system_prompt
        self.max_turns = max_turns

    def query(self, question: str):
        agent = Agent(self.system_prompt)
        next_prompt = question

        for turn in range(self.max_turns):
            result = agent(next_prompt)
            print(result)

            actions = [
                action_re.match(line)
                for line in result.split("\n")
                if action_re.match(line)
            ]

            if not actions:
                return result

            action, action_input = actions[0].groups()
            if action not in known_actions:
                raise Exception(f"Unknown action: {action}")

            # There is an action to run
            action, action_input = actions[0].groups()
            if action not in known_actions:
                raise Exception("Unknown action: {}: {}".format(action, action_input))
            print(" -- running {} {}".format(action, action_input))
            observation = known_actions[action](action_input)
            print("Observation:", observation)
            next_prompt = "Observation: {}".format(observation)

        return "Max turns reached. Agent did not produce final answer."