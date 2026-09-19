name = input("Enter patient name: ")

req = input("Enter requested departments: ").split()
avail = input("Enter available departments: ").split()
prev = input("Enter previously visited departments: ").split()
doc = input("Enter preferred doctors: ").split()
adoc = input("Enter available doctors: ").split()
emer = input("Enter emergency departments: ").split()

print("\nPATIENT:", name)

#list
print("\nRequested departments:", req)
print("First department:", req[0])
print("First 2 departments:", req[:2])

#set
r = set(req)
a = set(avail)
p = set(prev)
e = set(emer)

#same departments
common = r.intersection(a)

#unavail departs
un = r.difference(a)

#previous visited patients
old = r.intersection(p)

#emergency departs
em = r.intersection(e)

#duplicate reqs
dup = len(req) - len(r)
all_dep = r.union(a)
a.add("Emergency")


if "Emergency" in a:
    a.remove("Emergency")

#same doctors in common
d = set(doc).intersection(set(adoc))

#membership checks
if "Cardiology" in r:
    print("Cardiology is requested")

#departs recommend
if len(em) > 0:
    rec = list(em)[0]
elif len(common) > 0:
    rec = list(common)[0]
else:
    rec = "No department"

#status review
if len(em) > 0:
    status = "Emergency Appointment"
elif len(common) > 0:
    status = "Appointment Available"
else:
    status = "Appointment Not Available"

#printing dataaaaaaa
print("\n----- APPOINTMENT REPORT -----")
print("Patient Name:", name)
print("Requested:", req)
print("Available:", list(common))
print("Unavailable:", list(un))
print("Previous:", list(old))
print("Emergency:", list(em))
print("Duplicate Requests:", dup)
print("Common Doctors:", list(d))
print("Recommended Department:", rec)