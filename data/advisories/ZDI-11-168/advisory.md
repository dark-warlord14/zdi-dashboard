# ZDI-11-168: Multiple Vendor librpc.dll Remote Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-168
- **ZDI-CAN:** ZDI-CAN-808
- **Date:** 2011-05-16
- **CVE:** CVE-2011-0321 , CVE-2011-1210
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** IBM, EMC
- **Affected Products:** Informix
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-168/
## Vulnerability Details

This vulnerability allows remote attackers to register RPC services on vulnerable installations of EMC Legato Networker and IBM Informix Dynamic Server. Authentication is not required to exploit this vulnerability. The flaw exists within the librpc.dll component which listens by default on UDP port 111. When handling the pmap_set request the process verifies the source address is "127.0.0.1". This communication is via UDP and a valid source address is not required, a udp packet from source address "127.0.0.1" can be created sent to this service allowing a remote attacker to register and unregister RPC services. A remote attack can use this vulnerability to create a denial of service condition or eavesdrop on process communications.

## Additional Details

EMC (Fix posted January 31, 2011): CVE-2011-0321 http://archives.neohapsis.com/archives/bugtraq/2011-01/0162.html http://archives.neohapsis.com/archives/bugtraq/2011-01/att-0162/ESA-2011-003.txt IBM issued patch May 16, 2011: CVE-2011-1210 11.10 - http://www.ibm.com/support/docview.wss?uid=swg1IC76179 11.50 - http://www.ibm.com/support/docview.wss?uid=swg1IC76177 11.70 - http://www.ibm.com/support/docview.wss?uid=swg1IC76178

## Disclosure Timeline

- 2010-11-15 - Vulnerability reported to vendor
- 2011-05-16 - Coordinated public release of advisory
