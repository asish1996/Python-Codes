from Tkinter import *
from tkMessageBox import *
class Checkbar(Frame):

    def __init__(self, parent=None, picks=[], side=TOP, anchor=W):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.pack(side=side, anchor=anchor, expand=YES)
            self.vars.append(var)

    def state(self):
        return map((lambda var: var.get()), self.vars)

if __name__ == '__main__':
    root = Tk()
    lng = Checkbar(root, ['SMART TRANSPORTATION', 'CLIMATE CHANGE ADAPTATION', 'SUSTAINABLE WATER', 'MECHANICS, DATASCIENCE'])
    lng.pack(side=TOP, fill=X)
    lng.config(relief=GROOVE, bd=2)


    def allstates():
        user_wants = list(lng.state())
        output_indices = [i for i, e in enumerate(user_wants) if e != 0]
        mapping = {0: 'SMART TRANSPORTATION', 1: 'CLIMATE CHANGE ADAPTATION', 2: 'SUSTAINABLE WATER',3:'MECHANICS, DATASCIENCE'}
        courses = {'SMART TRANSPORTATION': ['TRAFFIC ENGINEERING,', 'INTELLIGENT TRANSPORTATION,','PROBABILITY ESTIMATION,','CSIPP,','GIS,','INFRASTRUCTURE MANAGEMENT,','DECISION ANALYTICS,',
                                             'USM,','Sensing and Data Mining,'],
                   'CLIMATE CHANGE ADAPTATION': ['USM,','CLIMATE CHANGE ADAPTATION,','INFRASTRUCTURE MANAGEMENT,','PROBABILITY ESTIMATION,','CLIMATE CHANGE SCIENCE AND SOLUTION,','GSM,' ],
                   'SUSTAINABLE WATER': ['WATER RESOURCE ENGINEERING,','FUNDEMENTALS WQ,','WATER CHEMISTRY,','FTPPO,','BIOLOGICAL WATERTREATMENT,','MODELLING EQM,','MICROBIOLOGY,'],
                   'MECHANICS, DATASCIENCE': ['Molecular Simulation of Materials,','Finite Elements in Mechanics,','PROBABILITY ESTIMATION,','DECISION ANALYTICS,','Sensing and Data Mining,']}
        # print user_wants
        output = []
        for item in output_indices:
            output.append(mapping[item])
        real_output = []
        for item in output:
            for key in courses[item]:
                real_output.append(key)
        real_output=list(set(real_output))
        # print real_output
        Button(root, text='Credits selected', command=allstates2(real_output)).pack(side=BOTTOM)
        # allstates2(real_output)
        credits(real_output)
        # print real_output

    Button(root, text='Quit', command=root.quit).pack(side=BOTTOM)
    Button(root, text='Display Courses', command=allstates).pack(side=BOTTOM)

    def allstates2(self):
        ftp = Checkbar(root, self)
        ftp.pack(side=LEFT, fill=X)
    # def allstates3(self) :
    #     user_wants1 = list(self)
    #     print user_wants1
    # #     # output_indices1 = [i for i, e in enumerate(user_wants1) if e != 0]
    #     # print output_indices1
    #     # #output_indices1 = [i for i, e in enumerate(user_wants1) if e != 0]
    #     credits(user_wants1)


    def credits(listed):
        # selectedCourses=[]
        # selectedCourses = [i for i, e in enumerate(listed) if e != 0]
        # print selectedCourses
        COurse_code={'TRAFFIC ENGINEERING,': 12, 'INTELLIGENT TRANSPORTATION,':12,'PROBABILITY ESTIMATION,':12,
                     'CSIPP,':12,'GIS,':12,'INFRASTRUCTURE MANAGEMENT,':6,'DECISION ANALYTICS,':12,'USM,':12, 'CLIMATE CHANGE ADAPTATION,':6,
                     'INFRASTRUCTURE MANAGEMENT,':6,'CLIMATE CHANGE SCIENCE AND SOLUTION,' :12,'GSM,':12,'WATER RESOURCE ENGINEERING,':12,'FUNDEMENTALS WQ,':12,
                     'WATER CHEMISTRY,':12,'FTPPO,':12,'BIOLOGICAL WATERTREATMENT,' :12,'MODELLING EQM,':12,'MICROBIOLOGY,':12,
                     'Molecular Simulation of Materials,':6,'Finite Elements in Mechanics,':12, 'Sensing and Data Mining,':6 }
        credits=0
        # showinfo('Credits selected are', listed,)
        LBL=Label(root,text=listed).pack(side=LEFT)
        print "Required Courses are "
        for item in listed:
            print item, COurse_code[item], "units"
            credits += COurse_code[item]
        print "Total credits are ", credits
        # if credits > 48:
        #     showwarning('LIMIT EXCEEDED','COURSES SELECTED ARE MORE THAN 48 CREDITS')
        # else:
        showinfo('TOTAL CREDITS ARE', credits)


        # real_output = []
        # for item in output:
        #     for key in courses[item]:
        #         real_output.append(key)
        # real_output=list(set(real_output))


        # credits = 0
        # # print selectedCourses
        # for s in selectedCourses:
        #     credits += COurse_code[s]
        #     print "Hi 2"
        #     credits.get()
        #     if credits > 48:
        #         messagebox.showwarning('Exceeding Limit of allowed credits')
        #     else:
        #         messagebox.showinfo('Credits selected are', +credits)

root.mainloop()
