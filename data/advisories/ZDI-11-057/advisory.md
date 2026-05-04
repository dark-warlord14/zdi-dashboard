# ZDI-11-057: (0Day) Hewlett-Packard Data Protector Cell Manager Service Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-057
- **ZDI-CAN:** ZDI-CAN-417
- **Date:** 2011-02-07
- **CVE:** CVE-2011-0921
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Data Protector
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-057/
## Vulnerability Details

This vulnerability allows an attacker to execute remote code on vulnerable installations of Hewlett-Packard Data Protector. User interaction is not required to exploit this vulnerability. The specific flaw exists within the Cell Manager Service which listens by default on a random TCP port. The crs.exe process fails to properly validate supplied username, domain, and hostname credentials. A remote attacker can leverage this flaw to execute code on all Data Protector clients.

## Disclosure Timeline

- 2009-01-26 - Vulnerability reported to vendor
- 2011-02-07 - Coordinated public release of advisory
