# ZDI-22-789: Trend Micro Maximum Security Link Following Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-789
- **ZDI-CAN:** ZDI-CAN-15739
- **Date:** 2022-05-26
- **CVE:** CVE-2022-30687
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Maximum Security
- **Credit:** Amir Ahmadi (@KingAmir )
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-789/
## Vulnerability Details

This vulnerability allows local attackers to delete arbitrary files on affected installations of Trend Micro Maximum Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the implementation of the Secure Erase feature. The issue results from the lack of proper validation of a user-supplied link prior to using it in file operations. An attacker can leverage this vulnerability to delete files in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/tmka-11017

## Disclosure Timeline

- 2022-01-14 - Vulnerability reported to vendor
- 2022-05-26 - Coordinated public release of advisory
