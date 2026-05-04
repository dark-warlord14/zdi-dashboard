# ZDI-08-001: IBM Tivoli Storage Manager Express Backup Server Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-001
- **ZDI-CAN:** ZDI-CAN-196
- **Date:** 2008-01-14
- **CVE:** CVE-2008-0247
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** IBM
- **Affected Products:** Tivoli Storage Manager Express
- **Credit:** Sebastian Apelt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-001/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of IBM Tivoli Storage Manager Express. Authentication is not required to exploit this vulnerability. The specific flaw resides in the TSM Express Backup Server service, dsmsvc.exe, which listens by default on TCP port 1500. The process trusts a user-supplied length value. By supplying a large number, an attacker can overflow a static heap buffer leading to arbitrary code execution in the context of the SYSTEM user.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-1.ibm.com/support/docview.wss?uid=swg21291536

## Disclosure Timeline

- 2007-12-05 - Vulnerability reported to vendor
- 2008-01-14 - Coordinated public release of advisory
