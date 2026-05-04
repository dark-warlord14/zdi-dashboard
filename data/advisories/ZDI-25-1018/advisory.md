# ZDI-25-1018: Arista NG Firewall load_capture_settings Exposed Dangerous Function Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1018
- **ZDI-CAN:** ZDI-CAN-27006
- **Date:** 2025-11-25
- **CVE:** CVE-2025-6980
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Arista
- **Affected Products:** NG Firewall
- **Credit:** Gereon Huppertz
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1018/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Arista NG Firewall. Authentication is not required to exploit this vulnerability. The specific flaw exists within the logout.py module. The issue results from an exposed dangerous function. An attacker can leverage this vulnerability to disclose information in the context of root.

## Additional Details

Arista has issued an update to correct this vulnerability. More details can be found at: https://www.arista.com/en/support/advisories-notices/security-advisory/22535-security-advisory-0123

## Disclosure Timeline

- 2025-06-18 - Vulnerability reported to vendor
- 2025-11-25 - Coordinated public release of advisory
- 2025-11-25 - Advisory Updated
