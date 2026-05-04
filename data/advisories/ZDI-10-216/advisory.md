# ZDI-10-216: IBM Informix Dynamic Server oninit.exe EXPLAIN Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-216
- **ZDI-CAN:** ZDI-CAN-288
- **Date:** 2010-10-18
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Informix
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-216/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of IBM Informix Dynamic Server. Authentication is required in that an attacker must have valid credentials to connect to the database. The specific flaw exists within the oninit.exe process bound by default to TCP port 9088 or 1526. A lack of sanity checking within a logging function can result in a stack based buffer overflow leading to arbitrary code execution under the context of the SYSTEM user.

## Additional Details

this issue is fixed in version by defect # idsdb00154243 - 11.50.xC1 idsdb00154125 - 11.10.xC2W2

## Disclosure Timeline

- 2008-02-07 - Vulnerability reported to vendor
- 2010-10-18 - Coordinated public release of advisory
