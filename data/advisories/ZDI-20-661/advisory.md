# ZDI-20-661: FreeBSD Kernel NAT Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-661
- **ZDI-CAN:** ZDI-CAN-10850
- **Date:** 2020-05-19
- **CVE:** CVE-2020-7455
- **CVSS:** 4.1
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** FreeBSD
- **Affected Products:** Kernel
- **Credit:** Vishnu Dev TJ
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-661/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of FreeBSD Kernel. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of NAT. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of kernel.

## Additional Details

FreeBSD has issued an update to correct this vulnerability. More details can be found at: https://www.freebsd.org/security/advisories/FreeBSD-SA-20:13.libalias.asc

## Disclosure Timeline

- 2020-04-17 - Vulnerability reported to vendor
- 2020-05-19 - Coordinated public release of advisory
