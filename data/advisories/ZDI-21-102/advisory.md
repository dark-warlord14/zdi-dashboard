# ZDI-21-102: Trend Micro Antivirus for Mac Memory Exhaustion Denial-Of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-102
- **ZDI-CAN:** ZDI-CAN-11605
- **Date:** 2021-01-29
- **CVE:** CVE-2021-25227
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:L
- **Affected Vendors:** Trend Micro
- **Affected Products:** Antivirus for Mac
- **Credit:** Michael DePlante of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-102/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Trend Micro Antivirus for Mac. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the iCoreService executable. The issue results from the lack of proper validation of user-supplied data, which can result in a memory exhaustion condition. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/TMKA-10191

## Disclosure Timeline

- 2020-07-30 - Vulnerability reported to vendor
- 2021-01-29 - Coordinated public release of advisory
