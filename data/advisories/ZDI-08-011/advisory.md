# ZDI-08-011: IBM Informix Dynamic Server DBPATH Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-011
- **ZDI-CAN:** ZDI-CAN-254
- **Date:** 2008-03-13
- **CVE:** CVE-2008-0727
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** IBM
- **Affected Products:** Informix
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-011/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of IBM's Informix Dynamic Server. User interaction is not required to exploit this vulnerability. Authentication is required in that an attacker must have database connection priviliges. The specific flaw exists in the oninit.exe process that listens by default on TCP port 1526. During authentication, the process does not validate the length of the DBPATH variable. An attacker can provide a overly long variable name and overflow a global buffer, overwriting function pointers leading to arbitrary code execution.

## Additional Details

IBM has released an update available at the following URLs: http://www-1.ibm.com/support/docview.wss?uid=swg1IC55208 http://www-1.ibm.com/support/docview.wss?uid=swg1IC55207

## Disclosure Timeline

- 2007-11-07 - Vulnerability reported to vendor
- 2008-03-13 - Coordinated public release of advisory
