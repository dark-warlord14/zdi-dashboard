# ZDI-10-004: Cisco CiscoWorks IPM GIOP getProcessName Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-004
- **ZDI-CAN:** ZDI-CAN-396
- **Date:** 2010-01-21
- **CVE:** CVE-2010-0138
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Cisco
- **Affected Products:** Internetwork Performance Monitor
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-004/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco CiscoWorks Internetwork Performance Monitor. Authentication is not required to exploit this vulnerability. The specific flaw exists in the handling of CORBA GIOP requests. By making a specially crafted getProcessName GIOP request an attacker can corrupt memory. Successful exploitation can result in a full compromise with SYSTEM credentials.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: http://www.cisco.com/en/US/products/products_security_advisory09186a0080b1351d.shtml

## Disclosure Timeline

- 2008-10-15 - Vulnerability reported to vendor
- 2010-01-21 - Coordinated public release of advisory
