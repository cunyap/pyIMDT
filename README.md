
##main function

#get intial frequency shift
BeforeCell = initial(txt_file1)
AfterCell = initial(txt_file2)

fb = fitting(BeforeCell)
fa = fitting(AfterCell)

#Now choose either discrete (sweeps) or continous measurement (phase locked loops) that was done

faa=Sweeps(tmds-file)

#OR

faa=PLL(tdms-file)

mass=mass(fb,fa,faa)

plot(mass)

##initial
#read the txt file, give the Phase(frequceny) [the phase as function of frequency]


def initial(txt-files):


return [Frequency,Phase]



## fitting
# Function to fit Phase als Funktion von Frequency  via S5 from :https://media.nature.com/original/nature-assets/nature/journal/v550/n7677/extref/nature24288-s1.pdf

def fitting(Frequency, Phase):


return resonance



## mass
#Function to calculate mass from this according to S1 from same pdf. 

def mass(initial frequency, frequencies after cell pickup , following frequencies)


return []   #mass as a function of frequency


##Sweeps
#Function to extract the subsquent resonance frequencies from following sweeps
#open tdms file, extract the data on third tab, loop over it using the fitting function, return a list of resonance frequencies.
def sweeps (tdms file):
    
#extract freq and phase    
#loops over fitting

return [list of resonance frequencies] 

##PLL
def pll (tdms file)

#extract frequency shifts

return [list of resonance frequencies]
    
##Plot
#Function to plot mass over time
