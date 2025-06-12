print("Welcome to personality test")
name = input("Please enter your name:")
email = input("Please enter your email:")
print("1.Strongly Disagree")
print("2.Agree")
print("3.Neutral")
print("4.Agree")
print("5.Strongly Agree")
print("Type your answer from 1 to 5")
print()
#Extraversion (E)
#Introversion (I)
#Sensing (S)
#Intuition (N)
#Thinking (T)
#Feeling (F)
#Judging (J)
#Perceivign (P)


class Person:
    def __init__(self, EI, SN, TF, JP):
        self.EI = EI
        self.SN = SN
        self.TF = TF
        self.JP = JP
    def add_point(self, point):
        self.EI += point
    def add_point2(self, point2):
        self.SN += point2
    def add_point3(self, point3):
        self.TF += point3
    def add_point4(self, point4):
        self.JP += point4

def get_valid_input():
    while True:
        try:
            ans = int(input("Answer from 1 to 5: "))
            if 1 <= ans <= 5:
                return ans
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

personality = Person(0, 0, 0, 0)

print("1.You enjoy being the center of attention.")
ei1 = get_valid_input()
personality.add_point(ei1)
print()
print("2.You prefer spending weekends out with a big group of friends even though you are not close to them.")
ei2 = get_valid_input()
personality.add_point(ei2)
print()
print("3.You often speak before thinking things through.")
ei3 = get_valid_input()
personality.add_point(ei3)
print()
print("4.You feel bored or lonely when you're by yourself for too long")
ei4 = get_valid_input()
personality.add_point(ei4)
print()
print("5.You often find yourself starting conversations with strangers.")
ei5 = get_valid_input()
personality.add_point(ei5)
print()

print("6.You focus more on future possibilities than present details..")
sn1 = get_valid_input()
personality.add_point2(sn1)
print()
print("7.You enjoy discussing abstract or theoretical ideas.")
sn2 = get_valid_input()
personality.add_point2(sn2)
print()
print("8.You prefer exploring new ideas rather than following proven methods.")
sn3 = get_valid_input()
personality.add_point2(sn3)
print()
print("9.You trust your gut feelings more than hard facts.")
sn4 = get_valid_input()
personality.add_point2(sn4)
print()
print("10.You like thinking about what could be rather than what is?")
sn5 = get_valid_input()
personality.add_point2(sn5)
print()

print("11.You make decisions based more on logic than emotions.")
tf1 = get_valid_input()
personality.add_point3(tf1)
print()
print("12.You believe fairness is more important than kindness.")
tf2 = get_valid_input()
personality.add_point3(tf2)
print()
print("13.You value being right over keeping the peace.")
tf3 = get_valid_input()
personality.add_point3(tf3)
print()
print("14.You find it easy to separate feelings from facts..")
tf4 = get_valid_input()
personality.add_point3(tf4)
print()
print("15.You focus more on tasks than on how people feel about them.")
tf5 = get_valid_input()
personality.add_point3(tf5)
print()

print("16.You prefer having a detailed plan rather than going with the flow.")
jp1 = get_valid_input()
personality.add_point4(jp1)
print()
print("17.You feel stressed when things are left unfinished.")
jp2 = get_valid_input()
personality.add_point4(jp2)
print()
print("18.You like sticking to schedules and routines..")
jp3 = get_valid_input()
personality.add_point4(jp3)
print()
print("19.You often make decisions quickly and confidently..")
jp4 = get_valid_input()
personality.add_point4(jp4)
print()
print("20.You dislike last-minute changes to your plans.")
jp5 = get_valid_input()
personality.add_point4(jp5)
print()

print(f'Score of EI: {personality.EI}')
print(f'Score of SN: {personality.SN}')
print(f'Score of TF: {personality.TF}')
print(f'Score of JP: {personality.JP}')


def get_personality_type(p):
    if p.EI >= 15:
        ei_letter = 'E'
    else:
        ei_letter = 'I'
    if p.SN >= 15:
        sn_letter = 'S'
    else:
        sn_letter = 'N'
    if p.TF >= 15:
        tf_letter = 'T'
    else:
        tf_letter = 'F'
    if p.JP >= 15:
        jp_letter = 'J'
    else:
        jp_letter = 'P'

    return ei_letter + sn_letter + tf_letter + jp_letter


