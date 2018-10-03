## The Project

In this project, you will load the TRIPS ontology and use selectional restrictions to assign the correct semantic roles to semantic templates.


# CSC 247/447 Programming Assignment \#1

In this assignment you will be reading the TRIPS ontology and then using it to perform some word sense disambiguation tasks.

### Loading the Ontology and Lexicon

The TRIPS ontology is provided as a JSON file for easy loading.  `code/ontology.py`
demonstrates how to load a JSON file.  If you run the code from the root directory of this project, you should see this:

```
project1> python code/ontology.py
there are 2907 nodes in the ontology
```

#### `ontology.json`

This file contains the semantic types and their arguments.  Each entry has the following fields:

```
{
	"name": "ACTIVITY",          // name of the type
	"parent": "EVENT-OF-ACTION", // the parent of the current type
	"children": [
		"DIETING",                 // list of children of the type
		"PHYSICAL-ACTIVITY",
		...
	],
	"wordnet": [		           // list of wordnet mappings to the type
		"project%1:04:00",
		"project%1:09:00",
		"activity%1:04:00"
	],
	"arguments": [                     // list of semantic arguments for the type
		{
			"role": "AGENT",         // role filled by the argument
			"restrictions": [        // role restriction, see below
				"REFERENTIAL-SEM"
			],
			"optionality": "ESSENTIAL",  // whether the role is required or not
			"implements": "AGENT"
		},
		...
	]
}
```

#### `lexicon.json`

This file contains mappings from words to ontology types.  Note the words are all
in their base form.  The full lexicon also contains morphology to allow us to match
other forms of the word (eg "run" and "running").

### Basic Functionality

Once you have the ontology loaded there is some basic functionality that you will need to implement. The first will be a function to determine if a type is a subtype of a second type.

A second key function implements an inheritance algorithm to produce a set of possible roles and selectional restrictions for a type. For example, given the type `CONSUME` we will find directly that it has an `AFFECTED` role restricted `FOOD`, `WATER` or `MEDICATION`, and has an inherited `AGENT` role restricted to be `ORGANISM`.
With `CONVERSING`, we find directly the `AGENT` AND `AGENT1` roles as one of `SOCIAL-GROUP-ABSTR`, `AGENT`, `SOCIAL-GROUP`, `ROBOT`,
`SUPERNATURAL-BEING`, or `ANIMAL`, and inherits the `FORMAL` role among others.

### The Task

You will be given a semantic template showing words (that you can look up in your ontology) and semantic roles relating them as in the following example:

```
(eat :AGENT bat :AFFECTED date)
```

Note that bat can be `NONHUMAN-ANIMAL` or a `MANUFACTURED-OBJECT` and date can be a `FRUIT` or a `TIME-POINT`. Your answer should specify the correct type for all the words in the pattern. So the answer for the example would be

```
(CONSUME :AGENT NONHUMAN-ANIMAL :AFFECTED FRUIT)
```

Note this was a simple case since eat has only one meaning in the ontology. A verb like run has four meanings, `EXECUTE`, `FUNCTION`, `GOVERNING` and `MOVE-RAPIDLY`. Sometimes the right sense can be determined by the roles that are given independent of the argument words. For instance, given

```
(run :AGENT he :AFFECTED machine)
```
only senses of run that allow both the `AGENT` and `AFFECTED` roles would be possible. In some cases, there are multiple solutions possible. In that case, your program should list each of the possibilities.

### Results

We will provide several examples for testing.  You should each additionally provide 10 of your own templates with the
correct answers (one correct answer for each, removing any output predicates which satisfy the restrictions but have the wrong meaning).

### Submission

Submit a `[yourname].zip` file on blackboard containing the folder structure provided.  Your code should be in the folder entitled `code` and your data should be in the folder entitled `data`.  Make sure to implement the methods in `code/test.py` to make grading easier.

The submission should contain:
* The original files in their current locations
* Any additional code files you need for your system to work
* An implemented `code/test.py` file.
* `report.{txt|pdf}` containing a description of your work including any specific running instructions and an outline of the algorithms you have implemented
* `input/[yourname]-templates.txt` containing a list of at least 10 templates you have come up with
* `[yourname]-templates.gold.txt` containing the correct answers for the templates you came up with
