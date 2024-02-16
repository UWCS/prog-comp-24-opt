MAKEFLAGS += --warn-undefined-variables
SHELL := bash


# Set some default values to run the job with. These can be modified here or
# overriden as environment variables
export GRID_SIZE ?= 100
export NUM_AGENTS ?= 100


# Run the job on your local computer
.PHONY: local
local:
	@cd bonus/ && ./run.sbatch

# Try to check the output of the job against an expected value
.PHONY: check
check:
	@cd bonus/ && ./run.sbatch 1>../result.out 2>/dev/null
	@diff result.out "expected/${GRID_SIZE}_${NUM_AGENTS}.out"
	@echo "Program is equivalent for size=${GRID_SIZE} and agents=${NUM_AGENTS}"

# Run the job on the DCS batch compute system
.PHONY: batch
batch:
	@cd bonus/ && sbatch run.sbatch


# Zip up the contents of the directory for submission
.PHONY: submission
submission:
	@rm submission.zip && zip -r submission.zip bonus/
