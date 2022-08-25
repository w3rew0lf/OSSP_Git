import textwrap

value = """Apple Inc. is an American multinational technology company that specializes 
in consumer electronics, software and online services headquartered in Cupertino, California, 
United States. Apple is the largest technology company by revenue (totaling US$365.8 billion in 2021) 
and as of June 2022, is the world's biggest company by market capitalization, the fourth-largest 
personal computer vendor by unit sales and second-largest mobile phone manufacturer. It is one of the 
Big Five American information technology companies, alongside Alphabet, Amazon, Meta, and Microsoft.."""

# Wrap this text.
wrapper = textwrap.TextWrapper(width=50)

word_list = wrapper.wrap(text=value)

# Print each line.
for element in word_list:
	print(element)