
Initial Categories:
  - ToDo
  - Plan
  - Do
  - Done


Database structure:
  
  Tables:
    Kanbans - will list multiple distinctive kanbans, will start with single kanban
        Includes: id, date created, title, and is active (whether it is set as main)

    Categories - the columns of a kanban board describing each items status
        Includes: id, kanban id, column name

    Items
        Includes: id, kanban id, column id, item name, priority (ToBe: origin, event trigger)



Possible categories:
  - todo
  - planning solution
  - build
  - test 
  - deploy
  - pending
  - research
  - validate


Implementation Notes
  - use INTEGER PRIMARY KEY AUTORINCREMENT for primary key

Commnds(toBe):
  kanban ls - list
  kanban -a To-Do item - advance item
  kanban add new-item
      - how to best specify all fields?
      - have defaults,
  kanban -p To-Do item <new-priority>
  kanban pending 
      - show pending kanbans and what triggers them
      - contained at the process which will have the info of when to trigger
      - the trigger could be a trigger to the local process, or a foreign one
          - contained in function call info


Index

  Kanban table - lists all available kanbans, contains id, time created & name
      - how to track which is active? How to change? Active column?
      - for now, just start with one
      - id, name, time created

  Column table - lists all the kaban columns (todo, next...)
      - each references the kanban it belongs to
      - either: one standard table, or one for each kanban
      - columns designate what the process is capable of
      - should represent a specific action
      - id, column name, kanban id

  Item table - lists all items to complete (finish kanban, do laundry)
      - each references the column it belongs to
          - if columns are standardized, should also ref kanban
      - id, item, priority, event triggers, origin
      - must be fomrattable into a kanban card


Kanban:

    Kanban was intended for manufacturing and for repetitive processes. When a process must be completed, it is posted to an agent as a kanban card. This is specifically useful for tracking materials in inventory. When available, the kanban is kept with the materials, when unavailable, it is posted. 
    More generally, a kanban is a method of sharing tasks between different agents which can be connected together to help maintain an effective process. Automated systems could utilize this kind of tool to specify what needs it's attention, and what should be done once a task is completed.

  - each process could have a Kanban table specifying what it should do and what it is capable of
  - can include Pending Cards, which will trigger on specific events
  - An agent will then be responsible for consistently checking the db to see what should be done, based on the items, and some priority
  - inteneded for high level, adaptive processing, rather than low level, specific processes
  - Could also include event triggers, e.g. once the hose is replaced, trigger the kanban: water plants
  - Should also be able to table a kanban if there is some sort of problem
        - send to pending with a specified trigger
  - may also be useful to have a list of pending kanbans and their priorities in case something takes a long time
  - must be ablet to communicate with each other: Kanban cards! (JSON?)
  - each process could then include the (callable?) subpackage kanban, incl a db
  - How to trigger events? A centralized listener process? If so, this should be readily replaced if needed
      - Or should each process have a method of keeping track? Standardized comms?


KEEP IN MIND
  - this isn't necessary for immediate tasks, there is no reason to add complexityto a process that 
  - that being said, it could certainly be useful for task sharing, allowing for separate high level process to share the load

Other Notes:
  - Allows for active task scheduling. An agent can then use its perception, allowable actions and intelligence to work on a set of problems in a standardized way.
  - could then create a dedicated task manager which receives summaries of information, and schedule new kanban tasks if applicabel


Future additions:
  AUTOCOMPLETE - will make it significantly easier to manage
  Automated process test?
    - is there anything worthwhile to try out? RSS feed?
  Triggers - when a kanban is complete execute a function
  Links from item to notes/files
  Nested Kanbans?
  Librarian with kanban - save and organize bookmarks, papers and general information
      - new info added = new kanban card
      - upon receiving, librarian plans where to organize
      - can receive information request as well
      - could also link information (hyperlink? directory?)
      - could check if info is reorganized
