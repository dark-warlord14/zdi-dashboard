# ZDI-23-857: Trend Micro Apex Central Cross-Site Scripting Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-857
- **ZDI-CAN:** ZDI-CAN-18867
- **Date:** 2023-05-24
- **CVE:** CVE-2023-32535
- **CVSS:** 6.1
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex Central
- **Credit:** Poh Jia Hao of STAR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-857/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Trend Micro Apex Central. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the serverid parameter provided to the index.php component. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of arbitrary script. An attacker can leverage this vulnerability to execute script in the context of the current user.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000293107

## Disclosure Timeline

- 2022-12-29 - Vulnerability reported to vendor
- 2023-05-24 - Coordinated public release of advisory
- 2023-06-14 - Advisory Updated
