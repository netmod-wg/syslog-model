import os

list_of_ietf_models =\
[ ["ietf-tls-client", "draft-ietf-netconf-tls-client-server", "33"],
  ["ietf-crypto-types", "draft-ietf-netconf-crypto-types", "27"],
  ["ietf-tls-common", "draft-ietf-netconf-tls-client-server", "33"],
  ["ietf-truststore", "draft-ietf-netconf-trust-anchors", "21"],
  ["ietf-keystore", "draft-ietf-netconf-keystore", "28"],
  ["iana-tls-cipher-suite-algs", "draft-ietf-netconf-tls-client-server", "33"]]

def fetch_and_extract(draft, module, version):
    print("Fetching file " + draft + " with version " + version)
    draft_version = draft + "-" + version
    print(draft_version)
    os.system('curl -sO https://www.ietf.org/archive/id/%s.txt' %draft_version)
    print("Extracting Module from " + draft_version)
    os.system('xym %s.txt' %draft_version)
    print("Moving module " + module + " to ../bin/dependent/")
    os.system('mv %s* ../bin/dependent/' %module)
    print("Cleaning up ...")
    os.system('rm %s.txt' %draft_version)

def fetch(module, path):
    file = path + module + ".yang.txt"
    print("Fetching file " + file)
    os.system('curl -sO http://%s' %file)
    model = module + ".yang"
    print("Moving module " + model + " to ../bin/dependent/")
    os.system("mv '%s'.txt ../bin/dependent/'%s'" %(model, model))

os.system("mkdir -p ../bin/dependent")

for list in list_of_ietf_models:
    module, draft, version = list
    print(module)
    fetch_and_extract(draft, module, version)

# for list in list_of_ieee_models:
#    module, path = list
#    print(module)
#    fetch(module, path)

os.system('rm *.yang')
