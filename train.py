import cohere
from cohere.classify import Example
co = cohere.Client('b73cb43c-740e-4f98-a5c1-90586bbf65e8-ft')

response = co.classify(
  model='b73cb43c-740e-4f98-a5c1-90586bbf65e8-ft',
  inputs=["I drank a lot of water and went on a long hike and watched some birds"])

print('The confidence levels of the labels are: {}'.format(response.classifications))