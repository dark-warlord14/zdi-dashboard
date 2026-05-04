# ZDI-20-307: Trend Micro Worry-Free Business Security Directory Traversal Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-307
- **ZDI-CAN:** ZDI-CAN-10073
- **Date:** 2020-03-17
- **CVE:** CVE-2020-8600
- **CVSS:** 8.6
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Worry-Free Business Security
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-307/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Trend Micro Worry-Free Business Security. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the TempFileName parameter provided to the cgiRecvFile.exe endpoint. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000245572

## Disclosure Timeline

- 2020-01-21 - Vulnerability reported to vendor
- 2020-03-17 - Coordinated public release of advisory
