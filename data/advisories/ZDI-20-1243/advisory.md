# ZDI-20-1243: Trend Micro Antivirus for Mac Improper Access Control Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1243
- **ZDI-CAN:** ZDI-CAN-10945
- **Date:** 2020-10-14
- **CVE:** CVE-2020-27013
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Antivirus for Mac
- **Credit:** Cees Elzinga from Danish Cyber Defence
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1243/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Trend Micro Antivirus for Mac. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the iCoreService endpoint, which listens on local TCP port 37848 by default. The issue results from improper access control. An attacker can leverage this vulnerability to disclose information in the context of root.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/TMKA-09950

## Disclosure Timeline

- 2020-06-11 - Vulnerability reported to vendor
- 2020-10-14 - Coordinated public release of advisory
