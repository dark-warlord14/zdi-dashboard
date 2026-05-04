# ZDI-20-684: NEC ESMPRO Manager RMI Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-684
- **ZDI-CAN:** ZDI-CAN-10007
- **Date:** 2020-06-01
- **CVE:** CVE-2020-10917
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NEC
- **Affected Products:** ESMPRO Manager
- **Credit:** Sivathmican Sivakumaran of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-684/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NEC ESMPRO Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the RMI service. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Fixed in version 11.0.5

## Disclosure Timeline

- 2020-01-16 - Vulnerability reported to vendor
- 2020-06-01 - Coordinated public release of advisory