def print_personality_description(type_code):
    descriptions = {
        "ISTJ": "ISTJ - Quiet, serious, earn success by being thorough and dependable. Practical, matter-of-fact, realistic, and responsible. Decide logically what should be done and work toward it steadily, regardless of distractions. Take pleasure in making everything orderly and organized—their work, their home, their life. Value traditions and loyalty..",
        "ISFJ": "ISFJ - Quiet, friendly, responsible, and conscientious. Committed and steady in meeting their obligations. Thorough, painstaking, and accurate. Loyal, considerate, notice and remember specifics about people who are important to them, concerned with how others feel. Strive to create an orderly and harmonious environment at work and at home.",
        "INFJ": "INFJ - Seek meaning and connection in ideas, relationships, and material possessions. Want to understand what motivates people and are insightful about others. Conscientious and committed to their firm values. Develop a clear vision about how best to serve the common good. Organized and decisive in implementing their vision..",
        "INTJ": "INTJ - Have original minds and great drive for implementing their ideas and achieving their goals. Quickly see patterns in external events and develop long-range explanatory perspectives. When committed, organize a job and carry it through. Skeptical and independent, have high standards of competence and performance—for themselves and others.",
        "ISTP": "ISTP - Tolerant and flexible, quiet observers until a problem appears, then act quickly to find workable solutions. Analyze what makes things work and readily get through large amounts of data to isolate the core of practical problems. Interested in cause and effect, organize facts using logical principles, value efficiency.",
        "ISFP": "ISFP - Quiet, friendly, sensitive, and kind. Enjoy the present moment, what's going on around them. Like to have their own space and to work within their own time frame. Loyal and committed to their values and to people who are important to them. Dislike disagreements and conflicts; don't force their opinions or values on others.",
        "INFP": "INFP - Idealistic, loyal to their values and to people who are important to them. Want to live a life that is congruent with their values. Curious, quick to see possibilities, can be catalysts for implementing ideas. Seek to understand people and to help them fulfill their potential. Adaptable, flexible, and accepting unless a value is threatened.",
        "INTP": "INTP - Seek to develop logical explanations for everything that interests them. Theoretical and abstract, interested more in ideas than in social interaction. Quiet, contained, flexible, and adaptable. Have unusual ability to focus in depth to solve problems in their area of interest. Skeptical, sometimes critical, always analytical.",
        "ESTP": "ESTP - Flexible and tolerant, take a pragmatic approach focused on immediate results. Bored by theories and conceptual explanations; want to act energetically to solve the problem. Focus on the here and now, spontaneous, enjoy each moment they can be active with others. Enjoy material comforts and style. Learn best through doing.",
        "ESFP": "ESFP - Outgoing, friendly, and accepting. Exuberant lovers of life, people, and material comforts. Enjoy working with others to make things happen. Bring common sense and a realistic approach to their work and make work fun. Flexible and spontaneous, adapt readily to new people and environments. Learn best by trying a new skill with other people.",
        "ENFP": "ENFP - Warmly enthusiastic and imaginative. See life as full of possibilities. Make connections between events and information very quickly, and confidently proceed based on the patterns they see. Want a lot of affirmation from others, and readily give appreciation and support. Spontaneous and flexible, often rely on their ability to improvise and their verbal fluency.",
        "ENTP": "ENTP - Quick, ingenious, stimulating, alert, and outspoken. Resourceful in solving new and challenging problems. Adept at generating conceptual possibilities and then analyzing them strategically. Good at reading other people. Bored by routine, will seldom do the same thing the same way, apt to turn to one new interest after another",
        "ESTJ": "ESTJ - Practical, realistic, matter-of-fact. Decisive, quickly move to implement decisions. Organize projects and people to get things done, focus on getting results in the most efficient way possible. Take care of routine details. Have a clear set of logical standards, systematically follow them and want others to also. Forceful in implementing their plans..",
        "ESFJ": "ESFJ - Warmhearted, conscientious, and cooperative. Want harmony in their environment, work with determination to establish it. Like to work with others to complete tasks accurately and on time. Loyal, follow through even in small matters. Notice what others need in their day-to-day lives and try to provide it. Want to be appreciated for who they are and for what they contribute.",
        "ENFJ": "ENFJ - Warm, empathetic, responsive, and responsible. Highly attuned to the emotions, needs, and motivations of others. Find potential in everyone, want to help others fulfill their potential. May act as catalysts for individual and group growth. Loyal, responsive to praise and criticism. Sociable, facilitate others in a group, and provide inspiring leadership.",
        "ENTJ": "ENTJ - Frank, decisive, assume leadership readily. Quickly see illogical and inefficient procedures and policies, develop and implement comprehensive systems to solve organizational problems. Enjoy long-term planning and goal setting. Usually well informed, well read, enjoy expanding their knowledge and passing it on to others. Forceful in presenting their ideas."
    }
    print()
    print(f"Your personality type is: {type_code}")
    print(descriptions.get(type_code, "No description available for this type."))

# Get type and show result
initialize = get_personality_type(personality)
print(name, "this is your personality type:")
print_personality_description(initialize)


