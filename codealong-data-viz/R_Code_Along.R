##Loading Excel Package
install.packages( "xlsx")
library("xlsx")

##Load data/ Create dataframe
T2H<-read.xlsx("//e04tcv-CIFS02.ent.ds.gsa.gov/R05_PUBLIC$/time-to-hire-data-file.xlsx", 1)

# Review dataframe
summary(T2H)

## data transformations ##

# Calculate time to hire dimension
T2H$T2H_days<-as.numeric(difftime( T2H$HIRED_DATE, T2H$RECEIVED_DATE, units = "days"))

# First four of the job series, convert to integer and then to string
T2H$series_clean<-factor(as.numeric(substr(T2H$SERIES, 1, 4)))

# Create year hired
T2H$HIRED_DATE_CY<-factor(format(T2H$HIRED_DATE, "%Y"))

## subset data frame ##

# subset T2H with positive values
T2H<-subset(T2H, T2H$T2H_days>=0 & T2H$HIRE_COUNT>0)
summary(T2H)


### crosstab 
table(T2H$HIRED_DATE_CY, T2H$HIRE_COUNT)

# Comparison - column graph
T2H$HIRED_DATE_CY_flipped<-factor(T2H$HIRED_DATE_CY, levels = c("2010", "2009", "2008", "2007", "2006", "2005", "2004" ))
barplot(table(T2H$HIRE_COUNT, T2H$HIRED_DATE_CY_flipped), xlab="Hires", ylab="Calendar Year", main = "Hires by CY",
        col="black", horiz=TRUE)

# Comparison - bar graph
barplot(table(T2H$HIRE_COUNT, T2H$HIRED_DATE_CY), xlab="Calendar Year", ylab="Hires", main = "Hires by CY",
        col="black")

# Histogram - T2H overall 
barplot(T2H$T2H_days, ylab="Days to Hire", xlab="Hiring Instances", main= "Histogram - T2H")
#Flip hiring instances on Y axis
plot(factor(T2H$T2H_days), ylab="Hiring Instances", xlab="Time to Hire", main= "Histogram - T2H")

#By bins
plot(factor(cut(T2H$T2H_days, 8)), ylab="Hiring Instances", xlab="Time to Hire", main= "Histogram - T2H Binned")

###Breaks to identify ideal number of bins
plot(factor(cut(T2H$T2H_days, breaks = seq(0, 500, by = 40))), ylab="Hiring Instances", xlab="Time to Hire", main= "Histogram - T2H Binned Ideal")

#Box an whisker
boxplot(T2H$T2H_days, ylab="Days to Hire", main= "Boxplot - T2H", outline = F, col="light blue")

# subset for 1101s, 1102s, 1170s and 1176 
T2H_1100s<-subset(T2H, T2H$series_clean=="1101" | T2H$series_clean=="1102"|
                    T2H$series_clean=="1170" | T2H$series_clean=="1176")  
T2H_1100s$series_clean<-droplevels(T2H_1100s$series_clean)

# Box & wisker - T2H distribution for 4 or 5 series (1101, 1102, 1170, 1176)

boxplot( T2H_1100s$T2H_days~T2H_1100s$series_clean,  ylab="Days to Hire", outline=F, col="light blue", main="Box and Whisker Plots by Job Series") 
stripchart(T2H_1100s$T2H_days~T2H_1100s$series_clean,
           vertical = TRUE, method = "jitter", 
           pch = 21, col = "black", bg = "beige", 
           add = TRUE) 

### Using R for ANOVA - t-test for 1101s & 1102s
T2H_1110Xs<-subset(T2H_1100s, T2H_1100s$series_clean=="1102" | T2H_1100s$series_clean=="1101")
t.test(T2H_1110Xs$T2H_days~T2H_1110Xs$series_clean)

####

# Comparison line chart - # of 1102 hires by month/year
plot(T2H$HIRED_DATE[T2H$series_clean=="1102"], T2H$HIRE_COUNT[T2H$series_clean=="1102"], type="l", xlab="Hire Date", ylab = "Hire Count", main = "Hire Count over Time for 1102s - Line Graph")

plot(T2H$HIRED_DATE, T2H$HIRE_COUNT, type="l", xlab="Hire Date", ylab = "Hire Count", main = "Hire Count over Time for All Employees - Line Graph")

plot(T2H$HIRED_DATE, T2H$HIRE_COUNT, xlab="Hire Date", ylab = "Hire Count", main = "Hire Count over Time for All Employees - Line Graph")



# Scatterplots
###########################

plot(T2H$HIRED_DATE[T2H$series_clean=="1102"], T2H$T2H_days[T2H$series_clean=="1102"], xlab="Year", ylab="Time to Hire Days", main = "T2H for 1102s")

#T2H Scatterplot - All Employees
plot(T2H$HIRED_DATE[T2H$T2H_days<=500], T2H$T2H_days[T2H$T2H_days<=500], xlab="Year", ylab="Time to Hire Days", main = "T2H for All Employees")

#Applicants vs hires
plot(   T2H$HIRE_COUNT, T2H$APPLICATION_COUNT, xlab = "Hires", ylab = "Applicants", main = "Applicants vs Hires")

