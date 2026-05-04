# ZDI-20-456: Microsoft Windows KERNELBASE Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-456
- **ZDI-CAN:** ZDI-CAN-9748
- **Date:** 2020-04-15
- **CVE:** CVE-2020-0821
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** xina1i
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-456/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the KERNELBASE.dll module. When parsing the Resource Directory Entry field of a Portable Executable format file, the process does not properly validate user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0821

## Disclosure Timeline

- 2019-12-03 - Vulnerability reported to vendor
- 2020-04-15 - Coordinated public release of advisory
