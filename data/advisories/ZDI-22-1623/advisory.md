# ZDI-22-1623: Hewlett Packard Enterprise OfficeConnect 1820 Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1623
- **ZDI-CAN:** ZDI-CAN-17747
- **Date:** 2022-11-21
- **CVE:** CVE-2022-37932
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** OfficeConnect 1820
- **Credit:** Fernando Munoz
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1623/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Hewlett Packard Enterprise OfficeConnect 1820 switches. Authentication is not required to exploit this vulnerability. The specific flaw exists within the default_password_cfg.lua endpoint. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to bypass authentication on the system and execute code in the context of root.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpesc/public/docDisplay?docLocale=en_US&docId=hpesbnw04383en_us

## Disclosure Timeline

- 2022-09-22 - Vulnerability reported to vendor
- 2022-11-21 - Coordinated public release of advisory
