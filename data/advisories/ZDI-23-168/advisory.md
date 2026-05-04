# ZDI-23-168: SolarWinds Network Performance Monitor sshd_SftpRename Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-168
- **ZDI-CAN:** ZDI-CAN-19907
- **Date:** 2023-02-24
- **CVE:** CVE-2022-47506
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Network Performance Monitor
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-168/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Network Performance Monitor. Authentication may be required to exploit this vulnerability, depending on the product configuration. The specific flaw exists within the sshd_SftpRename function. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://www.solarwinds.com/trust-center/security-advisories/CVE-2022-47506

## Disclosure Timeline

- 2022-12-22 - Vulnerability reported to vendor
- 2023-02-24 - Coordinated public release of advisory
