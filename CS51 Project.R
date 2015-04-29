# rearranging the data so the response variable is in the end
stagec <- stagec[c("pgtime", "age", "eet", "g2", "grade", "gleason", "ploidy", "pgstat")]

# delete all missing data
stagec <- na.omit(stagec)

# Converting factors to characters for comparison
stagec$ploidy <- as.characters(stagec$ploidy)

# Divides a set on a specific column
split <- function(data, col, value)
{
  if (is.numeric(data[1,col])) {
    data$split <- as.vector(apply(data[col], 1, function(x) value >= x))}
  else if (is.character(data[1,col])) {
    data$split <- as.vector(apply(data[col], 1, function(x) value == x))
  
  set1 <- data[data$split == TRUE, ]
  set2 <- data[data$split == FALSE, ]
  set1$split <- NULL
  set2$split <- NULL
  List <- list(set1, set2)
  
  return(List)
}

# Calculates gini impurity
gini <- function(data)
{
  # Response variable is the last column
  res_col <- ncol(data)
  total <- nrow(data)
  p1 <- length(which(data[res_col]==1))
  p2 <- length(which(data[res_col]==0))
  gini_impurity <- 1 - ((p1/total)^2 + (p2/total)^2)
  
  return(gini_impurity)
}

next_branches <- function(data)
{
  current_gini <- gini(data)
  
  # Variables to track the best criteria
  best_gain <- 0
  best_criteria <- NULL
  best_sets <- NULL
  best_set1 <- NULL
  best_set2 <- NULL
  
  # Number of columns without the response
  n_col <- ncol(data) - 1
  
  # Go through each column to figure out the best information gain 
  for (i in 1:n_col)
  {
    print(paste0("At COLUMN: ", i))
    
    if (is.numeric(data[1,i])==TRUE)
    {s <- split(data,i,mean(data[,i]))}
    else
    {s <- split(data,i,as.character(data[1,i]))}
    
    
    set1 <- as.data.frame(s[1])
    set2 <- as.data.frame(s[2])
    
    p <- nrow(set1)/nrow(data)
    # Information Gain
    gain <- current_gini - (p*gini(set1) + (1-p)*gini(set2))
    print(paste0("IG is: ", gain))
    if (gain > best_gain)
    {
      best_gain <- gain
      if (is.numeric(data[1,i])==TRUE)
      {best_criteria <- c(i, mean(data[,i]))}
      else
      {best_criteria <- c(i, as.character(data[1,i]))}
      best_set1 <- set1
      best_set2 <- set2
      print("rejected")
    }
  }
  print(best_gain)
  print(best_criteria)
  return(list(best_set1, best_set2, best_criteria))
}

