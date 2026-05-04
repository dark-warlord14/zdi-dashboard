# ZDI-23-1006: SolarWinds Orion Platform SendHttpRequest Missing Authorization Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1006
- **ZDI-CAN:** ZDI-CAN-21090
- **Date:** 2023-07-27
- **CVE:** CVE-2023-33225
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Orion Platform
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1006/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Orion Platform. Authentication is required to exploit this vulnerability. The specific flaw exists within the SendHttpRequest action. The issue results from the lack of authorization prior to allowing access to functionality. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://www.solarwinds.com/trust-center/security-advisories/CVE-2023-33225

## Disclosure Timeline

- 2023-05-11 - Vulnerability reported to vendor
- 2023-07-27 - Coordinated public release of advisory
