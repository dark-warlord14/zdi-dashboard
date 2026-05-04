# ZDI-11-105: Hewlett-Packard Client Automation radexecd.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-105
- **ZDI-CAN:** ZDI-CAN-914
- **Date:** 2011-03-18
- **CVE:** CVE-2011-0889
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Client Automation
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-105/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Client Automation. Authentication is not required to exploit this vulnerability. The flaw exists within the radexecd.exe component which listens by default on TCP port 3465. When handling a remote execute request the process does not properly authenticate the user issuing the request. Utilities are stored in the 'secure' path which enable an attacker to re-execute an arbitrary executable. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02750690

## Disclosure Timeline

- 2010-09-23 - Vulnerability reported to vendor
- 2011-03-18 - Coordinated public release of advisory
