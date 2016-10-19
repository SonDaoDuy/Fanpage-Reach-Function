library(rgl)

mydata = read.table("getdata.txt")

reach = mydata[,1]
boost = mydata[,2]
like = mydata[,3]
share = mydata[,4]
#num_of_sample = length(reach)

mean_reach = mean(reach)
sd_reach = sd(reach)
list = c()

# for(i in 1:1114){
#     if(!is.na(mean_reach) && !is.na(sd_reach) && !is.na(reach[i]) && ((reach[i] - mean_reach)^2 >= (sd_reach)^2)){
#         list = c(list, -i)
#     }
# }

for(i in 1:1114){
    if(!is.na(mean_reach) && !is.na(sd_reach) && !is.na(reach[i]) && (reach[i] >= 200000)){
        list = c(list, -i)
    }
}

reach = reach[list]
boost = boost[list]
like = like[list]
share = share[list]

write (reach,file = "reach.txt",ncolumns = 1,append = FALSE,sep="")
write(boost,file = "boost.txt",ncolumns = 1,append = FALSE,sep = "")
write (like,file = "like.txt",ncolumns = 1,append = FALSE,sep="")
write (share,file = "share.txt",ncolumns = 1,append = FALSE,sep="")

#length(reach)
#plot3d(share,like,reach)
