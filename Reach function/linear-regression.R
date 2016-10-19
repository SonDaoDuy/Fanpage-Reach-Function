library(plot3D)

# x, y, z variables
reach = read.table("reach.txt")
boost = read.table("boost.txt")
like = read.table("like.txt")
share = read.table("share.txt")
z = reach[,1]
t = boost[,1]
y = like[,1]
x = share[,1]
# Compute the linear regression (z = ax + by + d)
fit <- lm(z ~ y + x + t)
# predict values on regular xy grid
# grid.lines = 26
# x.pred <- seq(min(x), max(x), length.out = grid.lines)
# y.pred <- seq(min(y), max(y), length.out = grid.lines)
# #t.pred <- seq(min(t), max(t), length.out = grid.lines)
# xy <- expand.grid( x = x.pred, y = y.pred)
# z.pred <- matrix(predict(fit, newdata = xy), 
#                  nrow = grid.lines, ncol = grid.lines)
# fitted points for droplines to surface
fitpoints <- predict(fit)
# scatter plot with regression plane
# scatter3D(x, y, z, pch = 18, cex = 2, 
#     theta = 20, phi = 20, ticktype = "detailed",
#     xlab = "share", ylab = "like", zlab = "reach",  
#     surf = list(x = x.pred, y = y.pred, z = z.pred,  
#     facets = NA, fit = fitpoints))
write(fitpoints,file = "fitpoints.txt",ncolumns = 1,append = FALSE,sep = "")


for (i in 1:length(y)){
	write(coefficients(fit)[2]*y[i] + coefficients(fit)[3]*x[i] + coefficients(fit)[4]*t[i],
		file = "testresult.txt",ncolumns = 1,append = TRUE,sep = "")
}
write(coefficients(fit),file = "model.txt",ncolumns = 4,append = FALSE,sep = " ")
# y[2]
# coefficients(fit)[2]
#fitpoints
#plot(fitpoints)