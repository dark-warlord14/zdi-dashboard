# ZDI-18-1135: Microsoft Windows SMB2 Out-Of-Bounds Access Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1135
- **ZDI-CAN:** ZDI-CAN-6415
- **Date:** 2018-10-10
- **CVE:** CVE-2018-8333
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Haikuo Xie of Baidu Security Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1135/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of SMB2 responses. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8333

## Disclosure Timeline

- 2018-06-28 - Vulnerability reported to vendor
- 2018-10-10 - Coordinated public release of advisory
- 2018-10-10 - Advisory Updated
