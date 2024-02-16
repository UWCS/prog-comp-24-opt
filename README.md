# Bonus Problem: I Feel the Need...

***Note for 1st Years: you don't need to attempt/complete this problem in order to obtain a PDP point. That being said, it's a fun challenge, so we recommend you give it a go anyway ~~(and might help with future courseworks...)~~***

Open `optimise.py`. What does it do? Great question! That's not your problem. All we want you to do is make it run as fast as possible.

### Rules

- The code must run on the DCS machines
- The output of the optimised code must be the same as that of the original for all inputs

That's all - go wild.

### Getting started

#### Running the code locally

The Makefile provides a target `local`, which will run the code on your local machine. It can be run with:

```bash
make local
```

You can then change the input data to the program by modifying the values of `GRID_SIZE` and `NUM_AGENTS` in the Makefile, or setting them as environment variables.

Once you have got the hang of running the code, you can start trying to optimise it!

#### Checking your outputs

The Makefile provides a target `check`, which will try to compare the output of running your code against a set of provided solutions in the `expected/` directory. It will report if the output is the same, or show the difference between your output and the expected one. It can be run with:

```bash
make check
```

#### Running on DCS batch compute

**Please note that anything the runs correctly on your normal DCS account will run correctly on DCS batch compute as well!**

The Makefile provides a target `batch`, which will run your code on the DCS batch compute system, which you can [read more about here](https://warwick.ac.uk/fac/sci/dcs/intranet/user_guide/batch_compute/). This might take some time to queue and run, but allows you to run on the testing environment, and leverage some of the flags in the `sbatch` file. It can be run with:

```bash
make batch
```

### Submission

You need to submit a zip file containing:

- The `run.sbatch` file
- Any other required code files, for example `optimise.py`

The Makefile provides a target `submission`, which will zip up the contents of the bonus directory (which includes these things already) for you. It can be run with:

```bash
make submission
```

### Marking

We will unzip your submitted files, then test them using the `run.sbatch` file on the DCS batch compute system for a variety of input data. If any of the tests produce output different to the original, your submission will be disqualified. Finally, we will produce a ranking of valid solutions from fastest to slowest.

### A Good Place to Start
We want to make this challenge as fair as possible, so [here's an article you may want to read if you're stuck](https://medium.com/@guannan.shen.ai/compiler-optimizations-46db19221947)

---

Good Luck!

UWCS Academic Team
