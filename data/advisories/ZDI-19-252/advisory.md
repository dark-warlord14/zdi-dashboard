# ZDI-19-252: Unity com.unity3d.kharma Protocol Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-252
- **ZDI-CAN:** ZDI-CAN-7242
- **Date:** 2019-03-05
- **CVE:** CVE-2019-9197
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Unity Technologies
- **Affected Products:** Unity
- **Credit:** rgod of 9sg Security Team - rgod@9sgsec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-252/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Unity Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handler for the com.unity3d.kharma protocol. A crafted URI with the com.unity3d.kharma protocol can trigger execution of a system call composed from a user-supplied string. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Unity Technologies has issued an update to correct this vulnerability. More details can be found at: https://unity3d.com/security#CVE-2019-9197

## Disclosure Timeline

- 2018-09-14 - Vulnerability reported to vendor
- 2019-03-05 - Coordinated public release of advisory
