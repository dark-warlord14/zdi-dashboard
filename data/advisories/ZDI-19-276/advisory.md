# ZDI-19-276: Microsoft Windows Deployment Services TFTP Server Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-276
- **ZDI-CAN:** ZDI-CAN-7597
- **Date:** 2019-03-12
- **CVE:** CVE-2019-0603
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** John Simpson
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-276/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. Authentication is not required to exploit this vulnerability. The specific flaw exists within WDSTFTP during TFTP read requests. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0603

## Disclosure Timeline

- 2018-11-26 - Vulnerability reported to vendor
- 2019-03-12 - Coordinated public release of advisory
