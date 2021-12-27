
## Problem data
set.seed(10)
n <- 10
SAMPLES <- 100
mu <- matrix(abs(rnorm(n)), nrow = n)
Sigma <- matrix(rnorm(n^2), nrow = n, ncol = n)
Sigma <- t(Sigma) %*% Sigma
  
## Form problem
#w <- Variable(n)
w <- runif(n)
w <- w/sum(w)
ret <- t(mu) %*% w
risk <- quad_form(w, Sigma)
constraints <- list(w >= 0, sum(w) == 1)
    
## Risk aversion parameters
gammas <- 10^seq(-2, 3, length.out = SAMPLES)
ret_data <- rep(0, SAMPLES)
risk_data <- rep(0, SAMPLES)
w_data <- matrix(0, nrow = SAMPLES, ncol = n)

## Compute trade-off curve
for(i in seq_along(gammas)) {
  gamma <- gammas[i]
  objective <- ret - gamma * risk
  prob <- Problem(Maximize(objective), constraints)
  result <- solve(prob)
  
  ## Evaluate risk/return for current solution
  risk_data[i] <- result$getValue(sqrt(risk))
  ret_data[i] <- result$getValue(ret)
  w_data[i,] <- result$getValue(w)
}

result$getValue(risk)
result$getValue(ret)

cbPalette <- brewer.pal(n = 10, name = "Paired")
p1 <- ggplot() +
  geom_line(mapping = aes(x = risk_data, y = ret_data), color = "blue") +
  geom_point(mapping = aes(x = sqrt(diag(Sigma)), y = mu), color = "red")

markers_on <- c(10, 20, 30, 40)
nstr <- sprintf("gamma == %.2f", gammas[markers_on])
df <- data.frame(markers =  markers_on, x = risk_data[markers_on],
                 y = ret_data[markers_on], labels = nstr)

p1 + geom_point(data = df, mapping = aes(x = x, y = y), color = "black") +
  annotate("text", x = df$x + 0.2, y = df$y - 0.05, label = df$labels, parse = TRUE) +
  labs(x = "Risk (Standard Deviation)", y = "Return")

w_df <- data.frame(paste0("grp", seq_len(ncol(w_data))),
                   t(w_data[markers_on,]))
names(w_df) <- c("grp", sprintf("gamma == %.2f", gammas[markers_on]))
tidyW <- gather(w_df, key = "gamma", value = "fraction", names(w_df)[-1], factor_key = TRUE)
ggplot(data = tidyW, mapping = aes(x = gamma, y = fraction)) +
  geom_bar(mapping = aes(fill = grp), stat = "identity") +
  scale_x_discrete(labels = parse(text = levels(tidyW$gamma))) +
  scale_fill_manual(values = cbPalette) +
  guides(fill = FALSE) +
  labs(x = "Risk Aversion", y = "Fraction of Budget")