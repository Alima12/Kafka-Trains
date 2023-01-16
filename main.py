import os
import openai

a = """
About Snapp

Snapp is the pioneer provider of ride-hailing mobile solutions in Iran. It connects smartphone owners who need a ride to Snapp drivers who use their private cars, offering transportation services. We are ambitious, passionate, engaged, and excited about pushing the boundaries of the transportation industry to new frontiers and be the first choice of each user in Iran.



About the Team
Snapp is facing many problems in the case of scalability as a super fast-growing startup. As the Charlie team, we work on high loads and intelligent applications, identify bottlenecks, and re-architecture Snapp Monolith.
Join us if you like to face challenges and affect the lives of millions of people. We are open to contributions and willing to help anyone who gets started.

About the Role
We’re looking for a software engineer who will play a challenging role in enhancing, optimizing, redesigning, rewriting our current application infrastructure with full-stack technologies. Our software engineer must know all stages of software development.

Responsibilities
Estimate and design for small increments of work.
Communicate effectively with a positive and confident attitude.
Mentoring, sharing knowledge, and helping ensure effective coding practices.
Unit and integration tests as well as code reviews and pair-programming.
Research technologies/methodologies, explore alternative solutions and implementations, critically evaluate trade-offs.
Design and implement distributed, scalable, high-performance micro-service-based applications.
Work with high-end infrastructure technologies like Openshift that you cannot find it everywhere.

Requirements
Strong understanding of good design principle
Comfortable with an agile, flexible approach to feature development
Unit testing or component testing
A strong “Automation First” mentality
Experience in one of the programming languages like go, Python, 
Has experience in building Restful Web services.
Has experience using GIT for source version control
Familiar with Docker and Linux

Familiarity with SQL and relational databases (MySQL, PostgreSQL) and NoSQL databases (MongoDB, Redis)

"""

openai.api_key = "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"

response = openai.Completion.create(model="text-davinci-003", prompt=f"I want to apply for this job position. this is the job description: {a}\nWrite an about me for my resume.", temperature=0.5, max_tokens=1024, n=1, stop=None)
print(response.choices[0].text)

