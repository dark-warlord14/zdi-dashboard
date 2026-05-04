# ZDI-20-293: Parallels Desktop xHCI Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-293
- **ZDI-CAN:** ZDI-CAN-9428
- **Date:** 2020-03-13
- **CVE:** CVE-2020-8872
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** Reno Robert of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-293/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the xHCI component. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

Fixed in version 15.1.3 (47255)

## Disclosure Timeline

- 2019-11-20 - Vulnerability reported to vendor
- 2020-03-13 - Coordinated public release of advisory
- 2021-03-02 - Advisory Updated
