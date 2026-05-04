# ZDI-22-1663: SolarWinds Network Performance Monitor GetPdf Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1663
- **ZDI-CAN:** ZDI-CAN-17678
- **Date:** 2022-11-23
- **CVE:** CVE-2022-36962
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Network Performance Monitor
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1663/
## Vulnerability Details

This vulnerability allows remote attackers to execute code on affected installations of SolarWinds Network Performance Monitor. Authentication is required to exploit this vulnerability. The specific flaw exists within the GetPdf function. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://www.solarwinds.com/trust-center/security-advisories/cve-2022-36962

## Disclosure Timeline

- 2022-06-14 - Vulnerability reported to vendor
- 2022-11-23 - Coordinated public release of advisory
