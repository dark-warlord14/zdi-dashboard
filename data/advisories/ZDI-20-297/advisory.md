# ZDI-20-297: Parallels Desktop OS X Host Kernel Module Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-297
- **ZDI-CAN:** ZDI-CAN-10029
- **Date:** 2020-03-13
- **CVE:** CVE-2020-8876
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** grigoritchy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-297/
## Vulnerability Details

This vulnerability allows local attackers to disclose information on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the IOCTL handler. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Fixed in version 15.1.3 (47255)

## Disclosure Timeline

- 2020-02-26 - Vulnerability reported to vendor
- 2020-03-13 - Coordinated public release of advisory
