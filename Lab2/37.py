#Nested Dictionary

myfamily = {
    "child" : {
        "name" : "Emily",
        "year" : 2004
    },
    "child2":{
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}
#dictionary which contains dictionaries




child1 = {
        "name" : "Emily",
        "year" : 2004
    },
child2 = {
        "name" : "Tobias",
        "year" : 2007
    },
child3 = {
        "name" : "Linus",
        "year" : 2011
    }

myfamily  = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3 

}
#dictionary contains other three dictionaries


print(myfamily["child2"] ["name"])

