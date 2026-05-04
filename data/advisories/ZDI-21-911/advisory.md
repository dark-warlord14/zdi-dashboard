# ZDI-21-911: Trend Micro Apex One Incorrect Permission Preservation Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-911
- **ZDI-CAN:** ZDI-CAN-13769
- **Date:** 2021-07-30
- **CVE:** CVE-2021-32465
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** HexKitchen
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-911/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Trend Micro Apex One. Authentication as a low-privileged Windows domain user is required to exploit this vulnerability. The specific flaw exists within the product patching functionality. When applying a patch to the product, the permissions on some files are not properly preserved. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000287819

## Disclosure Timeline

- 2021-04-28 - Vulnerability reported to vendor
- 2021-07-30 - Coordinated public release of advisory
