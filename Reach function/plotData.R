mydata = read.table("getdata.txt")

reach = mydata[,1]
share = mydata[,4]
#num_of_sample = length(reach)

mean_reach = mean(reach)
sd_reach = sd(reach)
list = c()

for(i in 1:1114){
    if(!is.na(mean_reach) && !is.na(sd_reach) && !is.na(reach[i]) && ((reach[i] - mean_reach) >= (sd_reach))){
        list = c(list, -i)
    }
}
reach = reach[list]
share = share[list]
length(reach)
plot(share,reach)