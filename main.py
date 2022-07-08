from tkinter import *
import random
from PIL import Image, ImageTk

names = []
asked = []
score = 0

questions_answers = { #Questions that will be asked
    1: ["For how many days is a Test match scheduled?", '100 overs', '3 days','One day ', '5 days' ,'5 days',4],#Q1
    2: [" The Olympics are held every how many years?",'3 years','8 years','4 years', '1 year','4 years',3],#Q2
    3: ["In soccer, what body part can’t touch the ball?", 'Head','Hands','Legs','Chest','Hands',2],#Q3
    4: ["What’s the diameter of a basketball hoop in inches?",'14 Inches','16 Inches','18 Inches','20 Inches','18 Inches',3],#Q4
    5: ["Which batsman started his international cricketing career at the age of 16?",'MS Dhoni','Virat Kohli','Joe Root','Sachin Tendulkar','Sachin Tendulkar',4],#Q5
    6: ["How many players are there in a football (soccer) team?",'7','9','11','13','11',3],#Q6
    7: ["Which sport is not played with a ball?",'Basketball','Football','Cricket','Ice Hockey','Ice Hockey',4],#Q7
    8: ["Where will the 2023 Cricket World Cup be hosted?",'Australia','India','New Zealand','England','India',2],#Q8
    9: ["Which famous boxer is frequently ranked as the best heavyweight boxer of all time?",'Muhammad Ali','Tyson Fury','Mike Tyson','Anthony Joshua','Muhammad Ali',1],#Q9
    10: ["Which sport does Serena Williams play?",'Basketball','Tennis','Cricket','Football','Tennis',2],#Q10



}
def randomQuestions (): #randomises questions
    global qnum
    qnum = random.randint(1,10) # Number of questions
    if qnum not in asked:
      asked.append(qnum)
    elif qnum in asked:
      randomQuestions()
     

class Mainpage:#start page
  def __init__(self, parent):
    background_color="lightgrey"#background color

    self.heading_label=Label(window, text = "General Knowledge Sports quiz", font =( "Times","19","bold"),bg=background_color)
    self.heading_label.place(x=100, y=20)#Heading of the quiz

    self.var1=IntVar()

    self.user_label=Label(window, text="Please Enter your name Below: ", font=( "Times","18","bold"),bg=background_color)
    self.user_label.place(x=650, y=270)#name heading
    

    self.entry_box=Entry(window)
    self.entry_box.place(x=800, y=320)#entry box
    

    self.start_button = Button(window, text="START", font=( "Helvetica","13","bold"), bg="Light green",command=self.name_storage)
    self.start_button.place(x=100, y=500)#start button

  def name_storage(self): #stores names
      name = self.entry_box.get()

        # component 6 error handling

      if name == '':
            messagebox.showerror('Name is required! :(',
                                 'Please enter your name!')
      elif len(name) > 15:

        # to make sure name entered is between 1-15

            messagebox.showerror('an error has occurred!',
                                 'please enter a name between 1 and 15 characters'
                                 )
      elif name.isnumeric():
            messagebox.showerror('an error has occurred!',
                                 'Name can only consist of letters ONLY!!')
      elif not name.isalpha():

        # to make sure name entered is only letters not numbers

            messagebox.showerror('an error has occurred!', 'No Symbols Please! Please Try Again!')
      else:

        # to make sure name entered is only letters not symbols

            names.append(name)  # add name to names list declared at the beginning
            print (names)
      self.heading_label.destroy()
      self.user_label.destroy()
      self.entry_box.destroy()
      self.start_button.destroy()
      Quizpage(window)

