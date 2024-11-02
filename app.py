import random
from transformers import pipeline # type: ignore

# Load a pre-trained model for question answering
qa_pipeline = pipeline("question-answering")

# Expanded FAQ dictionary
faqs = {
    "What is the placement process?": "The placement process typically includes resume screening, aptitude tests, coding tests, and technical HR interviews.",
    "How can I prepare for aptitude tests?": "Practice regularly with sample papers, focus on time management, and review key concepts like percentages and ratios.",
    "What should I expect in coding interviews?": "Expect to solve algorithm and data structure problems, and be prepared to explain your thought process.",
    "What is the role of technical HR interviews?": "Technical HR interviews assess your technical knowledge and your fit for the company culture.",
    "How important is a resume in the placement process?": "A well-crafted resume is crucial as it's often the first impression a recruiter gets of you.",
    "What skills are most valued by employers?": "Employers typically value problem-solving skills, communication skills, and proficiency in relevant technologies.",
    "What is the difference between a technical interview and an HR interview?": "A technical interview focuses on your technical skills, while an HR interview assesses your personality and fit for the company.",
    "How can I improve my coding skills?": "Practice coding regularly on platforms like LeetCode, HackerRank, or CodeSignal, and work on projects to apply your skills.",
    "What topics should I study for technical interviews?": "Focus on data structures, algorithms, system design, and specific technologies relevant to the job.",
    "How do I handle tough interview questions?": "Stay calm, take your time to think, and don't hesitate to ask for clarification if needed.",
    "What are common coding interview questions?": "Common questions include reversing a string, finding the nth Fibonacci number, and implementing data structures.",
    "What should I wear to an interview?": "Dress professionally according to the company's culture, usually business formal or business casual.",
    "How do I follow up after an interview?": "Send a thank-you email expressing your appreciation for the opportunity and reiterating your interest in the position.",
    "What are behavioral interview questions?": "Behavioral questions assess how you've handled situations in the past and often start with 'Tell me about a time when...'",
    "How can I prepare for behavioral interviews?": "Use the STAR method (Situation, Task, Action, Result) to structure your responses to behavioral questions.",
    "What is an aptitude test?": "An aptitude test measures your logical reasoning, numerical ability, and problem-solving skills.",
    "What types of questions are in an aptitude test?": "Questions can include logical reasoning, quantitative aptitude, verbal reasoning, and data interpretation.",
    "How do I improve my aptitude test scores?": "Practice with sample tests and learn time management techniques to complete questions more efficiently.",
    "What is a coding challenge?": "A coding challenge is an exercise where you're asked to solve programming problems to demonstrate your coding skills.",
    "How do I prepare for a coding challenge?": "Familiarize yourself with common algorithms and data structures and practice solving problems under time constraints.",
    "What is the purpose of a group discussion in the interview process?": "A group discussion assesses your communication skills, teamwork, and ability to articulate your thoughts.",
    "How can I excel in a group discussion?": "Listen actively, contribute your ideas clearly, and encourage others to share their views.",
    "What are some common mistakes to avoid in interviews?": "Avoid being unprepared, speaking negatively about previous employers, and not asking questions at the end of the interview.",
    "How do I research a company before an interview?": "Review the company's website, recent news articles, and their social media profiles to understand their culture and values.",
    "What is a technical test?": "A technical test evaluates your skills in a specific technology or programming language relevant to the position.",
    "What are some good questions to ask the interviewer?": "Ask about team culture, opportunities for growth, and what a typical day looks like in the role.",
    "How can I showcase my projects during an interview?": "Discuss the challenges you faced, your approach to solving them, and the impact of your project.",
    "What is mock interviewing?": "Mock interviewing is a practice interview that helps you prepare for real interviews by simulating the experience.",
    "How do I find a mentor for placement preparation?": "Reach out to professors, industry professionals, or alumni who can provide guidance and support.",
    "What should I include in my portfolio?": "Include your projects, coding challenges, internships, and any relevant coursework or certifications.",
    "How important are internships for placements?": "Internships provide practical experience and can significantly enhance your resume and interview prospects.",
    "What role do certifications play in job applications?": "Certifications demonstrate your expertise and commitment to learning, making you more attractive to employers.",
    "How do I handle salary negotiations?": "Research salary ranges for similar roles, and be prepared to discuss your skills and experience justifying your request.",
    "What is the significance of networking in placements?": "Networking can help you learn about job opportunities, gain referrals, and receive valuable advice from industry professionals.",
    "How can I improve my communication skills for interviews?": "Practice speaking clearly and confidently, and consider joining public speaking groups like Toastmasters.",
    "What is the STAR method?": "The STAR method is a technique for answering behavioral interview questions by outlining the Situation, Task, Action, and Result.",
    "How do I prepare for a case interview?": "Familiarize yourself with common case interview frameworks and practice structuring your responses logically.",
    "What are some examples of coding languages I should know?": "Common languages include Python, Java, C++, and JavaScript, depending on the job requirements.",
    "What is a software development life cycle (SDLC)?": "The SDLC is a process used by software developers to design, develop, and maintain software applications.",
    "What is an algorithm?": "An algorithm is a step-by-step procedure for solving a problem or completing a task.",
    "How do I stay updated with industry trends?": "Follow tech blogs, attend webinars, and participate in online courses to keep your skills current.",
    "What is version control?": "Version control is a system that records changes to files over time, allowing you to revert to specific versions when needed.",
    "What is Git?": "Git is a widely used version control system that helps track changes in source code during software development.",
    "What are the differences between front-end and back-end development?": "Front-end development focuses on the visual aspects of a website, while back-end development deals with server-side logic and database management.",
    "What is API?": "An API (Application Programming Interface) allows different software applications to communicate with each other.",
    "What is a database?": "A database is an organized collection of structured information that can be easily accessed, managed, and updated.",
    "What are the types of databases?": "Common types include relational databases, NoSQL databases, and in-memory databases.",
    "What is SQL?": "SQL (Structured Query Language) is a programming language used for managing and querying relational databases.",
    "How do I prepare for system design interviews?": "Understand design principles, practice designing systems, and be prepared to explain your choices.",
    "What are data structures?": "Data structures are ways to organize and store data to enable efficient access and modification.",
    "What are some common data structures?": "Common data structures include arrays, linked lists, stacks, queues, trees, and hash tables.",
    "What is an operating system?": "An operating system is software that manages computer hardware and software resources and provides services to applications.",
    "What is a programming paradigm?": "A programming paradigm is a fundamental style of computer programming, such as object-oriented or functional programming.",
    "What is agile methodology?": "Agile is a project management and product development approach that emphasizes iterative progress and flexibility.",
    "What is a tech stack?": "A tech stack is a combination of technologies used to build and run an application.",
    "What is DevOps?": "DevOps is a set of practices that combines software development (Dev) and IT operations (Ops) to shorten the development life cycle.",
    "How do I improve my problem-solving skills?": "Practice solving different types of problems, break them down into smaller parts, and work on puzzles and brainteasers.",
    "What is a cloud service?": "A cloud service is a service provided over the internet that offers computing resources and storage on-demand.",
    "What are some popular cloud service providers?": "Popular providers include AWS, Microsoft Azure, Google Cloud Platform, and IBM Cloud.",
    "What is machine learning?": "Machine learning is a branch of artificial intelligence that enables systems to learn from data and improve over time.",
    "What is a neural network?": "A neural network is a computational model inspired by the way biological neural networks in the human brain work.",
    "What is big data?": "Big data refers to extremely large datasets that can be analyzed to reveal patterns, trends, and associations.",
    "What is data analysis?": "Data analysis is the process of inspecting, cleansing, transforming, and modeling data to discover useful information.",
    "What is a data scientist?": "A data scientist is a professional who uses statistical and computational techniques to analyze and interpret complex data.",
    "What is a data analyst?": "A data analyst interprets data and turns it into information to help organizations make informed business decisions.",
    "What is a business analyst?": "A business analyst identifies business needs and finds technical solutions to business problems.",
    "How do I prepare for online assessments?": "Practice with online assessment platforms and familiarize yourself with the format of the tests.",
    "What are soft skills?": "Soft skills are non-technical skills that relate to how you work and interact with others, such as communication and teamwork.",
    "Why are soft skills important for placements?": "Soft skills complement technical skills and are essential for effective collaboration and communication in the workplace.",
    "How do I build a strong LinkedIn profile?": "Include a professional photo, a compelling summary, relevant skills, and endorsements from peers.",
    "What is personal branding?": "Personal branding is the practice of marketing yourself and your career as a brand.",
    "How do I prepare for remote interviews?": "Test your technology beforehand, find a quiet space, and be mindful of your body language on camera.",
    "What are the challenges of remote work?": "Challenges include communication barriers, feeling isolated, and difficulty separating work-life balance.",
    "What are some tips for time management during placements?": "Prioritize tasks, set clear deadlines, and break tasks into manageable parts.",
    "How do I stay motivated during job searches?": "Set achievable goals, celebrate small wins, and seek support from friends and mentors.",
    "What is work-life balance?": "Work-life balance refers to the equilibrium between personal life and work commitments.",
    "How can I improve my adaptability skills?": "Stay open to new ideas, embrace change, and seek out new experiences that challenge your comfort zone.",
    "What is emotional intelligence?": "Emotional intelligence is the ability to recognize, understand, and manage your own emotions and those of others.",
    "How can I enhance my leadership skills?": "Take on leadership roles in projects, seek feedback, and learn from effective leaders in your field.",
    "What should I do if I don’t get the job?": "Request feedback, reflect on your performance, and continue improving your skills and interview techniques.",
    "What is the importance of internships?": "Internships provide real-world experience, networking opportunities, and can lead to job offers post-graduation.",
    "How do I balance studying and job preparation?": "Create a structured schedule, set specific goals for both academics and job prep, and allocate time for each.",
    "What is continuous learning?": "Continuous learning is the ongoing, voluntary, and self-motivated pursuit of knowledge for personal or professional development.",

    "What is an operating system?": "An operating system (OS) is software that manages computer hardware and software resources and provides common services for computer programs.",
    "What are the main functions of an operating system?": "The main functions include managing hardware resources, providing user interfaces, handling file management, and ensuring security and access control.",
    "What is a process in an OS?": "A process is a program in execution, which includes the program code, current activity, and a set of resources.",
    "What is virtual memory?": "Virtual memory is a memory management technique that allows the execution of processes that may not be completely in memory, using disk space to extend apparent memory.",
    
    "What is DBMS?": "A Database Management System (DBMS) is software that allows users to define, create, maintain, and control access to databases.",
    "What are the types of DBMS?": "The main types include Hierarchical, Network, Relational, and Object-oriented DBMS.",
    "What is normalization?": "Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity.",
    "What is a primary key?": "A primary key is a unique identifier for a record in a database table, ensuring that no two rows have the same value.",
    
    "What is a computer network?": "A computer network is a set of interconnected computers that can communicate with each other and share resources.",
    "What are the types of networks?": "The main types are LAN (Local Area Network), WAN (Wide Area Network), MAN (Metropolitan Area Network), and PAN (Personal Area Network).",
    "What is the OSI model?": "The OSI model is a conceptual framework used to understand and implement networking protocols, consisting of seven layers: Application, Presentation, Session, Transport, Network, Data Link, and Physical.",
    "What is an IP address?": "An IP address is a unique string of numbers separated by periods or colons that identifies each computer using the Internet Protocol to communicate over a network.",
    
    "What is quantitative aptitude?": "Quantitative aptitude refers to the ability to handle numbers and mathematical concepts, often assessed in competitive exams.",
    "What is logical reasoning?": "Logical reasoning is the ability to analyze and evaluate arguments and to deduce conclusions from premises.",
    "If 3x + 7 = 22, what is x?": "x = 5.",
    "In a race of 100 meters, if A beats B by 10 meters, how much distance does A cover when B covers 90 meters?": "A covers 90 meters when B covers 90 meters, so A covers 100 meters in that time.",
    
    "Describe a challenging situation you faced at work and how you handled it.": "In my last project, we encountered a major roadblock when a team member left unexpectedly. I organized a meeting to redistribute tasks, and we managed to meet our deadlines by prioritizing essential features.",
    "How do you handle stress and pressure?": "I handle stress by staying organized, prioritizing my tasks, and taking short breaks to clear my mind.",
    "Can you describe a time you worked as part of a team?": "In a group project at university, I collaborated with my peers to divide tasks based on our strengths, which resulted in a successful presentation.",
    "How do you prioritize your work?": "I prioritize my work by assessing deadlines, importance, and the impact of tasks, using tools like to-do lists to stay organized."
}

def get_faq_answer(question):
    """Return the answer to the FAQ if it exists."""
    for faq in faqs:
        if faq.lower() in question.lower():
            return faqs[faq]
    return "I'm sorry, I don't have the answer to that question."

def chatbot_response(user_input):
    """Generate a response from the chatbot."""
    if user_input.lower() == "exit":
        return "Thank you for using the chatbot. Goodbye!"
    
    # Check if the question is in the FAQ
    answer = get_faq_answer(user_input)
    
    if answer != "I'm sorry, I don't have the answer to that question.":
        return answer
    
    # If not, use the QA model for any other questions
    context = "You can prepare for placements by practicing aptitude tests, coding problems, and mock interviews."
    result = qa_pipeline(question=user_input, context=context)
    return result['answer']

# Sample interaction with the chatbot
print("Welcome to the Placement Preparation Chatbot!")
print("Ask me anything about placements. Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)
