# ZDI-24-1472: Veeam Backup Enterprise Manager AuthorizeByVMwareSsoToken Improper Certificate Validation Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1472
- **ZDI-CAN:** ZDI-CAN-24589
- **Date:** 2024-11-12
- **CVE:** CVE-2024-40715
- **CVSS:** 5.0
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Veeam
- **Affected Products:** Backup Enterprise Manager
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1472/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Veeam Backup Enterprise Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of security tokens. The issue results from improper certificate validation. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Veeam has issued an update to correct this vulnerability. More details can be found at: https://www.veeam.com/kb4682

## Disclosure Timeline

- 2024-07-12 - Vulnerability reported to vendor
- 2024-11-12 - Coordinated public release of advisory
- 2024-11-12 - Advisory Updated
