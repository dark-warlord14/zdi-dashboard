# ZDI-20-1227: Trend Micro Maximum Security Race Condition Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1227
- **ZDI-CAN:** ZDI-CAN-10819
- **Date:** 2020-09-28
- **CVE:** CVE-2020-25775
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Maximum Security
- **Credit:** Abdelhamid Naceri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1227/
## Vulnerability Details

This vulnerability allows local attackers to delete arbitrary files on affected installations of Trend Micro Maximum Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the implementation of the Secure Erase feature. The issue results from the lack of proper validation of a user-supplied link prior to using it in file operations. An attacker can leverage this vulnerability to delete files in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/TMKA-09909

## Disclosure Timeline

- 2020-05-20 - Vulnerability reported to vendor
- 2020-09-28 - Coordinated public release of advisory
