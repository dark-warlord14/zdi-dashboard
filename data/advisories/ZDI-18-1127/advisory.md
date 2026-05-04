# ZDI-18-1127: Cisco WebEx Network Recording Player ARF File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1127
- **ZDI-CAN:** ZDI-CAN-6356
- **Date:** 2018-10-08
- **CVE:** CVE-2018-15415
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1127/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco WebEx Network Recording Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ATPDMOD.DLL module. When parsing an ARF file, the process does not properly validate a vtable entry before executing it, resulting in stack corruption. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20181003-webex-rce

## Disclosure Timeline

- 2018-07-23 - Vulnerability reported to vendor
- 2018-10-08 - Coordinated public release of advisory
- 2018-10-08 - Advisory Updated
