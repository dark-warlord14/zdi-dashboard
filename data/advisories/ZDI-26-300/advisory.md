# ZDI-26-300: Flowise AccountService resetPassword Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-300
- **ZDI-CAN:** ZDI-CAN-28762
- **Date:** 2026-04-27
- **CVE:** CVE-2026-41276
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Flowise
- **Affected Products:** Flowise
- **Credit:** Nicholas Zubrisky (@NZubrisky) of TrendAI Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-300/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Flowise. Authentication is not required to exploit this vulnerability. The specific flaw exists within the resetPassword method of the AccountService class. The issue results from improper implementation of the password reset mechanism. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Flowise has issued an update to correct this vulnerability. More details can be found at: https://github.com/FlowiseAI/Flowise/commit/6c78e1c36f4cf08874b9b7a444d61ab63441d78a

## Disclosure Timeline

- 2026-02-19 - Vulnerability reported to vendor
- 2026-04-27 - Coordinated public release of advisory
- 2026-04-27 - Advisory Updated
