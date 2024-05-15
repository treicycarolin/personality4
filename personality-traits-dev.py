class Personality:
  def __init__(self):
      self.description = ""
      self.steps = []

  def get_description(self):
      return self.description

  def get_steps(self):
      return self.steps


class ProblemSolvingTraitBuilder:
  def __init__(self):
      self.personality = Personality()

  def add_description(self):
      self.personality.description = "Adept at identifying, analyzing, and solving complex technical issues efficiently."

  def add_steps(self):
      self.personality.steps = ["1. Identify the problem.",
                                "2. Analyze the problem.",
                                "3. Develop a solution.",
                                "4. Implement the solution.",
                                "5. Evaluate the result."]

  def get_personality(self):
      return self.personality


class PersistencyTraitBuilder:
  def __init__(self):
      self.personality = Personality()

  def add_description(self):
      self.personality.description = "Demonstrates determination and resilience in overcoming challenges and setbacks encountered during development."

  def add_steps(self):
      self.personality.steps = ["1. Set clear goals.",
                                "2. Break tasks into manageable pieces.",
                                "3. Stay motivated despite setbacks.",
                                "4. Learn from failures and adapt.",
                                "5. Celebrate achievements."]

  def get_personality(self):
      return self.personality


class AttentionToDetailTraitBuilder:
  def __init__(self):
      self.personality = Personality()

  def add_description(self):
      self.personality.description = "Pays meticulous attention to ensuring accuracy, quality, and reliability in their work, from reviewing requirements to testing and documentation."

  def add_steps(self):
      self.personality.steps = ["1. Review requirements carefully.",
                                "2. Double-check code for errors.",
                                "3. Test thoroughly under various conditions.",
                                "4. Document processes and decisions.",
                                "5. Seek feedback for improvement."]

  def get_personality(self):
      return self.personality


class PersonalityDirector:
  def __init__(self, builder):
      self.builder = builder

  def construct_personality(self):
      self.builder.add_description()
      self.builder.add_steps()


if __name__ == "__main__":
  # Create builders
  problem_solving_builder = ProblemSolvingTraitBuilder()
  persistency_builder = PersistencyTraitBuilder()
  attention_to_detail_builder = AttentionToDetailTraitBuilder()

  # Create directors
  problem_solving_director = PersonalityDirector(problem_solving_builder)
  persistency_director = PersonalityDirector(persistency_builder)
  attention_to_detail_director = PersonalityDirector(attention_to_detail_builder)

  # Construct personalities
  problem_solving_director.construct_personality()
  persistency_director.construct_personality()
  attention_to_detail_director.construct_personality()

  # Get personalities
  problem_solving_personality = problem_solving_builder.get_personality()
  persistency_personality = persistency_builder.get_personality()
  attention_to_detail_personality = attention_to_detail_builder.get_personality()

  # Print descriptions and steps
  print("1. Problem Solving Trait:")
  print("Description:", problem_solving_personality.get_description())
  print("Steps:")
  for step in problem_solving_personality.get_steps():
      print("-", step)

  print("\n2. Persistency Trait:")
  print("Description:", persistency_personality.get_description())
  print("Steps:")
  for step in persistency_personality.get_steps():
      print("-", step)

  print("\n3. Attention to Detail Trait:")
  print("Description:", attention_to_detail_personality.get_description())
  print("Steps:")
  for step in attention_to_detail_personality.get_steps():
      print("-", step)
