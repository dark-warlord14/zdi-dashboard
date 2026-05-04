# ZDI-13-193: (Pwn2Own) Microsoft Internet Explorer Protected Mode Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-193
- **ZDI-CAN:** ZDI-CAN-1871
- **Date:** 2013-08-13
- **CVE:** N/A
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** VUPEN Security [ http://www.vupen.com ]
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-193/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of data shared to the broker by the sandboxed process. The issue lies in the failure to validate objects after a sandboxed process has terminated. An attacker can leverage this vulnerability to execute code as the context of the current user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-059

## Disclosure Timeline

- 2013-04-26 - Vulnerability reported to vendor
- 2013-08-13 - Coordinated public release of advisory
