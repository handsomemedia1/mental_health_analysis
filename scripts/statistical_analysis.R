# Install and load required packages
if (!requireNamespace("tidyverse", quietly = TRUE)) install.packages("tidyverse")
if (!requireNamespace("ggplot2", quietly = TRUE)) install.packages("ggplot2")
if (!requireNamespace("rmarkdown", quietly = TRUE)) install.packages("rmarkdown")
if (!requireNamespace("knitr", quietly = TRUE)) install.packages("knitr")

library(tidyverse)
library(ggplot2)
library(knitr)

# Load the dataset
df <- read.csv("../data/processed/mental_health_tech_analyzed.csv")

# Convert relevant columns to factors
factor_cols <- c("self_employed", "tech_company", "mental_health_benefits", 
                "mental_health_benefits_awareness", "employer_mental_health_discussion",
                "employer_mental_health_learning_resources", "mental_health_treatment_anonymity",
                "mental_health_leave_accessibility", "mental_health_discussion_comfort_coworkers",
                "mental_health_discussion_comfort_supervisor")

df[factor_cols] <- lapply(df[factor_cols], as.factor)
df$year <- as.factor(df$year)

# 1. Chi-square tests for association between company type and mental health benefits
tech_benefits_test <- chisq.test(table(df$tech_company, df$mental_health_benefits))

# 2. Chi-square test for association between company size and mental health benefits
size_benefits_test <- chisq.test(table(df$number_of_employees, df$mental_health_benefits))

# 3. Test for trend over years
# Convert year back to numeric for this test
df$year_num <- as.numeric(as.character(df$year))
year_trend_model <- glm(mental_health_benefits_binary ~ year_num, 
                        family = binomial(link = "logit"), 
                        data = df)

# 4. Logistic regression for predicting mental health benefits
logit_model <- glm(mental_health_benefits_binary ~ self_employed + tech_company + number_of_employees,
                  family = binomial(link = "logit"),
                  data = df)

# 5. Comfort level analysis
comfort_model <- glm(mental_health_discussion_comfort_supervisor_binary ~ 
                     mental_health_benefits_binary + employer_mental_health_discussion_binary,
                     family = binomial(link = "logit"),
                     data = df)

# Create a summary document with all statistical results
sink("../reports/statistical_analysis_results.txt")

cat("STATISTICAL ANALYSIS OF MENTAL HEALTH IN TECH SURVEY\n")
cat("=====================================================\n\n")

cat("1. ASSOCIATION BETWEEN TECH COMPANIES AND MENTAL HEALTH BENEFITS\n")
cat("----------------------------------------------------------------\n")
print(tech_benefits_test)
cat("\n\n")

cat("2. ASSOCIATION BETWEEN COMPANY SIZE AND MENTAL HEALTH BENEFITS\n")
cat("-------------------------------------------------------------\n")
print(size_benefits_test)
cat("\n\n")

cat("3. TREND ANALYSIS OVER YEARS\n")
cat("---------------------------\n")
print(summary(year_trend_model))
cat("\n\n")

cat("4. PREDICTORS OF MENTAL HEALTH BENEFITS\n")
cat("-------------------------------------\n")
print(summary(logit_model))
cat("\n\n")

cat("5. FACTORS AFFECTING COMFORT DISCUSSING WITH SUPERVISOR\n")
cat("-----------------------------------------------------\n")
print(summary(comfort_model))
cat("\n\n")

sink()

# Create visualizations for the statistical analysis
# Create directory for R figures
dir.create("../reports/figures/r_analysis", showWarnings = FALSE, recursive = TRUE)

# 1. Visualize odds ratios from logistic regression
# Extract odds ratios and confidence intervals
odds_ratios <- exp(cbind(OR = coef(logit_model), confint(logit_model)))
odds_df <- as.data.frame(odds_ratios)
odds_df$Variable <- rownames(odds_df)
odds_df <- odds_df[-1,] # Remove intercept

# Plot odds ratios
png("../reports/figures/r_analysis/odds_ratios.png", width=800, height=600)
ggplot(odds_df, aes(x=reorder(Variable, OR), y=OR)) +
  geom_point(size=3) +
  geom_errorbar(aes(ymin=`2.5 %`, ymax=`97.5 %`), width=.2) +
  coord_flip() +
  geom_hline(yintercept=1, linetype="dashed", color="red") +
  labs(title="Odds Ratios for Predictors of Mental Health Benefits",
       x="Variable", y="Odds Ratio (95% CI)") +
  theme_minimal(base_size=14)
dev.off()

# Save model results as RDS for potential later use
saveRDS(logit_model, "../models/benefits_logistic_model.rds")
saveRDS(comfort_model, "../models/comfort_logistic_model.rds")

cat("Statistical analysis complete! Results saved to reports directory.\n")