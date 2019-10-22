# Let's import the dataset and get a feel for what's going on.

rm(list=ls())
data <- read.csv('C:/Users/ryang/prop_prices.csv', header=TRUE)

head(data,10)

tail(data,10)

summary(data)

sum(complete.cases(data))

print("Test")

# Some stuff to protect against headaches
data$sale_def <- data$sale_def/1000

price <- new_data$sale_def  
beds <- new_data$bed
area <- new_data$area_heated
pool <- new_data$pool




# Building simple linear models and plotting the data to get a better feel for it.


attach(data)
pairs(price ~ beds + area + pool, data, pch= ".")
boxplot(price ~ beds, outline=FALSE)
lm_1 <- lm(price ~ area)
lm_1
plot(area, price,
     ylim=c(0,1000),
     xlim=c(0,5000),
     type = "p",
     main = "Sales Price versus Home Size",
     xlab = "Home Size",
     ylab = "Price",
     col ="blue",
     pch = 20)
abline(lm_1, col ="red")
resids <- residuals(lm_1)
mean(resids)
hist(resids)
anova(lm_1)
summary(lm_1)
lm_2 <- lm(formula=price ~ area + 0)
summary(lm_2) 


# Investigating outliers in the dataset. 
install.packages("car")
library("car")
lm_nt <- lm(price ~ area)
lm_nt
plot(area, price,
     ylim=c(0,1000),
     xlim=c(0,5000),
     type = "p",
     main = "Sales Price versus Home Size",
     xlab = "Home Size",
     ylab = "Price",
     col ="blue",
     pch = 20)
abline(lm_nt, col ="red")
resids <- rstandard(lm_nt)
plot(area, resids,
     type = "p",
     xlim=c(0,5000),
     main = "Residuals vs Home Size",
     xlab = "Home Size",
     ylab = "Residuals",
     col = "red",
     pch = 19)
plot(resids, price,
          ylim=c(0,1000),
          type = "p",
          main = "Sales Price versus Residuals",
          xlab = "Residuals",
          ylab = "Price",
          col ="purple",
          pch = 18)
hist(resids)
qqnorm(resids)
qqline(resids)
par(mfrow = c(2,2))
plot(lm_nt)
data[37,]
data[214,]
data[638,]
data_out<- data[-c(37),] 
data_out1 <- data_out[-c(214),]
data_out2 <- data_out1[-c(638),]
new_data <- data_out2


new_price <- price - min(price,na.ram=TRUE) + 1
new_area <- area - min(area, na.ram=TRUE) + 1

car::powerTransform(new_price ~ new_area)

par(mfrow = c(2,2))
plot(area, price,
     ylim=c(0,1000),
     type = "p",
     main = "Sales Price versus Home Size",
     xlab = "Home Size",
     ylab = "Price",
     col ="blue",
     pch = 18)
plot(area, new_price,
     ylim=c(0,1000),
     type = "p",
     main = "Sales Price versus Home Size",
     xlab = "Home Size",
     ylab = "New Price",
     col ="red",
     pch = 18)
plot(new_area, price,
     ylim=c(0,1000),
     type = "p",
     main = "Sales Price versus Home Size",
     xlab = "New Home Size",
     ylab = "Price",
     col ="purple",
     pch = 18)
plot(new_area, new_price,
     ylim=c(0,1000),
     type = "p",
     main = "Sales Price versus Home Size",
     xlab = "New Home Size",
     ylab = "New Price",
     col ="red",
     pch = 18)

lm_pt <- lm(new_data$sale_def ~ new_data$area_heated, data=new_data)
lm_pt
abline(lm_pt, col ="red")
plot(new_data$area_heated, new_data$sale_def,
     type = "p",
     main = "Sales Price versus Home Size",
     xlab = "Home Size",
     ylab = "Price",
     col ="blue",
     pch = 20)

# Trying out some simple quadratic models to see if they are helpful

install.packages('boot', dependencies = TRUE, repos= 'http://cran.rstudio.com/')
library(boot)

beds2 <- beds^2
area2 <- area^2
pool2 <- pool^2

qm_1 <- lm(price ~ beds + beds2)

qm_2 <- lm(price ~ area + area2)

qm_3 <- lm(price ~ pool + pool2)

lm_1 <- lm(price ~ beds)

lm_2 <- lm(price ~ area)

lm_3 <- lm(price ~ pool)

hm_new_data <- data.frame(beds, area, pool)
pairs(hm_new_data)

summary.aov(qm_1)
summary.aov(lm_1)

summary.aov(qm_2)
summary.aov(lm_2)

summary.aov(qm_3)
summary.aov(lm_3)

# Building a multivariate model to better specify the relationship 
# between the response and explanatory variables

price <- new_data$sale_def  
beds <- new_data$bed
area <- new_data$area_heated
pool <- new_data$pool

mrm <- lm(price ~ beds + area + pool + 
            new_data$bath + new_data$area_heated + new_data$dist_cbd + 
            new_data$dist_lakes + new_data$saleyymm + new_data$property_id + 
            new_data$pcode, data = new_data)
summary(mrm)

pairs(new_data)

# Removing explantory variables to find a more parsimonious model
# Step 1 - Remove ordinal variables

mrm2 <- lm(price ~ beds + area + pool + 
            new_data$bath + new_data$area_heated + new_data$dist_cbd + 
            new_data$dist_lakes + new_data$saleyymm, 
            data = new_data)
summary(mrm2)

# Step 2 - Remove insignificant variables (in a linear regression setting)

mrm3 <- lm(price ~ beds + area + 
             new_data$bath + new_data$area_heated + 
             new_data$dist_cbd + new_data$saleyymm, 
             data = new_data)
summary(mrm3)

 # Step 3 - Remove clunky variables 

mrm4 <- lm(price ~ beds + area + new_data$bath + 
             new_data$area_heated + 
             new_data$dist_cbd, 
             data = new_data)
summary(mrm4)

par(mfrow = c(3,3))
plot(area, price,
     ylim = c(0,1.0),
     type = "p",
     main = "Sales Price versus Parcel Size",
     xlab = "Parcel Size",
     ylab = "Price",
     col ="blue",
     pch = 18)
plot(beds, price,
     ylim = c(0,1.0),
     type = "p",
     main = "Sales Price versus Number of Bedrooms",
     xlab = "Beds",
     ylab = "Price",
     col ="red",
     pch = 18)
plot(new_data$bath, price,
     ylim = c(0,1.0),
     type = "p",
     main = "Sales Price versus Number of Bathrooms",
     xlab = "Bathrooms",
     ylab = "Price",
     col ="pink",
     pch = 18)
plot(pool, price,
     ylim = c(0,1.0),
     type = "p",
     main = "Sales Price versus Pool",
     xlab = "Pool",
     ylab = "Price",
     col ="pink",
     pch = 18)
plot(new_data$area_heated, price,
     ylim = c(0,1.0),
     type = "p",
     main = "Sales Price versus Home Size",
     xlab = "Home Size",
     ylab = "Price",
     col ="purple",
     pch = 18)
plot(new_data$dist_cbd, price,
     ylim = c(0,1.0),
     type = "p",
     main = "Sales Price versus distance from CBD",
     xlab = "Proximity to Central Business District",
     ylab = "Price",
     col ="black",
     pch = 18)


