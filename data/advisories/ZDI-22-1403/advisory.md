# ZDI-22-1403: Trend Micro Apex One Forced Browsing Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1403
- **ZDI-CAN:** ZDI-CAN-18013
- **Date:** 2022-10-07
- **CVE:** CVE-2022-41746
- **CVSS:** 9.1
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Elias Martinez (FileNotFound - https://www.linkedin.com/in/eli-martinez07/ )
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1403/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Trend Micro Apex One. Authentication is required to exploit this vulnerability. The specific flaw exists within the Apex One web console. By navigating directly to a URL, a user can bypass authorization and gain write access to server configuration. An attacker can leverage this vulnerability to escalate privileges and reconfigure the server and associated endpoint agents.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/dcx/s/solution/000291645?language=en_US

## Disclosure Timeline

- 2022-08-04 - Vulnerability reported to vendor
- 2022-10-07 - Coordinated public release of advisory