class Quizpage:#Quiz page

  def __init__(self, parent):
    background_color="white"#background color
 
 
    self.quiz_frame = Frame(parent, bg = background_color, padx=40, pady=40)
    self.quiz_frame.grid() #frame of quiz page

    randomQuestions() #question randomiser

    self.question_label=Label(window, text = questions_answers[qnum][0], font =( "Tw Cen MT","18","bold")) #questions
    self.question_label.grid(row= 0, padx=10, pady=10)  

    self.var1=IntVar()

    self.options1 = Radiobutton(window, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.var1, pady=10)
    self.options1.grid(row=1, sticky=W)#option 1

    self.options2 = Radiobutton(window, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg=background_color, value=2, variable=self.var1, pady=10)
    self.options2.grid(row=2, sticky=W)#option 2

    self.options3 = Radiobutton(window, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg=background_color, value=3, variable=self.var1, pady=10)
    self.options3.grid(row=3, sticky=W)#option 3

    self.options4 = Radiobutton(window, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg=background_color, value=4, variable=self.var1, pady=10)
    self.options4.grid(row=4, sticky=W)#option 4

    self.confirm_button = Button(window, text="Confrim",bg="white",command=self.test_progress)
    self.confirm_button.grid(row=6)#confirm button which takes you to the next page 
    
    self.leave = Button(window, text='Leave', font=('Helvetica', '13', 'bold'), bg='red', command=self.end_screen) #leave button which takes you to the exit page 

    self.leave.place(x=0, y=250)  
    
    self.score_label  = Label(window, text ='score')
    self.score_label.grid(row= 7)  
     
     
  def questions_setup(self):
     randomQuestions()
     self.var1.set(0)
     self.question_label.config(text=questions_answers[qnum][0])
     self.options1.config(text=questions_answers[qnum][1])
     self.options2.config(text=questions_answers[qnum][2])
     self.options3.config(text=questions_answers[qnum][3])
     self.options4.config(text=questions_answers[qnum][4])

 
  def test_progress(self):
      global score
      
      scr_label=self.score_label
      choice=self.var1.get()
      if len(asked)>9:
        if choice == questions_answers[qnum][6]:
          score +=1
          scr_label.configure(text=score)
          self.confirm_button.config(text="Confirm")
        else:
          score+=0
          scr_label.configure(text="The correct answer was: "+ questions_answers[qnum][5] )
          self.confirm_button.config(text="confirm")
     
      else:
            if choice==0:
              self.confirm_button.config(text="Try Again, you didn't select an option then submit again" )
              choice=self.var1.get()
            else:
              if choice == questions_answers[qnum][6]:
                score+=1
                scr_label.configure(text=score)
                self.confirm_button.config(text="confirm")
                self.questions_setup()
      
              else:
                  score+=0
                  scr_label.configure(text="The correct answer was: " + questions_answers[qnum][5])
                  self.confirm_button.config(text="Confirmn")
                  self.questions_setup()


  def end_screen(self):
    window.destroy()
    name = names[0]
    open_end_object = end()



class end:


  def __init__(self):
      background_color = 'lightgreen'
      global window2
      window2 = Tk()
      window2.title('Exit Box')
      window2.geometry('700x600')
      self.end_frame = Frame(window2, width=700, height=600,bg=background_color)
      self.end_frame.grid(row=1)
      self.end_heading = Label(window2,text='Thank You For Trying Out The Quiz ', font=('Tw Cen Mt', 22, 'bold'), bg=background_color)
      self.end_heading.place(x=80, y=50) 
      self.exit_button = Button( 
          window2, 
          text='Exit',  
          width=10,  
          bg='lightblue', 
          font=('Tw Cen Mt', 12, 'bold'),  
          command=self.close_end,  
          ) 
      self.exit_button.place(x=260, y=200) 
      self.list_label = Label(window2, text='Do not hesitate to try again..', font=('Tw Cen Mt', 12, 'bold'), width=40, bg=background_color)
      self.list_label.place(x=110, y=100)
  
  
  def close_end(self):
      self.end_frame.destroy()
      self.end_heading.destroy()
      self.exit_button.destroy()
      self.list_label.destroy()
      window2.destroy()
  
  
  
if __name__ == '__main__':
  window = Tk()
  window.title('12CSC Quiz')
  window.geometry('700x600')
  bg_image = Image.open('img 4.jpg')
  bg_image = bg_image.resize((1000, 600), Image.ANTIALIAS)
  bg_image = ImageTk.PhotoImage(bg_image)
  image_label = Label(window, image=bg_image)
  image_label.place(x=0, y=0, relwidth=1, relheight=1)
  start_object = Mainpage(window)
  window.mainloop()