# ZDI-15-262: HP System Management Homepage Single Sign On Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-262
- **ZDI-CAN:** ZDI-CAN-2504
- **Date:** 2015-06-26
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** System Management
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-262/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard System Management Homepage. Authentication is not required to exploit this vulnerability. The specific flaw exists within the default handling of the Single Sign On (SSO) functionality. By providing an overly long parameter, an attacker is able to overflow a statically allocated stack buffer, and execute arbitrary code in the context of SYSTEM.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://www.hp.com/swpublishing/MTX-94e925ca071f4942ad39113cde

## Disclosure Timeline

- 2014-09-22 - Vulnerability reported to vendor
- 2015-06-26 - Coordinated public release of advisory
