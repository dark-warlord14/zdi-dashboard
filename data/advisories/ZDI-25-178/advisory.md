# ZDI-25-178: (0Day) CarlinKit CPC200-CCPA update.cgi Improper Verification of Cryptographic Signature Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-178
- **ZDI-CAN:** ZDI-CAN-24355
- **Date:** 2025-03-25
- **CVE:** CVE-2025-2764
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** CarlinKit
- **Affected Products:** CPC200-CCPA
- **Credit:** Aaron Luo and Spencer Hsieh of VicOne
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-178/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of CarlinKit CPC200-CCPA devices. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of update packages provided to update.cgi. The issue results from the lack of proper verification of a cryptographic signature. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

06/05/24 – ZDI contacted the vendor’s support team via email 07/12/24 – ZDI sent a second PSIRT contact request to CarlinKit support team 11/13/24 – ZDI asked for updates 02/18/25 – ZDI informed the vendor that since we have not received a response, we will publish the report as a 0-day advisory

## Disclosure Timeline

- 2025-03-11 - Vulnerability reported to vendor
- 2025-03-25 - Coordinated public release of advisory
- 2025-03-25 - Advisory Updated
