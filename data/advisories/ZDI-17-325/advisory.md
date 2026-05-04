# ZDI-17-325: (Pwn2Own) Microsoft Edge WriteClassesOfCategory DLL Planting Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-325
- **ZDI-CAN:** ZDI-CAN-4585
- **Date:** 2017-05-10
- **CVE:** CVE-2017-0233
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Tencent Security Team Ether
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-325/
## Vulnerability Details

This vulnerability allows remote attackers to escape the AppContainer sandbox on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the IBrowserBroker::WriteClassesOfCategory method. Executing this method can cause the broker process to load a module from an unqualified path. An attacker can leverage this in conjunction with other vulnerabilities to execute code under the context of the user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-0233

## Disclosure Timeline

- 2017-03-15 - Vulnerability reported to vendor
- 2017-05-10 - Coordinated public release of advisory
- 2018-03-06 - Advisory Updated
