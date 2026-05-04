# ZDI-21-771: (Pwn2Own) Microsoft Teams amsVideo Cross Site Scripting Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-771
- **ZDI-CAN:** ZDI-CAN-13482
- **Date:** 2021-07-05
- **CVE:** N/A
- **CVSS:** 6.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Teams
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-771/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Teams Desktop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the amsVideo parameter provided to the Teams endpoint. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

fixed in version 1.4.00.11161

## Disclosure Timeline

- 2021-04-07 - Vulnerability reported to vendor
- 2021-07-05 - Coordinated public release of advisory
