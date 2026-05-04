# ZDI-25-316: Hewlett Packard Enterprise StoreOnce VSA Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-316
- **ZDI-CAN:** ZDI-CAN-24985
- **Date:** 2025-06-02
- **CVE:** CVE-2025-37093
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** StoreOnce VSA
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-316/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Hewlett Packard Enterprise StoreOnce VSA. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the machineAccountCheck method. The issue results from improper implementation of an authentication algorithm. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbst04847en_us&docLocale=en_US

## Disclosure Timeline

- 2024-10-31 - Vulnerability reported to vendor
- 2025-06-02 - Coordinated public release of advisory
- 2025-06-02 - Advisory Updated
