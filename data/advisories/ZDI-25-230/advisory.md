# ZDI-25-230: (Pwn2Own) Samsung Galaxy S24 Smart Switch Agent Improper Verification of Cryptographic Signature Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-230
- **ZDI-CAN:** ZDI-CAN-25651
- **Date:** 2025-04-09
- **CVE:** CVE-2024-49413
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S24
- **Credit:** Ken Gannon of NCC Group (@yogehi)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-230/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Samsung Galaxy S24. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Smart Switch Agent application. The issue results from the lack of proper validation of cryptographic signature before installing an application. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: https://security.samsungmobile.com/securityUpdate.smsb?year=2024&month=12

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated
