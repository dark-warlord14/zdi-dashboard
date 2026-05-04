# ZDI-23-655: Trend Micro Apex One Improper Access Control Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-655
- **ZDI-CAN:** ZDI-CAN-18290
- **Date:** 2023-05-17
- **CVE:** CVE-2023-32552
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Elias Martinez (FileNotFound - https://www.linkedin.com/in/eli-martinez07/ )
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-655/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Trend Micro Apex One. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web console, which listens on TCP port 4343 by default. The issue results from improper access control. An attacker can leverage this vulnerability to disclose information from the application.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000293108

## Disclosure Timeline

- 2022-10-18 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
