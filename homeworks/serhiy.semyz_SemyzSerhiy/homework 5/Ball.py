class Ball:
     def __init__(self,name,form,material):
         self.name=name
         self.form=form
         self.material=material


     def __str__(self):

         return 'name is %s the form is %s material is %s' %(self.name,self.form,self.material)







