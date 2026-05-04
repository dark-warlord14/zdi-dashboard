# ZDI-11-115: IBM solidDB solid.exe Authentication Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-115
- **ZDI-CAN:** ZDI-CAN-963
- **Date:** 2011-04-01
- **CVE:** N/A
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** solidDB
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-115/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM solidDB. Authentication is not required to exploit this vulnerability. The specific flaw exists within the solid.exe process which listens by default on TCP ports 1315, 1964 and 2315. The authentication protocol allows a remote attacker to specify the length of a password hash. By specifying a minimum length the attacker can force the process to validate only the first several bytes of the password hash. This can be abused to bypass authentication to the database.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: https://www-304.ibm.com/support/docview.wss?uid=swg21474552

## Disclosure Timeline

- 2010-09-29 - Vulnerability reported to vendor
- 2011-04-01 - Coordinated public release of advisory
