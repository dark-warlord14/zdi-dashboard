# ZDI-09-099: Hewlett-Packard OpenView Data Protector Backup Client Service Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-099
- **ZDI-CAN:** ZDI-CAN-105
- **Date:** 2009-12-17
- **CVE:** CVE-2007-2280
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Data Protector
- **Credit:** Tenable Network Security Aaron Portnoy, TippingPoint DVLabs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-099/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard Storage Data Protector. Authentication is not required to exploit this vulnerability. The specific flaw exists within the backup client service daemon (OmniInet.exe), which binds to TCP port 5555. During the processing of long arguments to the 'MSG_PROTOCOL' command, a stack based buffer overflow occurs and can result in code execution under the context of the daemon.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c01124817

## Disclosure Timeline

- 2006-10-10 - Vulnerability reported to vendor
- 2009-12-17 - Coordinated public release of advisory
