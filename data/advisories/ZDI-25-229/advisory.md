# ZDI-25-229: (Pwn2Own) Samsung Galaxy S24 Quick Share Directory Traversal Arbitrary File Write Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-229
- **ZDI-CAN:** ZDI-CAN-25650
- **Date:** 2025-04-09
- **CVE:** CVE-2024-49421
- **CVSS:** 5.9
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:L
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S24
- **Credit:** Ken Gannon of NCC Group (@yogehi)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-229/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to create arbitrary files on affected installations of Samsung Galaxy S24. An attacker must first obtain the ability to perform activities on the target device. The specific flaw exists within the Quick Share application. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to create files in the context of the current user.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: https://security.samsungmobile.com/serviceWeb.smsb?year=2024&month=12

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated
