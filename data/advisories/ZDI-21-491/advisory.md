# ZDI-21-491: Apache Tapestry ContextAssetRequestHandler Incorrect Authorization Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-491
- **ZDI-CAN:** ZDI-CAN-12101
- **Date:** 2021-04-29
- **CVE:** CVE-2021-30638
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Apache
- **Affected Products:** Tapestry
- **Credit:** Kc Udonsi of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-491/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apache Tapestry. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ContextAssetRequestHandler class. The issue results from the improper filtering of HTTP requests. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

Apache has issued an update to correct this vulnerability. More details can be found at: https://lists.apache.org/thread.html/r37dab61fc7f7088d4311e7f995ef4117d58d86a675f0256caa6991eb%40%3Cusers.tapestry.apache.org%3E

## Disclosure Timeline

- 2021-03-24 - Vulnerability reported to vendor
- 2021-04-29 - Coordinated public release of advisory
