# ZDI-23-1586: SolarWinds Network Configuration Manager SaveResultsToFile Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1586
- **ZDI-CAN:** ZDI-CAN-21220
- **Date:** 2023-11-06
- **CVE:** CVE-2023-33227
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Network Configuration Manager
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1586/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Network Configuration Manager. Authentication is required to exploit this vulnerability. The specific flaw exists within the SaveResultsToFile method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://www.solarwinds.com/trust-center/security-advisories/cve-2023-33227

## Disclosure Timeline

- 2023-05-30 - Vulnerability reported to vendor
- 2023-11-06 - Coordinated public release of advisory
