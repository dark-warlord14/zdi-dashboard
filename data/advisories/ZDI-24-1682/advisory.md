# ZDI-24-1682: GeoVision GV-ASManager Missing Authorization Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1682
- **ZDI-CAN:** ZDI-CAN-25394
- **Date:** 2024-12-12
- **CVE:** CVE-2024-12553
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** GeoVision
- **Affected Products:** GV-ASManager
- **Credit:** Angela
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1682/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of GeoVision GV-ASManager. Although authentication is required to exploit this vulnerability, default guest credentials may be used. The specific flaw exists within the GV-ASWeb service. The issue results from the lack of authorization prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Fixed in ASManager version 6.1.1.0

## Disclosure Timeline

- 2024-11-19 - Vulnerability reported to vendor
- 2024-12-12 - Coordinated public release of advisory
- 2024-12-12 - Advisory Updated
