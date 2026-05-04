# ZDI-25-1019: Arista NG Firewall replace_marker Exposed Dangerous Function Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1019
- **ZDI-CAN:** ZDI-CAN-27007
- **Date:** 2025-11-25
- **CVE:** CVE-2025-6979
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Arista
- **Affected Products:** NG Firewall
- **Credit:** Gereon Huppertz
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1019/
## Vulnerability Details

This vulnerability allows remote attackers to to bypass authentication on affected installations of Arista NG Firewall. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handler.py module. The issue results from an exposed dangerous method. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Arista has issued an update to correct this vulnerability. More details can be found at: https://www.arista.com/en/support/advisories-notices/security-advisory/22535-security-advisory-0123

## Disclosure Timeline

- 2025-06-18 - Vulnerability reported to vendor
- 2025-11-25 - Coordinated public release of advisory
- 2025-11-25 - Advisory Updated
