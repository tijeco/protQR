args <- commandArgs(TRUE)
x <- as.double(args[1])

dat <- read.csv(x)


scaled.dat <- scale(dat)

write.csv(scaled.dat,file="tmp.csv")
