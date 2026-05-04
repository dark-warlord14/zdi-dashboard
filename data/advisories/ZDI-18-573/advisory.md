# ZDI-18-573: (Pwn2Own) Microsoft Windows D3DKMTCreateDCFromMemory Memory Corruption Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-573
- **ZDI-CAN:** ZDI-CAN-5823
- **Date:** 2018-06-08
- **CVE:** CVE-2018-8164
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Richard Zhu (fluorescence)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-573/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the creation of a device context from memory using the D3DKMTCreateDCFromMemory API. When processing the width parameter, the process does not properly validate user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to escalate privileges to SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8164

## Disclosure Timeline

- 2018-03-18 - Vulnerability reported to vendor
- 2018-06-08 - Coordinated public release of advisory
- 2018-06-08 - Advisory Updated
