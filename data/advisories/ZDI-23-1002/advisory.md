# ZDI-23-1002: SolarWinds Network Configuration Manager VulnDownloader Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1002
- **ZDI-CAN:** ZDI-CAN-20995
- **Date:** 2023-07-27
- **CVE:** CVE-2023-23842
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Network Configuration Manager
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1002/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Network Configuration Manager. Authentication is required to exploit this vulnerability. The specific flaw exists within the VulnDownloader class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://www.solarwinds.com/trust-center/security-advisories/cve-2023-23842

## Disclosure Timeline

- 2023-05-03 - Vulnerability reported to vendor
- 2023-07-27 - Coordinated public release of advisory
