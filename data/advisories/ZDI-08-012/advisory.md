# ZDI-08-012: IBM Informix Dynamic Server Authentication Password Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-012
- **ZDI-CAN:** ZDI-CAN-255
- **Date:** 2008-03-13
- **CVE:** CVE-2008-0727
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** IBM
- **Affected Products:** Informix
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-012/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of IBM's Informix Dynamic Server. User interaction is not required to exploit this vulnerability. Authentication is not required to exploit this vulnerability. The specific flaw exists in the oninit.exe process that listens by default on TCP port 1526. During authentication, the process does not validate the length of the supplied user password. An attacker can provide a overly long password and overflow a stack based buffer resulting in arbitrary code execution.

## Additional Details

IBM has released an update available at the following URLs: http://www-1.ibm.com/support/docview.wss?uid=swg1IC55210 http://www-1.ibm.com/support/docview.wss?uid=swg1IC55209

## Disclosure Timeline

- 2007-11-07 - Vulnerability reported to vendor
- 2008-03-13 - Coordinated public release of advisory
