# ZDI-22-375: SolarWinds Orion Platform Unrestricted File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-375
- **ZDI-CAN:** ZDI-CAN-13664
- **Date:** 2022-02-16
- **CVE:** CVE-2021-35244
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Orion Platform
- **Credit:** @fkadibs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-375/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Orion Platform. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of alert creation. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://support.solarwinds.com/SuccessCenter/s/article/Orion-Platform-2020-2-6-Hotfix-3?language=en_US

## Disclosure Timeline

- 2021-08-20 - Vulnerability reported to vendor
- 2022-02-16 - Coordinated public release of advisory
