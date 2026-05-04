# ZDI-09-053: Microsoft Windows WINS Service Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-053
- **ZDI-CAN:** ZDI-CAN-437
- **Date:** 2009-08-11
- **CVE:** CVE-2009-1923
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft
- **Affected Products:** Windows 2003 SP2, Windows 2000 SP4
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-053/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. Authentication is not required to exploit this vulnerability. The specific flaw exists within the WINS.exe process which provides name resolution services for NetBIOS networks. While parsing a push request the WINS service copies packet data to a static heap buffer while within a controlled loop. By providing a specially crafted request an attacker can overflow this heap buffer leading to arbitrary code execution under the SYSTEM context.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS09-039.mspx

## Disclosure Timeline

- 2009-02-24 - Vulnerability reported to vendor
- 2009-08-11 - Coordinated public release of advisory
