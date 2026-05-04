# ZDI-24-883: Zen Cart findPluginAdminPage Local File Inclusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-883
- **ZDI-CAN:** ZDI-CAN-21408
- **Date:** 2024-06-26
- **CVE:** CVE-2024-5762
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Zen Cart
- **Affected Products:** Zen Cart
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-883/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Zen Cart. Authentication is not required to exploit this vulnerability. The specific flaw exists within the findPluginAdminPage function. The issue results from the lack of proper validation of user-supplied data prior to passing it to a PHP include function. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the service account.

## Additional Details

Zen Cart has issued an update to correct this vulnerability. More details can be found at: https://docs.zen-cart.com/release/whatsnew_2.0.0

## Disclosure Timeline

- 2023-08-28 - Vulnerability reported to vendor
- 2024-06-26 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
