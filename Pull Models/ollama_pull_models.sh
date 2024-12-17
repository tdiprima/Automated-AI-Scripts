#!/bin/bash
# Author: Tammy DiPrima
# Adapted for RHEL from code by: Matt Williams @technovangelist

# Extract model names from ollama ls command excluding the first row (header)
model_names=$(ollama ls | tail -n +2 | cut -d' ' -f1)

# Iterate over each model name and pull it using ollama pull command
echo "$model_names" | while read -r model; do
    # Uncomment the following line to test without actually pulling models
    echo "Test: Pulling model: $model"

    # Comment the following line out for testing, and uncomment for real execution
    # ollama pull "$model"
done
