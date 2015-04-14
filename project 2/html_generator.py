# This code is from the exmaple code provided by Udacity. 
#I have made minor changes to fit my html structure.
def generate_lesson_HTML(lesson_header):
    html_text_1 = '''
<div class="lesson">
  <h2 id="lesson-?">
    ''' + lesson_header
    html_text_2 = '''
  </h2>'''
    lesson_html = html_text_1 + html_text_2
    return lesson_html


def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
  <div class="concept">
    <div class="concept-title">
      ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
      <p>
        ''' + concept_description
    html_text_3 = '''
      </p>
    </div>
  </div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

lesson_and_concepts = [ ['Lesson 5: Structured Data: Lists & For Loops'] ,
                             ['Structured Data', 'Structured data is data that can be broken down into its individual elements and where we can perform operations on those elements.'] ,
                             ['Lists', 'Lists are a sequence of any elements. There are no restrictions on the types of elements that can be put in a list. They can also contain more than one type of element.'] ,
                             ['Mutation', 'Mutation means we can change the value of a list after we have created it. While lists do support mutation, it is extremely important to remember that strings do not.']]



def make_concept_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return (generate_concept_HTML(concept_title, concept_description))


                 
def make_HTML_for_lesson_and_concepts(lesson_and_concepts):
  header = lesson_and_concepts[0][0]
  header_html = (generate_lesson_HTML(header))
  counter = ''
  for e in lesson_and_concepts[1:]: 
    first = make_concept_HTML(e)
    counter = counter + first
  return header_html + counter 


 

print make_HTML_for_lesson_and_concepts(lesson_and_concepts)





