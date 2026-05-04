# ZDI-25-228: (Pwn2Own) Samsung Galaxy S24 Quick Share Insufficient UI Warning Arbitrary File Write Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-228
- **ZDI-CAN:** ZDI-CAN-25649
- **Date:** 2025-04-09
- **CVE:** N/A
- **CVSS:** 5.3
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S24
- **Credit:** Ken Gannon of NCC Group (@yogehi)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-228/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to create arbitrary files on affected installations of Samsung Galaxy S24. An attacker must first obtain the ability to perform activities on the target device. The specific flaw exists within the Quick Share application. The user interface fails to warn the user of unsafe actions. An attacker can leverage this vulnerability to create files in the context of the current user.

## Additional Details

The vendor states this is intended behavior for better user experience. Therefore, there is no acknowledgement or patch for this.

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated
