# ZDI-19-223: Malwarebytes Anti-Malware URI Handler Remote Command Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-223
- **ZDI-CAN:** ZDI-CAN-7162
- **Date:** 2019-02-20
- **CVE:** CVE-2019-6739
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Malwarebytes
- **Affected Products:** Anti-Malware
- **Credit:** rgod of 9sg Security Team - rgod@9sgsec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-223/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Malwarebytes Anti-Malware. User interaction is required to exploit this vulnerability in that the target must visit a malicious web page. There is an issue with the way the product handles URIs within certain schemes. The product does not warn the user that a dangerous navigation is about to take place. Because special characters in the URI are not sanitized, this could lead to the execution of arbitrary commands. An attacker can leverage this vulnerability to execute code in the context of the current user at medium integrity.

## Additional Details

This vulnerability report was resolved by builds including and after 3.6.1.2711-1.0.508.

## Disclosure Timeline

- 2018-10-25 - Vulnerability reported to vendor
- 2019-02-20 - Coordinated public release of advisory
- 2024-02-27 - Advisory Updated
