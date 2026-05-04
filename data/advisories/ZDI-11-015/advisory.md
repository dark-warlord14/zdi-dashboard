# ZDI-11-015: HP Mercury Loadrunner Agent Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-015
- **ZDI-CAN:** ZDI-CAN-768
- **Date:** 2011-01-12
- **CVE:** CVE-2011-0272
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** LoadRunner
- **Credit:** AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-015/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP LoadRunner. Authentication is not required to exploit this vulnerability. The specific flaw exists within the magentproc.exe process which binds by default on TCP ports 5001, 5002, 5003, 50500, and 54345. The process blindly trusts a user supplied 32-bit value as an allocation size. It then copies data directly from a request packet into the statically allocated heap buffer. This can be abused by attackers to execute remote code under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02680678

## Disclosure Timeline

- 2010-07-20 - Vulnerability reported to vendor
- 2011-01-12 - Coordinated public release of advisory
