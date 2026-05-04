# ZDI-24-573: Trend Micro Apex One Security Agent Link Following Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-573
- **ZDI-CAN:** ZDI-CAN-22032
- **Date:** 2024-06-06
- **CVE:** CVE-2024-36307
- **CVSS:** 4.7
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** NT AUTHORITY\ANONYMOUS LOGON
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-573/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the VsApiNT module. By creating a mount point, an attacker can abuse the agent to disclose the contents of a file. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/dcx/s/solution/000298063?language=en_US

## Disclosure Timeline

- 2023-12-01 - Vulnerability reported to vendor
- 2024-06-06 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
