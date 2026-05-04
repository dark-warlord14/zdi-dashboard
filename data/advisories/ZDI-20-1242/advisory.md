# ZDI-20-1242: Trend Micro Antivirus for Mac Protection Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1242
- **ZDI-CAN:** ZDI-CAN-11046
- **Date:** 2020-10-14
- **CVE:** CVE-2020-25777
- **CVSS:** 5.4
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Antivirus for Mac
- **Credit:** Cees Elzinga from Danish Cyber Defence
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1242/
## Vulnerability Details

This vulnerability allows remote attackers to bypass web filtering on affected installations of Trend Micro Antivirus for Mac. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the KERedirect module. The issue results from the improper filtering of HTTP requests. An attacker can leverage this vulnerability to bypass the protection offered by the product.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/TMKA-09947

## Disclosure Timeline

- 2020-06-11 - Vulnerability reported to vendor
- 2020-10-14 - Coordinated public release of advisory
