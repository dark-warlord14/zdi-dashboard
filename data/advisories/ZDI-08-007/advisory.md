# ZDI-08-007: Symantec VERITAS Storage Foundation Administrator Service Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-007
- **ZDI-CAN:** ZDI-CAN-227
- **Date:** 2008-02-20
- **CVE:** CVE-2008-0638
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Symantec
- **Affected Products:** Veritas Storage Foundation
- **Credit:** Sebastian Apelt (webmaster@buzzworld.org)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-007/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Symantec VERITAS Storage Foundation. Authentication is not required to exploit this vulnerability. The specific flaw resides in the Administrator service, vxsvc.exe, which listens by default on UDP port 3207. The process trusts a user-supplied size value, receiving the specified amount of data into a static heap buffer. By sending a specially crafted packet, an attacker can overflow that buffer leading to arbitrary code execution in the context of the SYSTEM user.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/avcenter/security/Content/2008.02.20a.html

## Disclosure Timeline

- 2007-09-14 - Vulnerability reported to vendor
- 2008-02-20 - Coordinated public release of advisory
